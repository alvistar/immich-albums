# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.105.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from openapi_client.models.job_status_dto import JobStatusDto
from typing import Optional, Set
from typing_extensions import Self

class AllJobStatusResponseDto(BaseModel):
    """
    AllJobStatusResponseDto
    """ # noqa: E501
    background_task: JobStatusDto = Field(alias="backgroundTask")
    face_detection: JobStatusDto = Field(alias="faceDetection")
    facial_recognition: JobStatusDto = Field(alias="facialRecognition")
    library: JobStatusDto
    metadata_extraction: JobStatusDto = Field(alias="metadataExtraction")
    migration: JobStatusDto
    notifications: JobStatusDto
    search: JobStatusDto
    sidecar: JobStatusDto
    smart_search: JobStatusDto = Field(alias="smartSearch")
    storage_template_migration: JobStatusDto = Field(alias="storageTemplateMigration")
    thumbnail_generation: JobStatusDto = Field(alias="thumbnailGeneration")
    video_conversion: JobStatusDto = Field(alias="videoConversion")
    __properties: ClassVar[List[str]] = ["backgroundTask", "faceDetection", "facialRecognition", "library", "metadataExtraction", "migration", "notifications", "search", "sidecar", "smartSearch", "storageTemplateMigration", "thumbnailGeneration", "videoConversion"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AllJobStatusResponseDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of background_task
        if self.background_task:
            _dict['backgroundTask'] = self.background_task.to_dict()
        # override the default output from pydantic by calling `to_dict()` of face_detection
        if self.face_detection:
            _dict['faceDetection'] = self.face_detection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of facial_recognition
        if self.facial_recognition:
            _dict['facialRecognition'] = self.facial_recognition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of library
        if self.library:
            _dict['library'] = self.library.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata_extraction
        if self.metadata_extraction:
            _dict['metadataExtraction'] = self.metadata_extraction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of migration
        if self.migration:
            _dict['migration'] = self.migration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notifications
        if self.notifications:
            _dict['notifications'] = self.notifications.to_dict()
        # override the default output from pydantic by calling `to_dict()` of search
        if self.search:
            _dict['search'] = self.search.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sidecar
        if self.sidecar:
            _dict['sidecar'] = self.sidecar.to_dict()
        # override the default output from pydantic by calling `to_dict()` of smart_search
        if self.smart_search:
            _dict['smartSearch'] = self.smart_search.to_dict()
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
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AllJobStatusResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "backgroundTask": JobStatusDto.from_dict(obj["backgroundTask"]) if obj.get("backgroundTask") is not None else None,
            "faceDetection": JobStatusDto.from_dict(obj["faceDetection"]) if obj.get("faceDetection") is not None else None,
            "facialRecognition": JobStatusDto.from_dict(obj["facialRecognition"]) if obj.get("facialRecognition") is not None else None,
            "library": JobStatusDto.from_dict(obj["library"]) if obj.get("library") is not None else None,
            "metadataExtraction": JobStatusDto.from_dict(obj["metadataExtraction"]) if obj.get("metadataExtraction") is not None else None,
            "migration": JobStatusDto.from_dict(obj["migration"]) if obj.get("migration") is not None else None,
            "notifications": JobStatusDto.from_dict(obj["notifications"]) if obj.get("notifications") is not None else None,
            "search": JobStatusDto.from_dict(obj["search"]) if obj.get("search") is not None else None,
            "sidecar": JobStatusDto.from_dict(obj["sidecar"]) if obj.get("sidecar") is not None else None,
            "smartSearch": JobStatusDto.from_dict(obj["smartSearch"]) if obj.get("smartSearch") is not None else None,
            "storageTemplateMigration": JobStatusDto.from_dict(obj["storageTemplateMigration"]) if obj.get("storageTemplateMigration") is not None else None,
            "thumbnailGeneration": JobStatusDto.from_dict(obj["thumbnailGeneration"]) if obj.get("thumbnailGeneration") is not None else None,
            "videoConversion": JobStatusDto.from_dict(obj["videoConversion"]) if obj.get("videoConversion") is not None else None
        })
        return _obj


