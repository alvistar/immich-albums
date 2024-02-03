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

from openapi_client.models.people_update_item import PeopleUpdateItem

class TestPeopleUpdateItem(unittest.TestCase):
    """PeopleUpdateItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PeopleUpdateItem:
        """Test PeopleUpdateItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PeopleUpdateItem`
        """
        model = PeopleUpdateItem()
        if include_optional:
            return PeopleUpdateItem(
                birth_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                feature_face_asset_id = '',
                id = '',
                is_hidden = True,
                name = ''
            )
        else:
            return PeopleUpdateItem(
                id = '',
        )
        """

    def testPeopleUpdateItem(self):
        """Test PeopleUpdateItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
