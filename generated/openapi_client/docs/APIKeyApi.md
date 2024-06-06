# openapi_client.APIKeyApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](APIKeyApi.md#create_api_key) | **POST** /api-key | 
[**delete_api_key**](APIKeyApi.md#delete_api_key) | **DELETE** /api-key/{id} | 
[**get_api_key**](APIKeyApi.md#get_api_key) | **GET** /api-key/{id} | 
[**get_api_keys**](APIKeyApi.md#get_api_keys) | **GET** /api-key | 
[**update_api_key**](APIKeyApi.md#update_api_key) | **PUT** /api-key/{id} | 


# **create_api_key**
> APIKeyCreateResponseDto create_api_key(api_key_create_dto)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.api_key_create_dto import APIKeyCreateDto
from openapi_client.models.api_key_create_response_dto import APIKeyCreateResponseDto
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
    api_instance = openapi_client.APIKeyApi(api_client)
    api_key_create_dto = openapi_client.APIKeyCreateDto() # APIKeyCreateDto | 

    try:
        api_response = api_instance.create_api_key(api_key_create_dto)
        print("The response of APIKeyApi->create_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeyApi->create_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_create_dto** | [**APIKeyCreateDto**](APIKeyCreateDto.md)|  | 

### Return type

[**APIKeyCreateResponseDto**](APIKeyCreateResponseDto.md)

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> delete_api_key(id)



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
    api_instance = openapi_client.APIKeyApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_api_key(id)
    except Exception as e:
        print("Exception when calling APIKeyApi->delete_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key**
> APIKeyResponseDto get_api_key(id)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.api_key_response_dto import APIKeyResponseDto
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
    api_instance = openapi_client.APIKeyApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_api_key(id)
        print("The response of APIKeyApi->get_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeyApi->get_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**APIKeyResponseDto**](APIKeyResponseDto.md)

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

# **get_api_keys**
> List[APIKeyResponseDto] get_api_keys()



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.api_key_response_dto import APIKeyResponseDto
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
    api_instance = openapi_client.APIKeyApi(api_client)

    try:
        api_response = api_instance.get_api_keys()
        print("The response of APIKeyApi->get_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeyApi->get_api_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[APIKeyResponseDto]**](APIKeyResponseDto.md)

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

# **update_api_key**
> APIKeyResponseDto update_api_key(id, api_key_update_dto)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.api_key_response_dto import APIKeyResponseDto
from openapi_client.models.api_key_update_dto import APIKeyUpdateDto
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
    api_instance = openapi_client.APIKeyApi(api_client)
    id = 'id_example' # str | 
    api_key_update_dto = openapi_client.APIKeyUpdateDto() # APIKeyUpdateDto | 

    try:
        api_response = api_instance.update_api_key(id, api_key_update_dto)
        print("The response of APIKeyApi->update_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeyApi->update_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **api_key_update_dto** | [**APIKeyUpdateDto**](APIKeyUpdateDto.md)|  | 

### Return type

[**APIKeyResponseDto**](APIKeyResponseDto.md)

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

