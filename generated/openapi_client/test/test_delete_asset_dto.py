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

from openapi_client.models.delete_asset_dto import DeleteAssetDto  # noqa: E501

class TestDeleteAssetDto(unittest.TestCase):
    """DeleteAssetDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteAssetDto:
        """Test DeleteAssetDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteAssetDto`
        """
        model = DeleteAssetDto()  # noqa: E501
        if include_optional:
            return DeleteAssetDto(
                ids = ["bf973405-3f2a-48d2-a687-2ed4167164be","dd41870b-5d00-46d2-924e-1d8489a0aa0f","fad77c3f-deef-4e7e-9608-14c1aa4e559a"]
            )
        else:
            return DeleteAssetDto(
                ids = ["bf973405-3f2a-48d2-a687-2ed4167164be","dd41870b-5d00-46d2-924e-1d8489a0aa0f","fad77c3f-deef-4e7e-9608-14c1aa4e559a"],
        )
        """

    def testDeleteAssetDto(self):
        """Test DeleteAssetDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
