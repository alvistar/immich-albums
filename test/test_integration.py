import os.path
from pathlib import Path
from typing import Tuple

import pytest
from testcontainers.compose import DockerCompose
from testcontainers.core.waiting_utils import wait_for_logs
import openapi_client
from openapi_client import ApiException
from immich_albums.im import ImmichAlbums

db_user = "postgres"
db_password = "postgres"
db_name = "immich"


def init_admin_user() -> Tuple[str, str, str]:
    api_configuration = openapi_client.Configuration(
        host="http://localhost:2283/api",
    )

    access_token = None
    api_key = None
    admin_id = None

    with openapi_client.ApiClient(api_configuration) as api_client:
        email = "admin@gmail.com"
        admin_name = "admin"
        password = "admin"

        api_instance = openapi_client.AuthenticationApi(api_client)
        signup_dto = openapi_client.SignUpDto(
            email=email, name=admin_name, password=password
        )
        try:
            print("Creating admin user...\n")
            api_response = api_instance.sign_up_admin(signup_dto)
            admin_id = api_response.id
            print(f"Created admin with id {admin_id}\n")
        except ApiException as e:
            print(f"Exception while creating admin: {e}\n")

        try:
            print("Logging in admin user...\n")
            login_credentials = openapi_client.LoginCredentialDto(
                email=email, password=password
            )
            api_response = api_instance.login(login_credentials)
            print(f"Logged in successfully with token {api_response.access_token}\n")
            access_token = api_response.access_token
        except ApiException as e:
            print(f"Exception while logging in admin: {e}\n")

    api_configuration = openapi_client.Configuration(
        host="http://localhost:2283/api", access_token=access_token
    )

    with openapi_client.ApiClient(api_configuration) as api_client:
        api_instance = openapi_client.UserApi(api_client)
        try:
            print("Setting external path\n")
            dto = openapi_client.UpdateUserDto(
                id=admin_id, external_path="/mnt/ext_library"
            )

            response = api_instance.update_user(dto)
            print("External path set successfully.\n")
        except ApiException as e:
            print(f"Exception while setting external path {e}\n")

        api_instance = openapi_client.APIKeyApi(api_client)
        try:
            print("Creating API key\n")
            dto = openapi_client.APIKeyCreateDto(
                name="admin_key",
            )
            response = api_instance.create_api_key(dto)
            api_key = response.secret
            print(f"API key created with secret {api_key}\n")

        except ApiException as e:
            print(f"Exception while creating API key: {e}\n")

    return access_token, api_key, admin_id


def setup_external_library(token: str, owner_id: str):
    api_configuration = openapi_client.Configuration(
        host="http://localhost:2283/api", api_key={"api_key": token}
    )

    library_id = None

    with openapi_client.ApiClient(api_configuration) as api_client:
        api_instance = openapi_client.LibraryApi(api_client)

        dto = openapi_client.CreateLibraryDto(
            name="My Library",
            owner_id=owner_id,
            type=openapi_client.LibraryType.EXTERNAL,
            import_paths=["/mnt/ext_library"],
        )

        try:
            api_response = api_instance.create_library(dto)
            library_id = api_response.id
            print(f"Library created with id {library_id}\n")

        except ApiException as e:
            print(f"Exception while creating library: {e}\n")

        try:
            api_instance.scan_library(library_id, openapi_client.ScanLibraryDto())
            print(f"Started library scan successfully")
        except ApiException as e:
            print(f"Exception while scanning library: {e}\n")

        wait_for_jobs(token)


def wait_for_jobs(token: str):
    api_configuration = openapi_client.Configuration(
        host="http://localhost:2283/api", api_key={"api_key": token}
    )

    with openapi_client.ApiClient(api_configuration) as api_client:
        api_instance = openapi_client.JobApi(api_client)

        try:
            print("Waiting for jobs to finish\n")
            response = api_instance.get_all_jobs_status()
            while response.library.job_counts.active > 0:
                print(
                    f"Waiting for {response.library.job_counts.active} jobs to finish\n"
                )
                response = api_instance.get_all_jobs_status()

        except ApiException as e:
            print(f"Exception while getting jobs: {e}\n")


@pytest.fixture(scope="session")
def immich_app():
    compose = DockerCompose("immich-app")
    with compose:
        # Wait for the container to start
        delay = wait_for_logs(compose, "Immich Server is listening on")
        stdout, stderr = compose.get_logs()
        print(stdout.decode("utf-8"))

        access_token, api_key, admin_id = init_admin_user()
        setup_external_library(api_key, admin_id)

        yield api_key


# Define a fixture that will search for and delete `.album` files in a specified directory
@pytest.fixture
def remove_album_files(request):
    directory_path = Path(
        "immich-app/ext_library"
    )  # Change this to your target directory

    def teardown():
        for path in directory_path.rglob(".album"):
            try:
                path.unlink()
                print(f"Deleted {path}")
            except Exception as e:
                print(f"Error deleting {path}: {e}")

    request.addfinalizer(teardown)


def test_create_albums(immich_app, remove_album_files):
    api_key = immich_app

    immich_albums = ImmichAlbums("http://localhost:2283/api", api_key)

    abs_path = os.path.abspath("./immich-app/ext_library")

    print(f"Creating albums from {abs_path}\n")

    immich_albums.create_albums_from_folder(
        path=abs_path,
        original_path=abs_path,
        replace_path="/mnt/ext_library",
        recursive=True,
    )

    api_configuration = openapi_client.Configuration(
        host="http://localhost:2283/api", api_key={"api_key": api_key}
    )

    with openapi_client.ApiClient(api_configuration) as api_client:
        api_instance = openapi_client.AlbumApi(api_client)
        try:
            print("Getting albums\n")
            albums = api_instance.get_all_albums()
            print(albums)
            assert len(albums) == 3
            assert any(album.album_name == "paris" for album in albums)
            assert any(album.album_name == "rome" for album in albums)

            paris_album = next(album for album in albums if album.album_name == "paris")
            assert paris_album.asset_count == 2

        except ApiException as e:
            print(f"Exception while getting albums: {e}\n")
