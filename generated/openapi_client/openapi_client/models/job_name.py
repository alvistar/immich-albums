# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.94.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class JobName(str, Enum):
    """
    JobName
    """

    """
    allowed enum values
    """
    THUMBNAILGENERATION = 'thumbnailGeneration'
    METADATAEXTRACTION = 'metadataExtraction'
    VIDEOCONVERSION = 'videoConversion'
    FACEDETECTION = 'faceDetection'
    FACIALRECOGNITION = 'facialRecognition'
    SMARTSEARCH = 'smartSearch'
    BACKGROUNDTASK = 'backgroundTask'
    STORAGETEMPLATEMIGRATION = 'storageTemplateMigration'
    MIGRATION = 'migration'
    SEARCH = 'search'
    SIDECAR = 'sidecar'
    LIBRARY = 'library'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of JobName from a JSON string"""
        return cls(json.loads(json_str))


