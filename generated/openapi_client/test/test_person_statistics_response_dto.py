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

from openapi_client.models.person_statistics_response_dto import PersonStatisticsResponseDto

class TestPersonStatisticsResponseDto(unittest.TestCase):
    """PersonStatisticsResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonStatisticsResponseDto:
        """Test PersonStatisticsResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonStatisticsResponseDto`
        """
        model = PersonStatisticsResponseDto()
        if include_optional:
            return PersonStatisticsResponseDto(
                assets = 56
            )
        else:
            return PersonStatisticsResponseDto(
                assets = 56,
        )
        """

    def testPersonStatisticsResponseDto(self):
        """Test PersonStatisticsResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
