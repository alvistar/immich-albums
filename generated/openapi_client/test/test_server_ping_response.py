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

from openapi_client.models.server_ping_response import ServerPingResponse  # noqa: E501

class TestServerPingResponse(unittest.TestCase):
    """ServerPingResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServerPingResponse:
        """Test ServerPingResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServerPingResponse`
        """
        model = ServerPingResponse()  # noqa: E501
        if include_optional:
            return ServerPingResponse(
                res = 'pong'
            )
        else:
            return ServerPingResponse(
                res = 'pong',
        )
        """

    def testServerPingResponse(self):
        """Test ServerPingResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
