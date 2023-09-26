# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.79.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.library_api import LibraryApi  # noqa: E501


class TestLibraryApi(unittest.TestCase):
    """LibraryApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LibraryApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_library(self) -> None:
        """Test case for create_library

        """
        pass

    def test_delete_library(self) -> None:
        """Test case for delete_library

        """
        pass

    def test_get_all_for_user(self) -> None:
        """Test case for get_all_for_user

        """
        pass

    def test_get_library_info(self) -> None:
        """Test case for get_library_info

        """
        pass

    def test_get_library_statistics(self) -> None:
        """Test case for get_library_statistics

        """
        pass

    def test_remove_offline_files(self) -> None:
        """Test case for remove_offline_files

        """
        pass

    def test_scan_library(self) -> None:
        """Test case for scan_library

        """
        pass

    def test_update_library(self) -> None:
        """Test case for update_library

        """
        pass


if __name__ == '__main__':
    unittest.main()