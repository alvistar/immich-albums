# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.105.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class VideoCodec(str, Enum):
    """
    VideoCodec
    """

    """
    allowed enum values
    """
    H264 = 'h264'
    HEVC = 'hevc'
    VP9 = 'vp9'
    AV1 = 'av1'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VideoCodec from a JSON string"""
        return cls(json.loads(json_str))


