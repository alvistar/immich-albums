# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.88.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field
from openapi_client.models.job_settings_dto import JobSettingsDto

class SystemConfigJobDto(BaseModel):
    """
    SystemConfigJobDto
    """
    background_task: JobSettingsDto = Field(..., alias="backgroundTask")
    clip_encoding: JobSettingsDto = Field(..., alias="clipEncoding")
    library: JobSettingsDto = Field(...)
    metadata_extraction: JobSettingsDto = Field(..., alias="metadataExtraction")
    migration: JobSettingsDto = Field(...)
    object_tagging: JobSettingsDto = Field(..., alias="objectTagging")
    recognize_faces: JobSettingsDto = Field(..., alias="recognizeFaces")
    search: JobSettingsDto = Field(...)
    sidecar: JobSettingsDto = Field(...)
    storage_template_migration: JobSettingsDto = Field(..., alias="storageTemplateMigration")
    thumbnail_generation: JobSettingsDto = Field(..., alias="thumbnailGeneration")
    video_conversion: JobSettingsDto = Field(..., alias="videoConversion")
    __properties = ["backgroundTask", "clipEncoding", "library", "metadataExtraction", "migration", "objectTagging", "recognizeFaces", "search", "sidecar", "storageTemplateMigration", "thumbnailGeneration", "videoConversion"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SystemConfigJobDto:
        """Create an instance of SystemConfigJobDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of background_task
        if self.background_task:
            _dict['backgroundTask'] = self.background_task.to_dict()
        # override the default output from pydantic by calling `to_dict()` of clip_encoding
        if self.clip_encoding:
            _dict['clipEncoding'] = self.clip_encoding.to_dict()
        # override the default output from pydantic by calling `to_dict()` of library
        if self.library:
            _dict['library'] = self.library.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata_extraction
        if self.metadata_extraction:
            _dict['metadataExtraction'] = self.metadata_extraction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of migration
        if self.migration:
            _dict['migration'] = self.migration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of object_tagging
        if self.object_tagging:
            _dict['objectTagging'] = self.object_tagging.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recognize_faces
        if self.recognize_faces:
            _dict['recognizeFaces'] = self.recognize_faces.to_dict()
        # override the default output from pydantic by calling `to_dict()` of search
        if self.search:
            _dict['search'] = self.search.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sidecar
        if self.sidecar:
            _dict['sidecar'] = self.sidecar.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage_template_migration
        if self.storage_template_migration:
            _dict['storageTemplateMigration'] = self.storage_template_migration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of thumbnail_generation
        if self.thumbnail_generation:
            _dict['thumbnailGeneration'] = self.thumbnail_generation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of video_conversion
        if self.video_conversion:
            _dict['videoConversion'] = self.video_conversion.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SystemConfigJobDto:
        """Create an instance of SystemConfigJobDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SystemConfigJobDto.parse_obj(obj)

        _obj = SystemConfigJobDto.parse_obj({
            "background_task": JobSettingsDto.from_dict(obj.get("backgroundTask")) if obj.get("backgroundTask") is not None else None,
            "clip_encoding": JobSettingsDto.from_dict(obj.get("clipEncoding")) if obj.get("clipEncoding") is not None else None,
            "library": JobSettingsDto.from_dict(obj.get("library")) if obj.get("library") is not None else None,
            "metadata_extraction": JobSettingsDto.from_dict(obj.get("metadataExtraction")) if obj.get("metadataExtraction") is not None else None,
            "migration": JobSettingsDto.from_dict(obj.get("migration")) if obj.get("migration") is not None else None,
            "object_tagging": JobSettingsDto.from_dict(obj.get("objectTagging")) if obj.get("objectTagging") is not None else None,
            "recognize_faces": JobSettingsDto.from_dict(obj.get("recognizeFaces")) if obj.get("recognizeFaces") is not None else None,
            "search": JobSettingsDto.from_dict(obj.get("search")) if obj.get("search") is not None else None,
            "sidecar": JobSettingsDto.from_dict(obj.get("sidecar")) if obj.get("sidecar") is not None else None,
            "storage_template_migration": JobSettingsDto.from_dict(obj.get("storageTemplateMigration")) if obj.get("storageTemplateMigration") is not None else None,
            "thumbnail_generation": JobSettingsDto.from_dict(obj.get("thumbnailGeneration")) if obj.get("thumbnailGeneration") is not None else None,
            "video_conversion": JobSettingsDto.from_dict(obj.get("videoConversion")) if obj.get("videoConversion") is not None else None
        })
        return _obj


