# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.105.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import StrictBool, StrictStr
from typing import List, Optional
from openapi_client.models.asset_order import AssetOrder
from openapi_client.models.asset_response_dto import AssetResponseDto
from openapi_client.models.time_bucket_response_dto import TimeBucketResponseDto
from openapi_client.models.time_bucket_size import TimeBucketSize

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class TimelineApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_time_bucket(
        self,
        size: TimeBucketSize,
        time_bucket: StrictStr,
        album_id: Optional[StrictStr] = None,
        is_archived: Optional[StrictBool] = None,
        is_favorite: Optional[StrictBool] = None,
        is_trashed: Optional[StrictBool] = None,
        key: Optional[StrictStr] = None,
        order: Optional[AssetOrder] = None,
        person_id: Optional[StrictStr] = None,
        user_id: Optional[StrictStr] = None,
        with_partners: Optional[StrictBool] = None,
        with_stacked: Optional[StrictBool] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[AssetResponseDto]:
        """get_time_bucket


        :param size: (required)
        :type size: TimeBucketSize
        :param time_bucket: (required)
        :type time_bucket: str
        :param album_id:
        :type album_id: str
        :param is_archived:
        :type is_archived: bool
        :param is_favorite:
        :type is_favorite: bool
        :param is_trashed:
        :type is_trashed: bool
        :param key:
        :type key: str
        :param order:
        :type order: AssetOrder
        :param person_id:
        :type person_id: str
        :param user_id:
        :type user_id: str
        :param with_partners:
        :type with_partners: bool
        :param with_stacked:
        :type with_stacked: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_time_bucket_serialize(
            size=size,
            time_bucket=time_bucket,
            album_id=album_id,
            is_archived=is_archived,
            is_favorite=is_favorite,
            is_trashed=is_trashed,
            key=key,
            order=order,
            person_id=person_id,
            user_id=user_id,
            with_partners=with_partners,
            with_stacked=with_stacked,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[AssetResponseDto]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_time_bucket_with_http_info(
        self,
        size: TimeBucketSize,
        time_bucket: StrictStr,
        album_id: Optional[StrictStr] = None,
        is_archived: Optional[StrictBool] = None,
        is_favorite: Optional[StrictBool] = None,
        is_trashed: Optional[StrictBool] = None,
        key: Optional[StrictStr] = None,
        order: Optional[AssetOrder] = None,
        person_id: Optional[StrictStr] = None,
        user_id: Optional[StrictStr] = None,
        with_partners: Optional[StrictBool] = None,
        with_stacked: Optional[StrictBool] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[AssetResponseDto]]:
        """get_time_bucket


        :param size: (required)
        :type size: TimeBucketSize
        :param time_bucket: (required)
        :type time_bucket: str
        :param album_id:
        :type album_id: str
        :param is_archived:
        :type is_archived: bool
        :param is_favorite:
        :type is_favorite: bool
        :param is_trashed:
        :type is_trashed: bool
        :param key:
        :type key: str
        :param order:
        :type order: AssetOrder
        :param person_id:
        :type person_id: str
        :param user_id:
        :type user_id: str
        :param with_partners:
        :type with_partners: bool
        :param with_stacked:
        :type with_stacked: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_time_bucket_serialize(
            size=size,
            time_bucket=time_bucket,
            album_id=album_id,
            is_archived=is_archived,
            is_favorite=is_favorite,
            is_trashed=is_trashed,
            key=key,
            order=order,
            person_id=person_id,
            user_id=user_id,
            with_partners=with_partners,
            with_stacked=with_stacked,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[AssetResponseDto]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_time_bucket_without_preload_content(
        self,
        size: TimeBucketSize,
        time_bucket: StrictStr,
        album_id: Optional[StrictStr] = None,
        is_archived: Optional[StrictBool] = None,
        is_favorite: Optional[StrictBool] = None,
        is_trashed: Optional[StrictBool] = None,
        key: Optional[StrictStr] = None,
        order: Optional[AssetOrder] = None,
        person_id: Optional[StrictStr] = None,
        user_id: Optional[StrictStr] = None,
        with_partners: Optional[StrictBool] = None,
        with_stacked: Optional[StrictBool] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """get_time_bucket


        :param size: (required)
        :type size: TimeBucketSize
        :param time_bucket: (required)
        :type time_bucket: str
        :param album_id:
        :type album_id: str
        :param is_archived:
        :type is_archived: bool
        :param is_favorite:
        :type is_favorite: bool
        :param is_trashed:
        :type is_trashed: bool
        :param key:
        :type key: str
        :param order:
        :type order: AssetOrder
        :param person_id:
        :type person_id: str
        :param user_id:
        :type user_id: str
        :param with_partners:
        :type with_partners: bool
        :param with_stacked:
        :type with_stacked: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_time_bucket_serialize(
            size=size,
            time_bucket=time_bucket,
            album_id=album_id,
            is_archived=is_archived,
            is_favorite=is_favorite,
            is_trashed=is_trashed,
            key=key,
            order=order,
            person_id=person_id,
            user_id=user_id,
            with_partners=with_partners,
            with_stacked=with_stacked,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[AssetResponseDto]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_time_bucket_serialize(
        self,
        size,
        time_bucket,
        album_id,
        is_archived,
        is_favorite,
        is_trashed,
        key,
        order,
        person_id,
        user_id,
        with_partners,
        with_stacked,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if album_id is not None:
            
            _query_params.append(('albumId', album_id))
            
        if is_archived is not None:
            
            _query_params.append(('isArchived', is_archived))
            
        if is_favorite is not None:
            
            _query_params.append(('isFavorite', is_favorite))
            
        if is_trashed is not None:
            
            _query_params.append(('isTrashed', is_trashed))
            
        if key is not None:
            
            _query_params.append(('key', key))
            
        if order is not None:
            
            _query_params.append(('order', order.value))
            
        if person_id is not None:
            
            _query_params.append(('personId', person_id))
            
        if size is not None:
            
            _query_params.append(('size', size.value))
            
        if time_bucket is not None:
            
            _query_params.append(('timeBucket', time_bucket))
            
        if user_id is not None:
            
            _query_params.append(('userId', user_id))
            
        if with_partners is not None:
            
            _query_params.append(('withPartners', with_partners))
            
        if with_stacked is not None:
            
            _query_params.append(('withStacked', with_stacked))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'cookie', 
            'api_key', 
            'bearer'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/timeline/bucket',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_time_buckets(
        self,
        size: TimeBucketSize,
        album_id: Optional[StrictStr] = None,
        is_archived: Optional[StrictBool] = None,
        is_favorite: Optional[StrictBool] = None,
        is_trashed: Optional[StrictBool] = None,
        key: Optional[StrictStr] = None,
        order: Optional[AssetOrder] = None,
        person_id: Optional[StrictStr] = None,
        user_id: Optional[StrictStr] = None,
        with_partners: Optional[StrictBool] = None,
        with_stacked: Optional[StrictBool] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[TimeBucketResponseDto]:
        """get_time_buckets


        :param size: (required)
        :type size: TimeBucketSize
        :param album_id:
        :type album_id: str
        :param is_archived:
        :type is_archived: bool
        :param is_favorite:
        :type is_favorite: bool
        :param is_trashed:
        :type is_trashed: bool
        :param key:
        :type key: str
        :param order:
        :type order: AssetOrder
        :param person_id:
        :type person_id: str
        :param user_id:
        :type user_id: str
        :param with_partners:
        :type with_partners: bool
        :param with_stacked:
        :type with_stacked: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_time_buckets_serialize(
            size=size,
            album_id=album_id,
            is_archived=is_archived,
            is_favorite=is_favorite,
            is_trashed=is_trashed,
            key=key,
            order=order,
            person_id=person_id,
            user_id=user_id,
            with_partners=with_partners,
            with_stacked=with_stacked,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[TimeBucketResponseDto]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_time_buckets_with_http_info(
        self,
        size: TimeBucketSize,
        album_id: Optional[StrictStr] = None,
        is_archived: Optional[StrictBool] = None,
        is_favorite: Optional[StrictBool] = None,
        is_trashed: Optional[StrictBool] = None,
        key: Optional[StrictStr] = None,
        order: Optional[AssetOrder] = None,
        person_id: Optional[StrictStr] = None,
        user_id: Optional[StrictStr] = None,
        with_partners: Optional[StrictBool] = None,
        with_stacked: Optional[StrictBool] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[TimeBucketResponseDto]]:
        """get_time_buckets


        :param size: (required)
        :type size: TimeBucketSize
        :param album_id:
        :type album_id: str
        :param is_archived:
        :type is_archived: bool
        :param is_favorite:
        :type is_favorite: bool
        :param is_trashed:
        :type is_trashed: bool
        :param key:
        :type key: str
        :param order:
        :type order: AssetOrder
        :param person_id:
        :type person_id: str
        :param user_id:
        :type user_id: str
        :param with_partners:
        :type with_partners: bool
        :param with_stacked:
        :type with_stacked: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_time_buckets_serialize(
            size=size,
            album_id=album_id,
            is_archived=is_archived,
            is_favorite=is_favorite,
            is_trashed=is_trashed,
            key=key,
            order=order,
            person_id=person_id,
            user_id=user_id,
            with_partners=with_partners,
            with_stacked=with_stacked,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[TimeBucketResponseDto]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_time_buckets_without_preload_content(
        self,
        size: TimeBucketSize,
        album_id: Optional[StrictStr] = None,
        is_archived: Optional[StrictBool] = None,
        is_favorite: Optional[StrictBool] = None,
        is_trashed: Optional[StrictBool] = None,
        key: Optional[StrictStr] = None,
        order: Optional[AssetOrder] = None,
        person_id: Optional[StrictStr] = None,
        user_id: Optional[StrictStr] = None,
        with_partners: Optional[StrictBool] = None,
        with_stacked: Optional[StrictBool] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """get_time_buckets


        :param size: (required)
        :type size: TimeBucketSize
        :param album_id:
        :type album_id: str
        :param is_archived:
        :type is_archived: bool
        :param is_favorite:
        :type is_favorite: bool
        :param is_trashed:
        :type is_trashed: bool
        :param key:
        :type key: str
        :param order:
        :type order: AssetOrder
        :param person_id:
        :type person_id: str
        :param user_id:
        :type user_id: str
        :param with_partners:
        :type with_partners: bool
        :param with_stacked:
        :type with_stacked: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_time_buckets_serialize(
            size=size,
            album_id=album_id,
            is_archived=is_archived,
            is_favorite=is_favorite,
            is_trashed=is_trashed,
            key=key,
            order=order,
            person_id=person_id,
            user_id=user_id,
            with_partners=with_partners,
            with_stacked=with_stacked,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[TimeBucketResponseDto]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_time_buckets_serialize(
        self,
        size,
        album_id,
        is_archived,
        is_favorite,
        is_trashed,
        key,
        order,
        person_id,
        user_id,
        with_partners,
        with_stacked,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if album_id is not None:
            
            _query_params.append(('albumId', album_id))
            
        if is_archived is not None:
            
            _query_params.append(('isArchived', is_archived))
            
        if is_favorite is not None:
            
            _query_params.append(('isFavorite', is_favorite))
            
        if is_trashed is not None:
            
            _query_params.append(('isTrashed', is_trashed))
            
        if key is not None:
            
            _query_params.append(('key', key))
            
        if order is not None:
            
            _query_params.append(('order', order.value))
            
        if person_id is not None:
            
            _query_params.append(('personId', person_id))
            
        if size is not None:
            
            _query_params.append(('size', size.value))
            
        if user_id is not None:
            
            _query_params.append(('userId', user_id))
            
        if with_partners is not None:
            
            _query_params.append(('withPartners', with_partners))
            
        if with_stacked is not None:
            
            _query_params.append(('withStacked', with_stacked))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'cookie', 
            'api_key', 
            'bearer'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/timeline/buckets',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


