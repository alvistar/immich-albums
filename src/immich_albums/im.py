from typing import Optional

import os
import click
import openapi_client
from openapi_client import ApiException, AlbumResponseDto

from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def write_album_id(path, id):
    with open(os.path.join(path, ".album"), 'w') as f:
        f.write(id)


def read_album_id(path) -> Optional[str]:
    try:
        with open(os.path.join(path, ".album"), 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None


class ImmichAlbums:
    def __init__(self, api_host, api_key):
        api_configuration = openapi_client.Configuration(
            host=api_host,
        )

        api_configuration.api_key['api_key'] = api_key

        self.api_configuration = api_configuration

    def get_asset_by_original_path(self, original_path) -> Optional[int]:
        with openapi_client.ApiClient(self.api_configuration) as api_client:
            # Create an instance of the API class
            api_instance = openapi_client.AssetApi(api_client)

            assets = api_instance.search_assets(original_path=original_path)
            return assets[0].id if len(assets) > 0 else None

    def create_album(self, album_name, assets_ids) -> str:
        with openapi_client.ApiClient(self.api_configuration) as api_client:
            # Create an instance of the API class
            api_instance = openapi_client.AlbumApi(api_client)

        try:
            print(f"Creating album {album_name}\n")

            create_album_request = openapi_client.CreateAlbumDto(
                album_name=album_name,
                asset_ids=assets_ids,
            )

            api_response: AlbumResponseDto = api_instance.create_album(create_album_request)

            print(f"Album id {api_response.id}")
            print("The response of create album:\n")
            print(api_response)

            return api_response.id
        except ApiException as e:
            print(f"Exception when calling create_album: {e}\n")

    def add_picture_to_album(self, album_id, asset_ids):
        with openapi_client.ApiClient(self.api_configuration) as api_client:
            # Create an instance of the API class
            api_instance = openapi_client.AlbumApi(api_client)

            try:
                print(f"Adding assets to album {album_id}\n")
                bulkIdsDto = openapi_client.BulkIdsDto(ids=asset_ids)
                api_response = api_instance.add_assets_to_album(album_id, bulkIdsDto)
                print("The response of add asset to album:\n")
                print(api_response)
            except ApiException as e:
                print(f"Exception when calling create_album: {e}\n")

    def get_assets_in_folder(self, folder: str, original_path: str, replace_path: str):
        assets_ids = []

        for filename in os.listdir(folder):
            full_path = os.path.join(folder, filename)
            if os.path.isfile(full_path):
                replaced_path = full_path.replace(original_path, replace_path)
                print(f"searching for: {replaced_path}")
                asset_id = self.get_asset_by_original_path(replaced_path)
                if asset_id is None:
                    print(f'not found: {replaced_path}')
                else:
                    print(f'found asset id: {asset_id}')
                    assets_ids.append(asset_id)

        return [str(asset_id) for asset_id in assets_ids]

    def create_album_from_folder(self, path: str, original_path: str, replace_path: str,
                                 dry_run: bool = False, skip_existing: bool = False):
        album = os.path.basename(path)

        album_id = read_album_id(path)
        if album_id:
            print(f"Album {album} exists with id {album_id}")

            if skip_existing:
                print(f"Skipping existing album {album}")
                return
        else:
            print(f"Album {album} does not exist")

        assets_ids = self.get_assets_in_folder(path, original_path, replace_path)

        if not dry_run:
            if album_id:
                print(f"Adding assets to album {album_id}")
                self.add_picture_to_album(album_id, assets_ids)
            else:
                album_id = self.create_album(album, assets_ids)
                print("Creating .album")
                write_album_id(path, album_id)
        else:
            print(f"DRY RUN: Creating album {album}")
            print(f"DRY RUN: Assets ids: {assets_ids}")

    def create_albums_from_folder(self,
                                  path: str,
                                  original_path: str,
                                  replace_path: str,
                                  recursive: bool = False,
                                  dry_run: bool = False,
                                  skip=None,
                                  skip_existing: bool = False
                                  ):

        if skip is None:
            skip = []

        if recursive:
            for folder_name, sub_folders, filenames in os.walk(path):
                if folder_name in skip:
                    print(f"Skipping folder: {folder_name}")
                    continue
                print(f"Processing folder: {folder_name}\n")
                self.create_album_from_folder(path, original_path, replace_path, dry_run, skip_existing=skip_existing)

                for sub_folder in sub_folders:
                    path = os.path.join(folder_name, sub_folder)
                    self.create_albums_from_folder(path, original_path, replace_path, True, dry_run,
                                                   skip=skip,
                                                   skip_existing=skip_existing)
        else:
            print(f"Processing folder: {path}\n")
            self.create_album_from_folder(path, original_path, replace_path, dry_run, skip_existing=skip_existing)


def set_default(ctx, param, value):
    config_file = os.path.expanduser(value)

    if os.path.exists(config_file):
        print("Loading config from: " + config_file)
        with open(config_file, 'r') as f:
            config = load(f.read(), Loader=Loader)
        ctx.default_map = config
    return value


@click.command()
@click.option('--config',
              default='~/.config/immich-albums/config.yml',
              type=click.Path(),
              callback=set_default,
              is_eager=True,
              expose_value=False)
@click.option('--api-key', help='Immich API key', required=True)
@click.option('--api-host', help='Immich API Host', required=True)
@click.option("--original-path", help="Original path on local host", required=True)
@click.option("--replace-path", help="Path as seen from immich host", required=True)
@click.option("-r", "--recursive", help="Recursive", is_flag=True)
@click.option("--dry-run", help="Dry run", is_flag=True)
@click.option("--skip", help="Folders to skip", multiple=True, default=[])
@click.option("--skip-existing", help="Skip existing albums", required=False, is_flag=True)
@click.argument('path', type=click.Path(exists=True), required=True)
def cli(api_key, api_host, path, original_path, replace_path, recursive,
        dry_run, skip, skip_existing):
    immich_albums = ImmichAlbums(api_host, api_key)
    abs_path = os.path.abspath(path)
    immich_albums.create_albums_from_folder(
        path=abs_path,
        original_path=original_path,
        replace_path=replace_path,
        recursive=recursive,
        dry_run=dry_run,
        skip=skip,
        skip_existing=skip_existing
    )


# main block
if __name__ == '__main__':
    cli()
