# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.94.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.o_auth_api import OAuthApi


class TestOAuthApi(unittest.TestCase):
    """OAuthApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OAuthApi()

    def tearDown(self) -> None:
        pass

    def test_finish_o_auth(self) -> None:
        """Test case for finish_o_auth

        """
        pass

    def test_generate_o_auth_config(self) -> None:
        """Test case for generate_o_auth_config

        """
        pass

    def test_link_o_auth_account(self) -> None:
        """Test case for link_o_auth_account

        """
        pass

    def test_redirect_o_auth_to_mobile(self) -> None:
        """Test case for redirect_o_auth_to_mobile

        """
        pass

    def test_start_o_auth(self) -> None:
        """Test case for start_o_auth

        """
        pass

    def test_unlink_o_auth_account(self) -> None:
        """Test case for unlink_o_auth_account

        """
        pass


if __name__ == '__main__':
    unittest.main()
