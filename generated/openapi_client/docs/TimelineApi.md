# openapi_client.TimelineApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_time_bucket**](TimelineApi.md#get_time_bucket) | **GET** /timeline/bucket | 
[**get_time_buckets**](TimelineApi.md#get_time_buckets) | **GET** /timeline/buckets | 


# **get_time_bucket**
> List[AssetResponseDto] get_time_bucket(size, time_bucket, album_id=album_id, is_archived=is_archived, is_favorite=is_favorite, is_trashed=is_trashed, key=key, order=order, person_id=person_id, user_id=user_id, with_partners=with_partners, with_stacked=with_stacked)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.asset_order import AssetOrder
from openapi_client.models.asset_response_dto import AssetResponseDto
from openapi_client.models.time_bucket_size import TimeBucketSize
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
    api_instance = openapi_client.TimelineApi(api_client)
    size = openapi_client.TimeBucketSize() # TimeBucketSize | 
    time_bucket = 'time_bucket_example' # str | 
    album_id = 'album_id_example' # str |  (optional)
    is_archived = True # bool |  (optional)
    is_favorite = True # bool |  (optional)
    is_trashed = True # bool |  (optional)
    key = 'key_example' # str |  (optional)
    order = openapi_client.AssetOrder() # AssetOrder |  (optional)
    person_id = 'person_id_example' # str |  (optional)
    user_id = 'user_id_example' # str |  (optional)
    with_partners = True # bool |  (optional)
    with_stacked = True # bool |  (optional)

    try:
        api_response = api_instance.get_time_bucket(size, time_bucket, album_id=album_id, is_archived=is_archived, is_favorite=is_favorite, is_trashed=is_trashed, key=key, order=order, person_id=person_id, user_id=user_id, with_partners=with_partners, with_stacked=with_stacked)
        print("The response of TimelineApi->get_time_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimelineApi->get_time_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | [**TimeBucketSize**](.md)|  | 
 **time_bucket** | **str**|  | 
 **album_id** | **str**|  | [optional] 
 **is_archived** | **bool**|  | [optional] 
 **is_favorite** | **bool**|  | [optional] 
 **is_trashed** | **bool**|  | [optional] 
 **key** | **str**|  | [optional] 
 **order** | [**AssetOrder**](.md)|  | [optional] 
 **person_id** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **with_partners** | **bool**|  | [optional] 
 **with_stacked** | **bool**|  | [optional] 

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

# **get_time_buckets**
> List[TimeBucketResponseDto] get_time_buckets(size, album_id=album_id, is_archived=is_archived, is_favorite=is_favorite, is_trashed=is_trashed, key=key, order=order, person_id=person_id, user_id=user_id, with_partners=with_partners, with_stacked=with_stacked)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.asset_order import AssetOrder
from openapi_client.models.time_bucket_response_dto import TimeBucketResponseDto
from openapi_client.models.time_bucket_size import TimeBucketSize
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
    api_instance = openapi_client.TimelineApi(api_client)
    size = openapi_client.TimeBucketSize() # TimeBucketSize | 
    album_id = 'album_id_example' # str |  (optional)
    is_archived = True # bool |  (optional)
    is_favorite = True # bool |  (optional)
    is_trashed = True # bool |  (optional)
    key = 'key_example' # str |  (optional)
    order = openapi_client.AssetOrder() # AssetOrder |  (optional)
    person_id = 'person_id_example' # str |  (optional)
    user_id = 'user_id_example' # str |  (optional)
    with_partners = True # bool |  (optional)
    with_stacked = True # bool |  (optional)

    try:
        api_response = api_instance.get_time_buckets(size, album_id=album_id, is_archived=is_archived, is_favorite=is_favorite, is_trashed=is_trashed, key=key, order=order, person_id=person_id, user_id=user_id, with_partners=with_partners, with_stacked=with_stacked)
        print("The response of TimelineApi->get_time_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimelineApi->get_time_buckets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | [**TimeBucketSize**](.md)|  | 
 **album_id** | **str**|  | [optional] 
 **is_archived** | **bool**|  | [optional] 
 **is_favorite** | **bool**|  | [optional] 
 **is_trashed** | **bool**|  | [optional] 
 **key** | **str**|  | [optional] 
 **order** | [**AssetOrder**](.md)|  | [optional] 
 **person_id** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **with_partners** | **bool**|  | [optional] 
 **with_stacked** | **bool**|  | [optional] 

### Return type

[**List[TimeBucketResponseDto]**](TimeBucketResponseDto.md)

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

