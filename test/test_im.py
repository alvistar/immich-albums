import pathlib
from unittest import mock

import pytest

from immich_albums.im import ImmichAlbums


@pytest.fixture(name="albums_folders")
def create_albums_folders_fixture(tmp_path: pathlib.Path):
    tmp_path = tmp_path / "albums"
    p_dir_A = tmp_path / "A"
    p_dir_B = tmp_path / "B"
    folders = [
        tmp_path, p_dir_A, p_dir_A / "1", p_dir_A / "2", p_dir_B, p_dir_B / "3"
    ]

    for p in folders:
        p.mkdir()

    return [str(p) for p in folders]


def test_recursion_v2(albums_folders: list[pathlib.Path]):
    with mock.patch.object(ImmichAlbums,
                           "create_album_from_folder") as mock_method:
        immich_albums = ImmichAlbums(None, None)
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
