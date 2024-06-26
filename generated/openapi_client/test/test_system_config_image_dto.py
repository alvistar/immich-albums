# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.105.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.system_config_image_dto import SystemConfigImageDto

class TestSystemConfigImageDto(unittest.TestCase):
    """SystemConfigImageDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemConfigImageDto:
        """Test SystemConfigImageDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemConfigImageDto`
        """
        model = SystemConfigImageDto()
        if include_optional:
            return SystemConfigImageDto(
                colorspace = 'srgb',
                extract_embedded = True,
                preview_format = 'jpeg',
                preview_size = 1,
                quality = 1,
                thumbnail_format = 'jpeg',
                thumbnail_size = 1
            )
        else:
            return SystemConfigImageDto(
                colorspace = 'srgb',
                extract_embedded = True,
                preview_format = 'jpeg',
                preview_size = 1,
                quality = 1,
                thumbnail_format = 'jpeg',
                thumbnail_size = 1,
        )
        """

    def testSystemConfigImageDto(self):
        """Test SystemConfigImageDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
