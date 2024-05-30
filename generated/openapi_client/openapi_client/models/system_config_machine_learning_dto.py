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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from openapi_client.models.clip_config import CLIPConfig
from openapi_client.models.recognition_config import RecognitionConfig
from typing import Optional, Set
from typing_extensions import Self

class SystemConfigMachineLearningDto(BaseModel):
    """
    SystemConfigMachineLearningDto
    """ # noqa: E501
    clip: CLIPConfig
    enabled: StrictBool
    facial_recognition: RecognitionConfig = Field(alias="facialRecognition")
    url: StrictStr
    __properties: ClassVar[List[str]] = ["clip", "enabled", "facialRecognition", "url"]

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
        """Create an instance of SystemConfigMachineLearningDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of clip
        if self.clip:
            _dict['clip'] = self.clip.to_dict()
        # override the default output from pydantic by calling `to_dict()` of facial_recognition
        if self.facial_recognition:
            _dict['facialRecognition'] = self.facial_recognition.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SystemConfigMachineLearningDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clip": CLIPConfig.from_dict(obj["clip"]) if obj.get("clip") is not None else None,
            "enabled": obj.get("enabled"),
            "facialRecognition": RecognitionConfig.from_dict(obj["facialRecognition"]) if obj.get("facialRecognition") is not None else None,
            "url": obj.get("url")
        })
        return _obj


