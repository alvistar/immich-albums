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

from openapi_client.models.recognition_config import RecognitionConfig

class TestRecognitionConfig(unittest.TestCase):
    """RecognitionConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecognitionConfig:
        """Test RecognitionConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecognitionConfig`
        """
        model = RecognitionConfig()
        if include_optional:
            return RecognitionConfig(
                enabled = True,
                max_distance = 1.337,
                min_faces = 56,
                min_score = 1.337,
                model_name = '',
                model_type = 'facial-recognition'
            )
        else:
            return RecognitionConfig(
                enabled = True,
                max_distance = 1.337,
                min_faces = 56,
                min_score = 1.337,
                model_name = '',
        )
        """

    def testRecognitionConfig(self):
        """Test RecognitionConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
