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

from openapi_client.models.tag_response_dto import TagResponseDto

class TestTagResponseDto(unittest.TestCase):
    """TagResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TagResponseDto:
        """Test TagResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TagResponseDto`
        """
        model = TagResponseDto()
        if include_optional:
            return TagResponseDto(
                id = '',
                name = '',
                type = 'OBJECT',
                user_id = ''
            )
        else:
            return TagResponseDto(
                id = '',
                name = '',
                type = 'OBJECT',
                user_id = '',
        )
        """

    def testTagResponseDto(self):
        """Test TagResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
