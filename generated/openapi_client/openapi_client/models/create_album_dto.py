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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.album_user_create_dto import AlbumUserCreateDto
from typing import Optional, Set
from typing_extensions import Self

class CreateAlbumDto(BaseModel):
    """
    CreateAlbumDto
    """ # noqa: E501
    album_name: StrictStr = Field(alias="albumName")
    album_users: Optional[List[AlbumUserCreateDto]] = Field(default=None, description="This property was added in v1.104.0", alias="albumUsers")
    asset_ids: Optional[List[StrictStr]] = Field(default=None, alias="assetIds")
    description: Optional[StrictStr] = None
    shared_with_user_ids: Optional[List[StrictStr]] = Field(default=None, description="This property was deprecated in v1.104.0", alias="sharedWithUserIds")
    __properties: ClassVar[List[str]] = ["albumName", "albumUsers", "assetIds", "description", "sharedWithUserIds"]

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
        """Create an instance of CreateAlbumDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in album_users (list)
        _items = []
        if self.album_users:
            for _item in self.album_users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['albumUsers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateAlbumDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "albumName": obj.get("albumName"),
            "albumUsers": [AlbumUserCreateDto.from_dict(_item) for _item in obj["albumUsers"]] if obj.get("albumUsers") is not None else None,
            "assetIds": obj.get("assetIds"),
            "description": obj.get("description"),
            "sharedWithUserIds": obj.get("sharedWithUserIds")
        })
        return _obj


