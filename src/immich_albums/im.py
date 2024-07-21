from typing import Optional

import os
import click
import openapi_client
from openapi_client import ApiException, AlbumResponseDto, MetadataSearchDto

from yaml import load
import logging
import os 
from dataclasses import dataclass

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

log_level = logging.INFO 
if os.getenv('DEBUG'):
    log_level = logging.DEBUG 

logging.basicConfig(level=log_level)

logger = logging.getLogger("im-albums")

formatter_all = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
fh_debug = logging.FileHandler('immich-albums.all.log')
fh_debug.setLevel(logging.DEBUG)
fh_debug.setFormatter(formatter_all)
fh_info = logging.FileHandler('immich-albums.info.log')
fh_info.setLevel(logging.INFO)
fh_info.setFormatter(formatter_all)
logger.addHandler(fh_debug)
logger.addHandler(fh_info)

def write_album_id(path, id):
    with open(os.path.join(path, ".album"), "w") as f:
        f.write(id)


def read_album_id(path) -> Optional[str]:
    try:
        with open(os.path.join(path, ".album"), "r") as f:
            return f.read()
    except FileNotFoundError:
        return None

@dataclass
class ProcessingResults:
    added_files: int
    missing_files: int 
    album_name: str 

class ImmichAlbums:
    def __init__(self, api_host, api_key):
        api_configuration = openapi_client.Configuration(
            host=api_host,
        )

        api_configuration.api_key["api_key"] = api_key

        self.api_configuration = api_configuration

    def get_asset_by_original_path(self, original_path) -> Optional[int]:
        with openapi_client.ApiClient(self.api_configuration) as api_client:
            # Create an instance of the API class
            api_instance = openapi_client.SearchApi(api_client)

            dto = MetadataSearchDto(original_path=original_path)
            assets = api_instance.search_metadata(dto).to_dict()["assets"]["items"]
            return assets[0]["id"] if len(assets) > 0 else None

    def create_album(self, album_name, assets_ids) -> str:
        with openapi_client.ApiClient(self.api_configuration) as api_client:
            # Create an instance of the API class
            api_instance = openapi_client.AlbumApi(api_client)

        try:
            logger.debug(f"Creating album {album_name}")

            create_album_request = openapi_client.CreateAlbumDto(
                album_name=album_name,
                asset_ids=assets_ids,
            )

            api_response: AlbumResponseDto = api_instance.create_album(
                create_album_request
            )

            logger.debug(f"Album id {api_response.id}")
            logger.debug("The response of create album:")
            logger.debug(api_response)

            return api_response.id
        except ApiException as e:
            logger.exception(f"Exception when calling create_album")

    def add_picture_to_album(self, album_id, asset_ids):
        with openapi_client.ApiClient(self.api_configuration) as api_client:
            # Create an instance of the API class
            api_instance = openapi_client.AlbumApi(api_client)

            try:
                logger.debug(f"Adding assets to album {album_id}\n")
                bulkIdsDto = openapi_client.BulkIdsDto(ids=asset_ids)
                api_response = api_instance.add_assets_to_album(album_id, bulkIdsDto)
                logger.debug("The response of add asset to album:\n")
                logger.debug(api_response)
            except ApiException as e:
                logger.exception(f"Exception when calling add_assets_to_album")

    def get_assets_in_folder(self, folder: str, original_path: str, replace_path: str):
        assets_ids = []
        missing_files = []

        for filename in os.listdir(folder):
            full_path = os.path.join(folder, filename)
            if os.path.isfile(full_path):
                replaced_path = full_path.replace(original_path, replace_path)
                logger.debug(f"searching for: {replaced_path}")
                asset_id = self.get_asset_by_original_path(replaced_path)
                if asset_id is None:
                    logger.info(f"File {replaced_path} is missing !")
                    missing_files.append(replace_path)
                else:
                    assets_ids.append(asset_id)
                    logger.debug(f"File {replaced_path} is {asset_id}")

        return ([str(asset_id) for asset_id in assets_ids], missing_files)

    def create_album_from_folder(
        self,
        path: str,
        original_path: str,
        replace_path: str,
        dry_run: bool = False,
        skip_existing: bool = False,
    ) -> ProcessingResults:
        album = os.path.basename(path)

        album_id = read_album_id(path)
        if album_id:
            logger.debug(f"Album {album} exists with id {album_id}")

            if skip_existing:
                logger.info(f"Skipping existing album {album}")
                return ProcessingResults(0,0, album)
        else:
            logger.debug(f"Album {album} does not exist")

        (assets_ids, missng_files) = self.get_assets_in_folder(path, original_path, replace_path)

        if not dry_run:
            if album_id:
                logger.debug(f"Adding assets to album {album_id}")
                self.add_picture_to_album(album_id, assets_ids)
            else:
                album_id = self.create_album(album, assets_ids)
                logger.debug(f"Creating file .album for album {album}")
                write_album_id(path, album_id)
        else:
            logger.debug(f"DRY RUN: Creating album {album} with assets {assets_ids} ")
            # logger.info(f"DRY RUN: Assets ids: {assets_ids}")

        return ProcessingResults(len(assets_ids), len(missng_files) , album)

    def create_albums_from_folder(
        self,
        path: str,
        original_path: str,
        replace_path: str,
        recursive: bool = False,
        dry_run: bool = False,
        skip=None,
        skip_existing: bool = False,
    ):

        if skip is None:
            skip = []

        if recursive:
            for folder_name, sub_folders, filenames in os.walk(path):
                if folder_name in skip:
                    logger.info(f"Skipping folder: {folder_name}")
                    continue
                logger.info(f"Processing folder: {folder_name}")
                pres = self.create_album_from_folder(
                    path,
                    original_path,
                    replace_path,
                    dry_run,
                    skip_existing=skip_existing,
                )
                logger.info(f"Created album {pres.album_name} with {pres.added_files} files ")

                for sub_folder in sub_folders:
                    path = os.path.join(folder_name, sub_folder)
                    self.create_albums_from_folder(
                        path,
                        original_path,
                        replace_path,
                        True,
                        dry_run,
                        skip=skip,
                        skip_existing=skip_existing,
                    )
                break  # Avoid walking over sub folders of path which are visited by the for loop.
        else:
            logger.info(f"Processing folder: {path}\n")
            self.create_album_from_folder(
                path, original_path, replace_path, dry_run, skip_existing=skip_existing
            )


def set_default(ctx, param, value):
    config_file = os.path.expanduser(value)

    if os.path.exists(config_file):
        logger.info("Loading config from: " + config_file)
        with open(config_file, "r") as f:
            config = load(f.read(), Loader=Loader)
        ctx.default_map = config
    return value


@click.command()
@click.option(
    "--config",
    default="~/.config/immich-albums/config.yml",
    type=click.Path(),
    callback=set_default,
    is_eager=True,
    expose_value=False,
)
@click.option("--api-key", help="Immich API key", required=True)
@click.option(
    "--api-host",
    help="Immich API Host endpoint. Ex https://localhost:22283/api",
    required=True,
)
@click.option("--original-path", help="Original path on local host", required=True)
@click.option("--replace-path", help="Path as seen from immich host", required=True)
@click.option("-r", "--recursive", help="Recursive", is_flag=True)
@click.option("--dry-run", help="Dry run", is_flag=True)
@click.option("--skip", help="Folders to skip", multiple=True, default=[])
@click.option(
    "--skip-existing", help="Skip existing albums", required=False, is_flag=True
)
@click.argument("path", type=click.Path(exists=True), required=True)
def cli(
    api_key,
    api_host,
    path,
    original_path,
    replace_path,
    recursive,
    dry_run,
    skip,
    skip_existing,
):
    immich_albums = ImmichAlbums(api_host, api_key)
    abs_path = os.path.abspath(path)
    immich_albums.create_albums_from_folder(
        path=abs_path,
        original_path=original_path,
        replace_path=replace_path,
        recursive=recursive,
        dry_run=dry_run,
        skip=skip,
        skip_existing=skip_existing,
    )


# main block
if __name__ == "__main__":
    cli()
