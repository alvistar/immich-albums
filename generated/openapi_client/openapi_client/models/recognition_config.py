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
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from openapi_client.models.model_type import ModelType
from typing import Optional, Set
from typing_extensions import Self

class RecognitionConfig(BaseModel):
    """
    RecognitionConfig
    """ # noqa: E501
    enabled: StrictBool
    max_distance: Union[Annotated[float, Field(le=2, strict=True, ge=0)], Annotated[int, Field(le=2, strict=True, ge=0)]] = Field(alias="maxDistance")
    min_faces: Annotated[int, Field(strict=True, ge=1)] = Field(alias="minFaces")
    min_score: Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(alias="minScore")
    model_name: StrictStr = Field(alias="modelName")
    model_type: Optional[ModelType] = Field(default=None, alias="modelType")
    __properties: ClassVar[List[str]] = ["enabled", "maxDistance", "minFaces", "minScore", "modelName", "modelType"]

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
        """Create an instance of RecognitionConfig from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecognitionConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "enabled": obj.get("enabled"),
            "maxDistance": obj.get("maxDistance"),
            "minFaces": obj.get("minFaces"),
            "minScore": obj.get("minScore"),
            "modelName": obj.get("modelName"),
            "modelType": obj.get("modelType")
        })
        return _obj


