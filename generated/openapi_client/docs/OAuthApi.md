# openapi_client.OAuthApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**finish_o_auth**](OAuthApi.md#finish_o_auth) | **POST** /oauth/callback | 
[**generate_o_auth_config**](OAuthApi.md#generate_o_auth_config) | **POST** /oauth/config | 
[**link_o_auth_account**](OAuthApi.md#link_o_auth_account) | **POST** /oauth/link | 
[**redirect_o_auth_to_mobile**](OAuthApi.md#redirect_o_auth_to_mobile) | **GET** /oauth/mobile-redirect | 
[**start_o_auth**](OAuthApi.md#start_o_auth) | **POST** /oauth/authorize | 
[**unlink_o_auth_account**](OAuthApi.md#unlink_o_auth_account) | **POST** /oauth/unlink | 


# **finish_o_auth**
> LoginResponseDto finish_o_auth(o_auth_callback_dto)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.login_response_dto import LoginResponseDto
from openapi_client.models.o_auth_callback_dto import OAuthCallbackDto
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
    api_instance = openapi_client.OAuthApi(api_client)
    o_auth_callback_dto = openapi_client.OAuthCallbackDto() # OAuthCallbackDto | 

    try:
        api_response = api_instance.finish_o_auth(o_auth_callback_dto)
        print("The response of OAuthApi->finish_o_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->finish_o_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_callback_dto** | [**OAuthCallbackDto**](OAuthCallbackDto.md)|  | 

### Return type

[**LoginResponseDto**](LoginResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_o_auth_config**
> OAuthConfigResponseDto generate_o_auth_config(o_auth_config_dto)



@deprecated use feature flags and /oauth/authorize

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.o_auth_config_dto import OAuthConfigDto
from openapi_client.models.o_auth_config_response_dto import OAuthConfigResponseDto
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
    api_instance = openapi_client.OAuthApi(api_client)
    o_auth_config_dto = openapi_client.OAuthConfigDto() # OAuthConfigDto | 

    try:
        api_response = api_instance.generate_o_auth_config(o_auth_config_dto)
        print("The response of OAuthApi->generate_o_auth_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->generate_o_auth_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_config_dto** | [**OAuthConfigDto**](OAuthConfigDto.md)|  | 

### Return type

[**OAuthConfigResponseDto**](OAuthConfigResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_o_auth_account**
> UserResponseDto link_o_auth_account(o_auth_callback_dto)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.o_auth_callback_dto import OAuthCallbackDto
from openapi_client.models.user_response_dto import UserResponseDto
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
    api_instance = openapi_client.OAuthApi(api_client)
    o_auth_callback_dto = openapi_client.OAuthCallbackDto() # OAuthCallbackDto | 

    try:
        api_response = api_instance.link_o_auth_account(o_auth_callback_dto)
        print("The response of OAuthApi->link_o_auth_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->link_o_auth_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_callback_dto** | [**OAuthCallbackDto**](OAuthCallbackDto.md)|  | 

### Return type

[**UserResponseDto**](UserResponseDto.md)

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

# **redirect_o_auth_to_mobile**
> redirect_o_auth_to_mobile()



### Example


```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.OAuthApi(api_client)

    try:
        api_instance.redirect_o_auth_to_mobile()
    except Exception as e:
        print("Exception when calling OAuthApi->redirect_o_auth_to_mobile: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_o_auth**
> OAuthAuthorizeResponseDto start_o_auth(o_auth_config_dto)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.o_auth_authorize_response_dto import OAuthAuthorizeResponseDto
from openapi_client.models.o_auth_config_dto import OAuthConfigDto
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
    api_instance = openapi_client.OAuthApi(api_client)
    o_auth_config_dto = openapi_client.OAuthConfigDto() # OAuthConfigDto | 

    try:
        api_response = api_instance.start_o_auth(o_auth_config_dto)
        print("The response of OAuthApi->start_o_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->start_o_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_config_dto** | [**OAuthConfigDto**](OAuthConfigDto.md)|  | 

### Return type

[**OAuthAuthorizeResponseDto**](OAuthAuthorizeResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_o_auth_account**
> UserResponseDto unlink_o_auth_account()



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.user_response_dto import UserResponseDto
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
    api_instance = openapi_client.OAuthApi(api_client)

    try:
        api_response = api_instance.unlink_o_auth_account()
        print("The response of OAuthApi->unlink_o_auth_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->unlink_o_auth_account: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserResponseDto**](UserResponseDto.md)

### Authorization

[cookie](../README.md#cookie), [api_key](../README.md#api_key), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

