# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.105.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.metadata_search_dto import MetadataSearchDto

class TestMetadataSearchDto(unittest.TestCase):
    """MetadataSearchDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetadataSearchDto:
        """Test MetadataSearchDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetadataSearchDto`
        """
        model = MetadataSearchDto()
        if include_optional:
            return MetadataSearchDto(
                checksum = '',
                city = '',
                country = '',
                created_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                device_asset_id = '',
                device_id = '',
                encoded_video_path = '',
                id = '',
                is_archived = True,
                is_encoded = True,
                is_favorite = True,
                is_motion = True,
                is_not_in_album = True,
                is_offline = True,
                is_visible = True,
                lens_model = '',
                library_id = '',
                make = '',
                model = '',
                order = 'asc',
                original_file_name = '',
                original_path = '',
                page = 1,
                person_ids = [
                    ''
                    ],
                preview_path = '',
                resize_path = '',
                size = 1,
                state = '',
                taken_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                taken_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                thumbnail_path = '',
                trashed_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                trashed_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                type = 'IMAGE',
                updated_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                webp_path = '',
                with_archived = True,
                with_deleted = True,
                with_exif = True,
                with_people = True,
                with_stacked = True
            )
        else:
            return MetadataSearchDto(
        )
        """

    def testMetadataSearchDto(self):
        """Test MetadataSearchDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
