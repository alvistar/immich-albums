import pathlib
from unittest import mock
from unittest.mock import patch

import pytest
from click.testing import CliRunner

from immich_albums.im import ImmichAlbums, cli

# Sample config content for testing
config_content = """
api_key: "test-api-key"
api_host: "https://localhost:22283/api"
original_path: "/path/to/original"
replace_path: "/path/to/replace"
recursive: true
dry_run: false
skip: ["/path/to/skip"]
skip_existing: true
"""


@pytest.fixture
def config_file(tmp_path):
    config_path = tmp_path / "config.yml"
    with open(config_path, "w") as f:
        f.write(config_content)
    return config_path


@pytest.fixture(name="albums_folders")
def create_albums_folders_fixture(tmp_path: pathlib.Path):
    tmp_path = tmp_path / "albums"
    p_dir_A = tmp_path / "A"
    p_dir_B = tmp_path / "B"
    folders = [tmp_path, p_dir_A, p_dir_A / "1", p_dir_A / "2", p_dir_B, p_dir_B / "3"]

    for p in folders:
        p.mkdir()

    return [str(p) for p in folders]


def test_recursion(albums_folders: list[pathlib.Path]):
    immich_albums = ImmichAlbums(None, None)
    with mock.patch.object(ImmichAlbums, "create_album_from_folder") as mock_method:
        immich_albums.create_albums_from_folder(
            path=str(albums_folders[0]),
            original_path="orignal_path",
            replace_path="replace_path",
            recursive=True,
        )

    assert mock_method.call_count == 6

    # ImmichAlbums should visit every folder exactly once, the order doesn't matter:
    visited_folders = [call[0][0] for call in mock_method.call_args_list]
    assert visited_folders == albums_folders


def test_file_config(config_file):
    with mock.patch("immich_albums.im.ImmichAlbums") as mock_class:
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "--config",
                str(config_file),
                "/",
            ],
        )
        # Check if the command executed successfully
        assert result.exit_code == 0

        # Check if the ImmichAlbums class was instantiated with the correct arguments
        mock_class.assert_called_once_with(
            "https://localhost:22283/api", "test-api-key"
        )

        # Check if the create_albums_from_folder method was called
        mock_class.return_value.create_albums_from_folder.assert_called_once_with(
            path="/",
            original_path="/path/to/original",
            replace_path="/path/to/replace",
            recursive=True,
            dry_run=False,
            skip=("/path/to/skip",),
            skip_existing=True,
        )
