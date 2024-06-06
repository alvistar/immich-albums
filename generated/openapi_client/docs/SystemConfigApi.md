# openapi_client.SystemConfigApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config**](SystemConfigApi.md#get_config) | **GET** /system-config | 
[**get_config_defaults**](SystemConfigApi.md#get_config_defaults) | **GET** /system-config/defaults | 
[**get_map_style**](SystemConfigApi.md#get_map_style) | **GET** /system-config/map/style.json | 
[**get_storage_template_options**](SystemConfigApi.md#get_storage_template_options) | **GET** /system-config/storage-template-options | 
[**update_config**](SystemConfigApi.md#update_config) | **PUT** /system-config | 


# **get_config**
> SystemConfigDto get_config()



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.system_config_dto import SystemConfigDto
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
    api_instance = openapi_client.SystemConfigApi(api_client)

    try:
        api_response = api_instance.get_config()
        print("The response of SystemConfigApi->get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemConfigApi->get_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemConfigDto**](SystemConfigDto.md)

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

# **get_config_defaults**
> SystemConfigDto get_config_defaults()



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.system_config_dto import SystemConfigDto
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
    api_instance = openapi_client.SystemConfigApi(api_client)

    try:
        api_response = api_instance.get_config_defaults()
        print("The response of SystemConfigApi->get_config_defaults:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemConfigApi->get_config_defaults: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemConfigDto**](SystemConfigDto.md)

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

# **get_map_style**
> object get_map_style(theme, key=key)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.map_theme import MapTheme
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
    api_instance = openapi_client.SystemConfigApi(api_client)
    theme = openapi_client.MapTheme() # MapTheme | 
    key = 'key_example' # str |  (optional)

    try:
        api_response = api_instance.get_map_style(theme, key=key)
        print("The response of SystemConfigApi->get_map_style:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemConfigApi->get_map_style: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **theme** | [**MapTheme**](.md)|  | 
 **key** | **str**|  | [optional] 

### Return type

**object**

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

# **get_storage_template_options**
> SystemConfigTemplateStorageOptionDto get_storage_template_options()



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.system_config_template_storage_option_dto import SystemConfigTemplateStorageOptionDto
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
    api_instance = openapi_client.SystemConfigApi(api_client)

    try:
        api_response = api_instance.get_storage_template_options()
        print("The response of SystemConfigApi->get_storage_template_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemConfigApi->get_storage_template_options: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemConfigTemplateStorageOptionDto**](SystemConfigTemplateStorageOptionDto.md)

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

# **update_config**
> SystemConfigDto update_config(system_config_dto)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.system_config_dto import SystemConfigDto
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
    api_instance = openapi_client.SystemConfigApi(api_client)
    system_config_dto = openapi_client.SystemConfigDto() # SystemConfigDto | 

    try:
        api_response = api_instance.update_config(system_config_dto)
        print("The response of SystemConfigApi->update_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemConfigApi->update_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_config_dto** | [**SystemConfigDto**](SystemConfigDto.md)|  | 

### Return type

[**SystemConfigDto**](SystemConfigDto.md)

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

