# openapi_client.SyncApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_delta_sync**](SyncApi.md#get_delta_sync) | **POST** /sync/delta-sync | 
[**get_full_sync_for_user**](SyncApi.md#get_full_sync_for_user) | **POST** /sync/full-sync | 


# **get_delta_sync**
> AssetDeltaSyncResponseDto get_delta_sync(asset_delta_sync_dto)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.asset_delta_sync_dto import AssetDeltaSyncDto
from openapi_client.models.asset_delta_sync_response_dto import AssetDeltaSyncResponseDto
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
    api_instance = openapi_client.SyncApi(api_client)
    asset_delta_sync_dto = openapi_client.AssetDeltaSyncDto() # AssetDeltaSyncDto | 

    try:
        api_response = api_instance.get_delta_sync(asset_delta_sync_dto)
        print("The response of SyncApi->get_delta_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncApi->get_delta_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_delta_sync_dto** | [**AssetDeltaSyncDto**](AssetDeltaSyncDto.md)|  | 

### Return type

[**AssetDeltaSyncResponseDto**](AssetDeltaSyncResponseDto.md)

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

# **get_full_sync_for_user**
> List[AssetResponseDto] get_full_sync_for_user(asset_full_sync_dto)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.asset_full_sync_dto import AssetFullSyncDto
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
    api_instance = openapi_client.SyncApi(api_client)
    asset_full_sync_dto = openapi_client.AssetFullSyncDto() # AssetFullSyncDto | 

    try:
        api_response = api_instance.get_full_sync_for_user(asset_full_sync_dto)
        print("The response of SyncApi->get_full_sync_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyncApi->get_full_sync_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_full_sync_dto** | [**AssetFullSyncDto**](AssetFullSyncDto.md)|  | 

### Return type

[**List[AssetResponseDto]**](AssetResponseDto.md)

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

