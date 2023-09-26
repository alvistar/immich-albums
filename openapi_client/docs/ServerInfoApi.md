# openapi_client.ServerInfoApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_server_config**](ServerInfoApi.md#get_server_config) | **GET** /server-info/config | 
[**get_server_features**](ServerInfoApi.md#get_server_features) | **GET** /server-info/features | 
[**get_server_info**](ServerInfoApi.md#get_server_info) | **GET** /server-info | 
[**get_server_version**](ServerInfoApi.md#get_server_version) | **GET** /server-info/version | 
[**get_stats**](ServerInfoApi.md#get_stats) | **GET** /server-info/stats | 
[**get_supported_media_types**](ServerInfoApi.md#get_supported_media_types) | **GET** /server-info/media-types | 
[**ping_server**](ServerInfoApi.md#ping_server) | **GET** /server-info/ping | 


# **get_server_config**
> ServerConfigDto get_server_config()



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.server_config_dto import ServerConfigDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ServerInfoApi(api_client)

    try:
        api_response = api_instance.get_server_config()
        print("The response of ServerInfoApi->get_server_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerInfoApi->get_server_config: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerConfigDto**](ServerConfigDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_features**
> ServerFeaturesDto get_server_features()



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.server_features_dto import ServerFeaturesDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ServerInfoApi(api_client)

    try:
        api_response = api_instance.get_server_features()
        print("The response of ServerInfoApi->get_server_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerInfoApi->get_server_features: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerFeaturesDto**](ServerFeaturesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_info**
> ServerInfoResponseDto get_server_info()



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.server_info_response_dto import ServerInfoResponseDto
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
    api_instance = openapi_client.ServerInfoApi(api_client)

    try:
        api_response = api_instance.get_server_info()
        print("The response of ServerInfoApi->get_server_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerInfoApi->get_server_info: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerInfoResponseDto**](ServerInfoResponseDto.md)

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

# **get_server_version**
> ServerVersionResponseDto get_server_version()



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.server_version_response_dto import ServerVersionResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ServerInfoApi(api_client)

    try:
        api_response = api_instance.get_server_version()
        print("The response of ServerInfoApi->get_server_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerInfoApi->get_server_version: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerVersionResponseDto**](ServerVersionResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats**
> ServerStatsResponseDto get_stats()



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.server_stats_response_dto import ServerStatsResponseDto
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
    api_instance = openapi_client.ServerInfoApi(api_client)

    try:
        api_response = api_instance.get_stats()
        print("The response of ServerInfoApi->get_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerInfoApi->get_stats: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerStatsResponseDto**](ServerStatsResponseDto.md)

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

# **get_supported_media_types**
> ServerMediaTypesResponseDto get_supported_media_types()



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.server_media_types_response_dto import ServerMediaTypesResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ServerInfoApi(api_client)

    try:
        api_response = api_instance.get_supported_media_types()
        print("The response of ServerInfoApi->get_supported_media_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerInfoApi->get_supported_media_types: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerMediaTypesResponseDto**](ServerMediaTypesResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_server**
> ServerPingResponse ping_server()



### Example

```python
import time
import os
import openapi_client
from openapi_client.models.server_ping_response import ServerPingResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ServerInfoApi(api_client)

    try:
        api_response = api_instance.ping_server()
        print("The response of ServerInfoApi->ping_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerInfoApi->ping_server: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerPingResponse**](ServerPingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

