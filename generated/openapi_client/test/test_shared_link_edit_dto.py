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

from openapi_client.models.shared_link_edit_dto import SharedLinkEditDto

class TestSharedLinkEditDto(unittest.TestCase):
    """SharedLinkEditDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SharedLinkEditDto:
        """Test SharedLinkEditDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SharedLinkEditDto`
        """
        model = SharedLinkEditDto()
        if include_optional:
            return SharedLinkEditDto(
                allow_download = True,
                allow_upload = True,
                change_expiry_time = True,
                description = '',
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                password = '',
                show_metadata = True
            )
        else:
            return SharedLinkEditDto(
        )
        """

    def testSharedLinkEditDto(self):
        """Test SharedLinkEditDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
