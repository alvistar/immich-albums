# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.105.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.on_this_day_dto import OnThisDayDto

class TestOnThisDayDto(unittest.TestCase):
    """OnThisDayDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OnThisDayDto:
        """Test OnThisDayDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OnThisDayDto`
        """
        model = OnThisDayDto()
        if include_optional:
            return OnThisDayDto(
                year = 1
            )
        else:
            return OnThisDayDto(
                year = 1,
        )
        """

    def testOnThisDayDto(self):
        """Test OnThisDayDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
