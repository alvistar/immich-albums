# openapi_client.SearchApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_explore_data**](SearchApi.md#get_explore_data) | **GET** /search/explore | 
[**search**](SearchApi.md#search) | **GET** /search | 
[**search_person**](SearchApi.md#search_person) | **GET** /search/person | 


# **get_explore_data**
> List[SearchExploreResponseDto] get_explore_data()



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.search_explore_response_dto import SearchExploreResponseDto
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
    api_instance = openapi_client.SearchApi(api_client)

    try:
        api_response = api_instance.get_explore_data()
        print("The response of SearchApi->get_explore_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_explore_data: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[SearchExploreResponseDto]**](SearchExploreResponseDto.md)

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

# **search**
> SearchResponseDto search(q=q, query=query, clip=clip, type=type, is_favorite=is_favorite, is_archived=is_archived, exif_info_city=exif_info_city, exif_info_state=exif_info_state, exif_info_country=exif_info_country, exif_info_make=exif_info_make, exif_info_model=exif_info_model, exif_info_projection_type=exif_info_projection_type, smart_info_objects=smart_info_objects, smart_info_tags=smart_info_tags, recent=recent, motion=motion)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.search_response_dto import SearchResponseDto
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
    api_instance = openapi_client.SearchApi(api_client)
    q = 'q_example' # str |  (optional)
    query = 'query_example' # str |  (optional)
    clip = True # bool |  (optional)
    type = 'type_example' # str |  (optional)
    is_favorite = True # bool |  (optional)
    is_archived = True # bool |  (optional)
    exif_info_city = 'exif_info_city_example' # str |  (optional)
    exif_info_state = 'exif_info_state_example' # str |  (optional)
    exif_info_country = 'exif_info_country_example' # str |  (optional)
    exif_info_make = 'exif_info_make_example' # str |  (optional)
    exif_info_model = 'exif_info_model_example' # str |  (optional)
    exif_info_projection_type = 'exif_info_projection_type_example' # str |  (optional)
    smart_info_objects = ['smart_info_objects_example'] # List[str] |  (optional)
    smart_info_tags = ['smart_info_tags_example'] # List[str] |  (optional)
    recent = True # bool |  (optional)
    motion = True # bool |  (optional)

    try:
        api_response = api_instance.search(q=q, query=query, clip=clip, type=type, is_favorite=is_favorite, is_archived=is_archived, exif_info_city=exif_info_city, exif_info_state=exif_info_state, exif_info_country=exif_info_country, exif_info_make=exif_info_make, exif_info_model=exif_info_model, exif_info_projection_type=exif_info_projection_type, smart_info_objects=smart_info_objects, smart_info_tags=smart_info_tags, recent=recent, motion=motion)
        print("The response of SearchApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 
 **clip** | **bool**|  | [optional] 
 **type** | **str**|  | [optional] 
 **is_favorite** | **bool**|  | [optional] 
 **is_archived** | **bool**|  | [optional] 
 **exif_info_city** | **str**|  | [optional] 
 **exif_info_state** | **str**|  | [optional] 
 **exif_info_country** | **str**|  | [optional] 
 **exif_info_make** | **str**|  | [optional] 
 **exif_info_model** | **str**|  | [optional] 
 **exif_info_projection_type** | **str**|  | [optional] 
 **smart_info_objects** | [**List[str]**](str.md)|  | [optional] 
 **smart_info_tags** | [**List[str]**](str.md)|  | [optional] 
 **recent** | **bool**|  | [optional] 
 **motion** | **bool**|  | [optional] 

### Return type

[**SearchResponseDto**](SearchResponseDto.md)

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

# **search_person**
> List[PersonResponseDto] search_person(name, with_hidden=with_hidden)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.person_response_dto import PersonResponseDto
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
    api_instance = openapi_client.SearchApi(api_client)
    name = 'name_example' # str | 
    with_hidden = True # bool |  (optional)

    try:
        api_response = api_instance.search_person(name, with_hidden=with_hidden)
        print("The response of SearchApi->search_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_person: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **with_hidden** | **bool**|  | [optional] 

### Return type

[**List[PersonResponseDto]**](PersonResponseDto.md)

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

