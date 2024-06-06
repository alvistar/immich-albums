# openapi_client.AuditApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_deletes**](AuditApi.md#get_audit_deletes) | **GET** /audit/deletes | 


# **get_audit_deletes**
> AuditDeletesResponseDto get_audit_deletes(after, entity_type, user_id=user_id)



### Example

* Api Key Authentication (cookie):
* Api Key Authentication (api_key):
* Bearer (JWT) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.audit_deletes_response_dto import AuditDeletesResponseDto
from openapi_client.models.entity_type import EntityType
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
    api_instance = openapi_client.AuditApi(api_client)
    after = '2013-10-20T19:20:30+01:00' # datetime | 
    entity_type = openapi_client.EntityType() # EntityType | 
    user_id = 'user_id_example' # str |  (optional)

    try:
        api_response = api_instance.get_audit_deletes(after, entity_type, user_id=user_id)
        print("The response of AuditApi->get_audit_deletes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditApi->get_audit_deletes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **datetime**|  | 
 **entity_type** | [**EntityType**](.md)|  | 
 **user_id** | **str**|  | [optional] 

### Return type

[**AuditDeletesResponseDto**](AuditDeletesResponseDto.md)

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

