# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.88.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.partner_response_dto import PartnerResponseDto  # noqa: E501

class TestPartnerResponseDto(unittest.TestCase):
    """PartnerResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PartnerResponseDto:
        """Test PartnerResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PartnerResponseDto`
        """
        model = PartnerResponseDto()  # noqa: E501
        if include_optional:
            return PartnerResponseDto(
                avatar_color = 'primary',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                email = '',
                external_path = '',
                id = '',
                in_timeline = True,
                is_admin = True,
                memories_enabled = True,
                name = '',
                oauth_id = '',
                profile_image_path = '',
                should_change_password = True,
                storage_label = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return PartnerResponseDto(
                avatar_color = 'primary',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                email = '',
                external_path = '',
                id = '',
                is_admin = True,
                name = '',
                oauth_id = '',
                profile_image_path = '',
                should_change_password = True,
                storage_label = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testPartnerResponseDto(self):
        """Test PartnerResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
