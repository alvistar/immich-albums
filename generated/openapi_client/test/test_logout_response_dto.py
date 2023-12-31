# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.79.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.logout_response_dto import LogoutResponseDto  # noqa: E501

class TestLogoutResponseDto(unittest.TestCase):
    """LogoutResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LogoutResponseDto:
        """Test LogoutResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LogoutResponseDto`
        """
        model = LogoutResponseDto()  # noqa: E501
        if include_optional:
            return LogoutResponseDto(
                redirect_uri = '',
                successful = True
            )
        else:
            return LogoutResponseDto(
                redirect_uri = '',
                successful = True,
        )
        """

    def testLogoutResponseDto(self):
        """Test LogoutResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
