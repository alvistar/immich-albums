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

from openapi_client.models.system_config_dto import SystemConfigDto  # noqa: E501

class TestSystemConfigDto(unittest.TestCase):
    """SystemConfigDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemConfigDto:
        """Test SystemConfigDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemConfigDto`
        """
        model = SystemConfigDto()  # noqa: E501
        if include_optional:
            return SystemConfigDto(
                ffmpeg = openapi_client.models.system_config_f_fmpeg_dto.SystemConfigFFmpegDto(
                    accel = 'nvenc', 
                    bframes = 56, 
                    cq_mode = 'auto', 
                    crf = 56, 
                    gop_size = 56, 
                    max_bitrate = '', 
                    npl = 56, 
                    preset = '', 
                    refs = 56, 
                    target_audio_codec = 'mp3', 
                    target_resolution = '', 
                    target_video_codec = 'h264', 
                    temporal_aq = True, 
                    threads = 56, 
                    tonemap = 'hable', 
                    transcode = 'all', 
                    two_pass = True, ),
                job = openapi_client.models.system_config_job_dto.SystemConfigJobDto(
                    background_task = openapi_client.models.job_settings_dto.JobSettingsDto(
                        concurrency = 56, ), 
                    clip_encoding = openapi_client.models.job_settings_dto.JobSettingsDto(
                        concurrency = 56, ), 
                    library = , 
                    metadata_extraction = , 
                    object_tagging = , 
                    recognize_faces = , 
                    search = , 
                    sidecar = , 
                    storage_template_migration = , 
                    thumbnail_generation = , 
                    video_conversion = , ),
                machine_learning = openapi_client.models.system_config_machine_learning_dto.SystemConfigMachineLearningDto(
                    classification = openapi_client.models.classification_config.ClassificationConfig(
                        enabled = True, 
                        min_score = 56, 
                        model_name = '', 
                        model_type = 'image-classification', ), 
                    clip = openapi_client.models.clip_config.CLIPConfig(
                        enabled = True, 
                        mode = 'vision', 
                        model_name = '', ), 
                    enabled = True, 
                    facial_recognition = openapi_client.models.recognition_config.RecognitionConfig(
                        enabled = True, 
                        max_distance = 56, 
                        min_faces = 56, 
                        min_score = 56, 
                        model_name = '', ), 
                    url = '', ),
                map = openapi_client.models.system_config_map_dto.SystemConfigMapDto(
                    enabled = True, 
                    tile_url = '', ),
                oauth = openapi_client.models.system_config_o_auth_dto.SystemConfigOAuthDto(
                    auto_launch = True, 
                    auto_register = True, 
                    button_text = '', 
                    client_id = '', 
                    client_secret = '', 
                    enabled = True, 
                    issuer_url = '', 
                    mobile_override_enabled = True, 
                    mobile_redirect_uri = '', 
                    scope = '', 
                    storage_label_claim = '', ),
                password_login = openapi_client.models.system_config_password_login_dto.SystemConfigPasswordLoginDto(
                    enabled = True, ),
                storage_template = openapi_client.models.system_config_storage_template_dto.SystemConfigStorageTemplateDto(
                    template = '', ),
                thumbnail = openapi_client.models.system_config_thumbnail_dto.SystemConfigThumbnailDto(
                    colorspace = 'srgb', 
                    jpeg_size = 56, 
                    quality = 56, 
                    webp_size = 56, )
            )
        else:
            return SystemConfigDto(
                ffmpeg = openapi_client.models.system_config_f_fmpeg_dto.SystemConfigFFmpegDto(
                    accel = 'nvenc', 
                    bframes = 56, 
                    cq_mode = 'auto', 
                    crf = 56, 
                    gop_size = 56, 
                    max_bitrate = '', 
                    npl = 56, 
                    preset = '', 
                    refs = 56, 
                    target_audio_codec = 'mp3', 
                    target_resolution = '', 
                    target_video_codec = 'h264', 
                    temporal_aq = True, 
                    threads = 56, 
                    tonemap = 'hable', 
                    transcode = 'all', 
                    two_pass = True, ),
                job = openapi_client.models.system_config_job_dto.SystemConfigJobDto(
                    background_task = openapi_client.models.job_settings_dto.JobSettingsDto(
                        concurrency = 56, ), 
                    clip_encoding = openapi_client.models.job_settings_dto.JobSettingsDto(
                        concurrency = 56, ), 
                    library = , 
                    metadata_extraction = , 
                    object_tagging = , 
                    recognize_faces = , 
                    search = , 
                    sidecar = , 
                    storage_template_migration = , 
                    thumbnail_generation = , 
                    video_conversion = , ),
                machine_learning = openapi_client.models.system_config_machine_learning_dto.SystemConfigMachineLearningDto(
                    classification = openapi_client.models.classification_config.ClassificationConfig(
                        enabled = True, 
                        min_score = 56, 
                        model_name = '', 
                        model_type = 'image-classification', ), 
                    clip = openapi_client.models.clip_config.CLIPConfig(
                        enabled = True, 
                        mode = 'vision', 
                        model_name = '', ), 
                    enabled = True, 
                    facial_recognition = openapi_client.models.recognition_config.RecognitionConfig(
                        enabled = True, 
                        max_distance = 56, 
                        min_faces = 56, 
                        min_score = 56, 
                        model_name = '', ), 
                    url = '', ),
                map = openapi_client.models.system_config_map_dto.SystemConfigMapDto(
                    enabled = True, 
                    tile_url = '', ),
                oauth = openapi_client.models.system_config_o_auth_dto.SystemConfigOAuthDto(
                    auto_launch = True, 
                    auto_register = True, 
                    button_text = '', 
                    client_id = '', 
                    client_secret = '', 
                    enabled = True, 
                    issuer_url = '', 
                    mobile_override_enabled = True, 
                    mobile_redirect_uri = '', 
                    scope = '', 
                    storage_label_claim = '', ),
                password_login = openapi_client.models.system_config_password_login_dto.SystemConfigPasswordLoginDto(
                    enabled = True, ),
                storage_template = openapi_client.models.system_config_storage_template_dto.SystemConfigStorageTemplateDto(
                    template = '', ),
                thumbnail = openapi_client.models.system_config_thumbnail_dto.SystemConfigThumbnailDto(
                    colorspace = 'srgb', 
                    jpeg_size = 56, 
                    quality = 56, 
                    webp_size = 56, ),
        )
        """

    def testSystemConfigDto(self):
        """Test SystemConfigDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
