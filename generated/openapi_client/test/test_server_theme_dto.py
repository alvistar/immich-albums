# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.94.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.server_theme_dto import ServerThemeDto

class TestServerThemeDto(unittest.TestCase):
    """ServerThemeDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServerThemeDto:
        """Test ServerThemeDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServerThemeDto`
        """
        model = ServerThemeDto()
        if include_optional:
            return ServerThemeDto(
                custom_css = ''
            )
        else:
            return ServerThemeDto(
                custom_css = '',
        )
        """

    def testServerThemeDto(self):
        """Test ServerThemeDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
