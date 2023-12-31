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

from openapi_client.models.server_features_dto import ServerFeaturesDto  # noqa: E501

class TestServerFeaturesDto(unittest.TestCase):
    """ServerFeaturesDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServerFeaturesDto:
        """Test ServerFeaturesDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServerFeaturesDto`
        """
        model = ServerFeaturesDto()  # noqa: E501
        if include_optional:
            return ServerFeaturesDto(
                clip_encode = True,
                config_file = True,
                facial_recognition = True,
                map = True,
                oauth = True,
                oauth_auto_launch = True,
                password_login = True,
                search = True,
                sidecar = True,
                tag_image = True
            )
        else:
            return ServerFeaturesDto(
                clip_encode = True,
                config_file = True,
                facial_recognition = True,
                map = True,
                oauth = True,
                oauth_auto_launch = True,
                password_login = True,
                search = True,
                sidecar = True,
                tag_image = True,
        )
        """

    def testServerFeaturesDto(self):
        """Test ServerFeaturesDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
