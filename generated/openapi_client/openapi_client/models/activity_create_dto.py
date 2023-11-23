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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.reaction_type import ReactionType

class ActivityCreateDto(BaseModel):
    """
    ActivityCreateDto
    """
    album_id: StrictStr = Field(..., alias="albumId")
    asset_id: Optional[StrictStr] = Field(None, alias="assetId")
    comment: Optional[StrictStr] = None
    type: ReactionType = Field(...)
    __properties = ["albumId", "assetId", "comment", "type"]

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
    def from_json(cls, json_str: str) -> ActivityCreateDto:
        """Create an instance of ActivityCreateDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ActivityCreateDto:
        """Create an instance of ActivityCreateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ActivityCreateDto.parse_obj(obj)

        _obj = ActivityCreateDto.parse_obj({
            "album_id": obj.get("albumId"),
            "asset_id": obj.get("assetId"),
            "comment": obj.get("comment"),
            "type": obj.get("type")
        })
        return _obj

