# openapi_client.AssetApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_bulk_upload**](AssetApi.md#check_bulk_upload) | **POST** /asset/bulk-upload-check | 
[**check_existing_assets**](AssetApi.md#check_existing_assets) | **POST** /asset/exist | 
[**delete_assets**](AssetApi.md#delete_assets) | **DELETE** /asset | 
[**get_all_assets**](AssetApi.md#get_all_assets) | **GET** /asset | 
[**get_all_user_assets_by_device_id**](AssetApi.md#get_all_user_assets_by_device_id) | **GET** /asset/device/{deviceId} | 
[**get_asset_info**](AssetApi.md#get_asset_info) | **GET** /asset/{id} | 
[**get_asset_statistics**](AssetApi.md#get_asset_statistics) | **GET** /asset/statistics | 
[**get_asset_thumbnail**](AssetApi.md#get_asset_thumbnail) | **GET** /asset/thumbnail/{id} | 
[**get_map_markers**](AssetApi.md#get_map_markers) | **GET** /asset/map-marker | 
[**get_memory_lane**](AssetApi.md#get_memory_lane) | **GET** /asset/memory-lane | 
[**get_random**](AssetApi.md#get_random) | **GET** /asset/random | 
[**run_asset_jobs**](AssetApi.md#run_asset_jobs) | **POST** /asset/jobs | 
[**serve_file**](AssetApi.md#serve_file) | **GET** /asset/file/{id} | 
[**update_asset**](AssetApi.md#update_asset) | **PUT** /asset/{id} | 
[**update_assets**](AssetApi.md#update_assets) | **PUT** /asset | 
[**update_stack_parent**](AssetApi.md#update_stack_parent) | **PUT** /asset/stack/parent | 
[**upload_file**](AssetApi.md#upload_file) | **POST** /asset/upload | 


# **check_bulk_upload**
> AssetBulkUploadCheckResponseDto check_bulk_upload(asset_bulk_upload_check_dto)



Checks if assets exist by checksums

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.asset_bulk_upload_check_dto import AssetBulkUploadCheckDto
from openapi_client.models.asset_bulk_upload_check_response_dto import AssetBulkUploadCheckResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetApi(api_client)
    asset_bulk_upload_check_dto = openapi_client.AssetBulkUploadCheckDto() # AssetBulkUploadCheckDto | 

    try:
        api_response = api_instance.check_bulk_upload(asset_bulk_upload_check_dto)
        print("The response of AssetApi->check_bulk_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->check_bulk_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_bulk_upload_check_dto** | [**AssetBulkUploadCheckDto**](AssetBulkUploadCheckDto.md)|  | 

### Return type

[**AssetBulkUploadCheckResponseDto**](AssetBulkUploadCheckResponseDto.md)

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_existing_assets**
> CheckExistingAssetsResponseDto check_existing_assets(check_existing_assets_dto)



Checks if multiple assets exist on the server and returns all existing - used by background backup

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.check_existing_assets_dto import CheckExistingAssetsDto
from openapi_client.models.check_existing_assets_response_dto import CheckExistingAssetsResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetApi(api_client)
    check_existing_assets_dto = openapi_client.CheckExistingAssetsDto() # CheckExistingAssetsDto | 

    try:
        api_response = api_instance.check_existing_assets(check_existing_assets_dto)
        print("The response of AssetApi->check_existing_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->check_existing_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_existing_assets_dto** | [**CheckExistingAssetsDto**](CheckExistingAssetsDto.md)|  | 

### Return type

[**CheckExistingAssetsResponseDto**](CheckExistingAssetsResponseDto.md)

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_assets**
> delete_assets(asset_bulk_delete_dto)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.asset_bulk_delete_dto import AssetBulkDeleteDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetApi(api_client)
    asset_bulk_delete_dto = openapi_client.AssetBulkDeleteDto() # AssetBulkDeleteDto | 

    try:
        api_instance.delete_assets(asset_bulk_delete_dto)
    except Exception as e:
        print("Exception when calling AssetApi->delete_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_bulk_delete_dto** | [**AssetBulkDeleteDto**](AssetBulkDeleteDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_assets**
> List[AssetResponseDto] get_all_assets(if_none_match=if_none_match, is_archived=is_archived, is_favorite=is_favorite, skip=skip, take=take, updated_after=updated_after, updated_before=updated_before, user_id=user_id)



Get all AssetEntity belong to the user

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.asset_response_dto import AssetResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetApi(api_client)
    if_none_match = 'if_none_match_example' # str | ETag of data already cached on the client (optional)
    is_archived = True # bool |  (optional)
    is_favorite = True # bool |  (optional)
    skip = 56 # int |  (optional)
    take = 56 # int |  (optional)
    updated_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    updated_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    user_id = 'user_id_example' # str |  (optional)

    try:
        api_response = api_instance.get_all_assets(if_none_match=if_none_match, is_archived=is_archived, is_favorite=is_favorite, skip=skip, take=take, updated_after=updated_after, updated_before=updated_before, user_id=user_id)
        print("The response of AssetApi->get_all_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_all_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_none_match** | **str**| ETag of data already cached on the client | [optional] 
 **is_archived** | **bool**|  | [optional] 
 **is_favorite** | **bool**|  | [optional] 
 **skip** | **int**|  | [optional] 
 **take** | **int**|  | [optional] 
 **updated_after** | **datetime**|  | [optional] 
 **updated_before** | **datetime**|  | [optional] 
 **user_id** | **str**|  | [optional] 

### Return type

[**List[AssetResponseDto]**](AssetResponseDto.md)

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_user_assets_by_device_id**
> List[str] get_all_user_assets_by_device_id(device_id)



Get all asset of a device that are in the database, ID only.

### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        api_response = api_instance.get_all_user_assets_by_device_id(device_id)
        print("The response of AssetApi->get_all_user_assets_by_device_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_all_user_assets_by_device_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

**List[str]**

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_info**
> AssetResponseDto get_asset_info(id, key=key)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.asset_response_dto import AssetResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetApi(api_client)
    id = 'id_example' # str | 
    key = 'key_example' # str |  (optional)

    try:
        api_response = api_instance.get_asset_info(id, key=key)
        print("The response of AssetApi->get_asset_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_asset_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **key** | **str**|  | [optional] 

### Return type

[**AssetResponseDto**](AssetResponseDto.md)

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_statistics**
> AssetStatsResponseDto get_asset_statistics(is_archived=is_archived, is_favorite=is_favorite, is_trashed=is_trashed)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.asset_stats_response_dto import AssetStatsResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetApi(api_client)
    is_archived = True # bool |  (optional)
    is_favorite = True # bool |  (optional)
    is_trashed = True # bool |  (optional)

    try:
        api_response = api_instance.get_asset_statistics(is_archived=is_archived, is_favorite=is_favorite, is_trashed=is_trashed)
        print("The response of AssetApi->get_asset_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_asset_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archived** | **bool**|  | [optional] 
 **is_favorite** | **bool**|  | [optional] 
 **is_trashed** | **bool**|  | [optional] 

### Return type

[**AssetStatsResponseDto**](AssetStatsResponseDto.md)

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_thumbnail**
> bytearray get_asset_thumbnail(id, format=format, key=key)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.thumbnail_format import ThumbnailFormat
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetApi(api_client)
    id = 'id_example' # str | 
    format = openapi_client.ThumbnailFormat() # ThumbnailFormat |  (optional)
    key = 'key_example' # str |  (optional)

    try:
        api_response = api_instance.get_asset_thumbnail(id, format=format, key=key)
        print("The response of AssetApi->get_asset_thumbnail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_asset_thumbnail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **format** | [**ThumbnailFormat**](.md)|  | [optional] 
 **key** | **str**|  | [optional] 

### Return type

**bytearray**

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_map_markers**
> List[MapMarkerResponseDto] get_map_markers(file_created_after=file_created_after, file_created_before=file_created_before, is_archived=is_archived, is_favorite=is_favorite, with_partners=with_partners, with_shared_albums=with_shared_albums)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.map_marker_response_dto import MapMarkerResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetApi(api_client)
    file_created_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    file_created_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    is_archived = True # bool |  (optional)
    is_favorite = True # bool |  (optional)
    with_partners = True # bool |  (optional)
    with_shared_albums = True # bool |  (optional)

    try:
        api_response = api_instance.get_map_markers(file_created_after=file_created_after, file_created_before=file_created_before, is_archived=is_archived, is_favorite=is_favorite, with_partners=with_partners, with_shared_albums=with_shared_albums)
        print("The response of AssetApi->get_map_markers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_map_markers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_created_after** | **datetime**|  | [optional] 
 **file_created_before** | **datetime**|  | [optional] 
 **is_archived** | **bool**|  | [optional] 
 **is_favorite** | **bool**|  | [optional] 
 **with_partners** | **bool**|  | [optional] 
 **with_shared_albums** | **bool**|  | [optional] 

### Return type

[**List[MapMarkerResponseDto]**](MapMarkerResponseDto.md)

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_memory_lane**
> List[MemoryLaneResponseDto] get_memory_lane(day, month)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.memory_lane_response_dto import MemoryLaneResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetApi(api_client)
    day = 56 # int | 
    month = 56 # int | 

    try:
        api_response = api_instance.get_memory_lane(day, month)
        print("The response of AssetApi->get_memory_lane:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_memory_lane: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **day** | **int**|  | 
 **month** | **int**|  | 

### Return type

[**List[MemoryLaneResponseDto]**](MemoryLaneResponseDto.md)

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_random**
> List[AssetResponseDto] get_random(count=count)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.asset_response_dto import AssetResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetApi(api_client)
    count = 3.4 # float |  (optional)

    try:
        api_response = api_instance.get_random(count=count)
        print("The response of AssetApi->get_random:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_random: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **float**|  | [optional] 

### Return type

[**List[AssetResponseDto]**](AssetResponseDto.md)

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_asset_jobs**
> run_asset_jobs(asset_jobs_dto)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.asset_jobs_dto import AssetJobsDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetApi(api_client)
    asset_jobs_dto = openapi_client.AssetJobsDto() # AssetJobsDto | 

    try:
        api_instance.run_asset_jobs(asset_jobs_dto)
    except Exception as e:
        print("Exception when calling AssetApi->run_asset_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_jobs_dto** | [**AssetJobsDto**](AssetJobsDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_file**
> bytearray serve_file(id, is_thumb=is_thumb, is_web=is_web, key=key)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetApi(api_client)
    id = 'id_example' # str | 
    is_thumb = True # bool |  (optional)
    is_web = True # bool |  (optional)
    key = 'key_example' # str |  (optional)

    try:
        api_response = api_instance.serve_file(id, is_thumb=is_thumb, is_web=is_web, key=key)
        print("The response of AssetApi->serve_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->serve_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **is_thumb** | **bool**|  | [optional] 
 **is_web** | **bool**|  | [optional] 
 **key** | **str**|  | [optional] 

### Return type

**bytearray**

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset**
> AssetResponseDto update_asset(id, update_asset_dto)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.asset_response_dto import AssetResponseDto
from openapi_client.models.update_asset_dto import UpdateAssetDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetApi(api_client)
    id = 'id_example' # str | 
    update_asset_dto = openapi_client.UpdateAssetDto() # UpdateAssetDto | 

    try:
        api_response = api_instance.update_asset(id, update_asset_dto)
        print("The response of AssetApi->update_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->update_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_asset_dto** | [**UpdateAssetDto**](UpdateAssetDto.md)|  | 

### Return type

[**AssetResponseDto**](AssetResponseDto.md)

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_assets**
> update_assets(asset_bulk_update_dto)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.asset_bulk_update_dto import AssetBulkUpdateDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetApi(api_client)
    asset_bulk_update_dto = openapi_client.AssetBulkUpdateDto() # AssetBulkUpdateDto | 

    try:
        api_instance.update_assets(asset_bulk_update_dto)
    except Exception as e:
        print("Exception when calling AssetApi->update_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_bulk_update_dto** | [**AssetBulkUpdateDto**](AssetBulkUpdateDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stack_parent**
> update_stack_parent(update_stack_parent_dto)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.update_stack_parent_dto import UpdateStackParentDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetApi(api_client)
    update_stack_parent_dto = openapi_client.UpdateStackParentDto() # UpdateStackParentDto | 

    try:
        api_instance.update_stack_parent(update_stack_parent_dto)
    except Exception as e:
        print("Exception when calling AssetApi->update_stack_parent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_stack_parent_dto** | [**UpdateStackParentDto**](UpdateStackParentDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> AssetFileUploadResponseDto upload_file(asset_data, device_asset_id, device_id, file_created_at, file_modified_at, key=key, x_immich_checksum=x_immich_checksum, duration=duration, is_archived=is_archived, is_favorite=is_favorite, is_offline=is_offline, is_visible=is_visible, library_id=library_id, live_photo_data=live_photo_data, sidecar_data=sidecar_data)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.asset_file_upload_response_dto import AssetFileUploadResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AssetApi(api_client)
    asset_data = None # bytearray | 
    device_asset_id = 'device_asset_id_example' # str | 
    device_id = 'device_id_example' # str | 
    file_created_at = '2013-10-20T19:20:30+01:00' # datetime | 
    file_modified_at = '2013-10-20T19:20:30+01:00' # datetime | 
    key = 'key_example' # str |  (optional)
    x_immich_checksum = 'x_immich_checksum_example' # str | sha1 checksum that can be used for duplicate detection before the file is uploaded (optional)
    duration = 'duration_example' # str |  (optional)
    is_archived = True # bool |  (optional)
    is_favorite = True # bool |  (optional)
    is_offline = True # bool |  (optional)
    is_visible = True # bool |  (optional)
    library_id = 'library_id_example' # str |  (optional)
    live_photo_data = None # bytearray |  (optional)
    sidecar_data = None # bytearray |  (optional)

    try:
        api_response = api_instance.upload_file(asset_data, device_asset_id, device_id, file_created_at, file_modified_at, key=key, x_immich_checksum=x_immich_checksum, duration=duration, is_archived=is_archived, is_favorite=is_favorite, is_offline=is_offline, is_visible=is_visible, library_id=library_id, live_photo_data=live_photo_data, sidecar_data=sidecar_data)
        print("The response of AssetApi->upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_data** | **bytearray**|  | 
 **device_asset_id** | **str**|  | 
 **device_id** | **str**|  | 
 **file_created_at** | **datetime**|  | 
 **file_modified_at** | **datetime**|  | 
 **key** | **str**|  | [optional] 
 **x_immich_checksum** | **str**| sha1 checksum that can be used for duplicate detection before the file is uploaded | [optional] 
 **duration** | **str**|  | [optional] 
 **is_archived** | **bool**|  | [optional] 
 **is_favorite** | **bool**|  | [optional] 
 **is_offline** | **bool**|  | [optional] 
 **is_visible** | **bool**|  | [optional] 
 **library_id** | **str**|  | [optional] 
 **live_photo_data** | **bytearray**|  | [optional] 
 **sidecar_data** | **bytearray**|  | [optional] 

### Return type

[**AssetFileUploadResponseDto**](AssetFileUploadResponseDto.md)

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

