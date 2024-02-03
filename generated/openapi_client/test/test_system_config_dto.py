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

from openapi_client.models.system_config_dto import SystemConfigDto

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
        model = SystemConfigDto()
        if include_optional:
            return SystemConfigDto(
                ffmpeg = openapi_client.models.system_config_f_fmpeg_dto.SystemConfigFFmpegDto(
                    accel = 'nvenc', 
                    accepted_audio_codecs = [
                        'mp3'
                        ], 
                    accepted_video_codecs = [
                        'h264'
                        ], 
                    bframes = 56, 
                    cq_mode = 'auto', 
                    crf = 56, 
                    gop_size = 56, 
                    max_bitrate = '', 
                    npl = 56, 
                    preferred_hw_device = '', 
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
                    face_detection = openapi_client.models.job_settings_dto.JobSettingsDto(
                        concurrency = 56, ), 
                    library = , 
                    metadata_extraction = , 
                    migration = , 
                    search = , 
                    sidecar = , 
                    smart_search = , 
                    thumbnail_generation = , 
                    video_conversion = , ),
                library = openapi_client.models.system_config_library_dto.SystemConfigLibraryDto(
                    scan = openapi_client.models.system_config_library_scan_dto.SystemConfigLibraryScanDto(
                        cron_expression = '', 
                        enabled = True, ), 
                    watch = openapi_client.models.system_config_library_watch_dto.SystemConfigLibraryWatchDto(
                        enabled = True, 
                        interval = 56, 
                        use_polling = True, ), ),
                logging = openapi_client.models.system_config_logging_dto.SystemConfigLoggingDto(
                    enabled = True, 
                    level = 'verbose', ),
                machine_learning = openapi_client.models.system_config_machine_learning_dto.SystemConfigMachineLearningDto(
                    clip = openapi_client.models.clip_config.CLIPConfig(
                        enabled = True, 
                        mode = 'vision', 
                        model_name = '', 
                        model_type = 'facial-recognition', ), 
                    enabled = True, 
                    facial_recognition = openapi_client.models.recognition_config.RecognitionConfig(
                        enabled = True, 
                        max_distance = 1.337, 
                        min_faces = 56, 
                        min_score = 1.337, 
                        model_name = '', ), 
                    url = '', ),
                map = openapi_client.models.system_config_map_dto.SystemConfigMapDto(
                    dark_style = '', 
                    enabled = True, 
                    light_style = '', ),
                new_version_check = openapi_client.models.system_config_new_version_check_dto.SystemConfigNewVersionCheckDto(
                    enabled = True, ),
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
                    signing_algorithm = '', 
                    storage_label_claim = '', ),
                password_login = openapi_client.models.system_config_password_login_dto.SystemConfigPasswordLoginDto(
                    enabled = True, ),
                reverse_geocoding = openapi_client.models.system_config_reverse_geocoding_dto.SystemConfigReverseGeocodingDto(
                    enabled = True, ),
                server = openapi_client.models.system_config_server_dto.SystemConfigServerDto(
                    external_domain = '', 
                    login_page_message = '', ),
                storage_template = openapi_client.models.system_config_storage_template_dto.SystemConfigStorageTemplateDto(
                    enabled = True, 
                    hash_verification_enabled = True, 
                    template = '', ),
                theme = openapi_client.models.system_config_theme_dto.SystemConfigThemeDto(
                    custom_css = '', ),
                thumbnail = openapi_client.models.system_config_thumbnail_dto.SystemConfigThumbnailDto(
                    colorspace = 'srgb', 
                    jpeg_size = 56, 
                    quality = 56, 
                    webp_size = 56, ),
                trash = openapi_client.models.system_config_trash_dto.SystemConfigTrashDto(
                    days = 56, 
                    enabled = True, )
            )
        else:
            return SystemConfigDto(
                ffmpeg = openapi_client.models.system_config_f_fmpeg_dto.SystemConfigFFmpegDto(
                    accel = 'nvenc', 
                    accepted_audio_codecs = [
                        'mp3'
                        ], 
                    accepted_video_codecs = [
                        'h264'
                        ], 
                    bframes = 56, 
                    cq_mode = 'auto', 
                    crf = 56, 
                    gop_size = 56, 
                    max_bitrate = '', 
                    npl = 56, 
                    preferred_hw_device = '', 
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
                    face_detection = openapi_client.models.job_settings_dto.JobSettingsDto(
                        concurrency = 56, ), 
                    library = , 
                    metadata_extraction = , 
                    migration = , 
                    search = , 
                    sidecar = , 
                    smart_search = , 
                    thumbnail_generation = , 
                    video_conversion = , ),
                library = openapi_client.models.system_config_library_dto.SystemConfigLibraryDto(
                    scan = openapi_client.models.system_config_library_scan_dto.SystemConfigLibraryScanDto(
                        cron_expression = '', 
                        enabled = True, ), 
                    watch = openapi_client.models.system_config_library_watch_dto.SystemConfigLibraryWatchDto(
                        enabled = True, 
                        interval = 56, 
                        use_polling = True, ), ),
                logging = openapi_client.models.system_config_logging_dto.SystemConfigLoggingDto(
                    enabled = True, 
                    level = 'verbose', ),
                machine_learning = openapi_client.models.system_config_machine_learning_dto.SystemConfigMachineLearningDto(
                    clip = openapi_client.models.clip_config.CLIPConfig(
                        enabled = True, 
                        mode = 'vision', 
                        model_name = '', 
                        model_type = 'facial-recognition', ), 
                    enabled = True, 
                    facial_recognition = openapi_client.models.recognition_config.RecognitionConfig(
                        enabled = True, 
                        max_distance = 1.337, 
                        min_faces = 56, 
                        min_score = 1.337, 
                        model_name = '', ), 
                    url = '', ),
                map = openapi_client.models.system_config_map_dto.SystemConfigMapDto(
                    dark_style = '', 
                    enabled = True, 
                    light_style = '', ),
                new_version_check = openapi_client.models.system_config_new_version_check_dto.SystemConfigNewVersionCheckDto(
                    enabled = True, ),
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
                    signing_algorithm = '', 
                    storage_label_claim = '', ),
                password_login = openapi_client.models.system_config_password_login_dto.SystemConfigPasswordLoginDto(
                    enabled = True, ),
                reverse_geocoding = openapi_client.models.system_config_reverse_geocoding_dto.SystemConfigReverseGeocodingDto(
                    enabled = True, ),
                server = openapi_client.models.system_config_server_dto.SystemConfigServerDto(
                    external_domain = '', 
                    login_page_message = '', ),
                storage_template = openapi_client.models.system_config_storage_template_dto.SystemConfigStorageTemplateDto(
                    enabled = True, 
                    hash_verification_enabled = True, 
                    template = '', ),
                theme = openapi_client.models.system_config_theme_dto.SystemConfigThemeDto(
                    custom_css = '', ),
                thumbnail = openapi_client.models.system_config_thumbnail_dto.SystemConfigThumbnailDto(
                    colorspace = 'srgb', 
                    jpeg_size = 56, 
                    quality = 56, 
                    webp_size = 56, ),
                trash = openapi_client.models.system_config_trash_dto.SystemConfigTrashDto(
                    days = 56, 
                    enabled = True, ),
        )
        """

    def testSystemConfigDto(self):
        """Test SystemConfigDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
