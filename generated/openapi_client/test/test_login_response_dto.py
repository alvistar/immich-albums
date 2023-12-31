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

from openapi_client.models.login_response_dto import LoginResponseDto  # noqa: E501

class TestLoginResponseDto(unittest.TestCase):
    """LoginResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoginResponseDto:
        """Test LoginResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoginResponseDto`
        """
        model = LoginResponseDto()  # noqa: E501
        if include_optional:
            return LoginResponseDto(
                access_token = '',
                first_name = '',
                is_admin = True,
                last_name = '',
                profile_image_path = '',
                should_change_password = True,
                user_email = '',
                user_id = ''
            )
        else:
            return LoginResponseDto(
                access_token = '',
                first_name = '',
                is_admin = True,
                last_name = '',
                profile_image_path = '',
                should_change_password = True,
                user_email = '',
                user_id = '',
        )
        """

    def testLoginResponseDto(self):
        """Test LoginResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
