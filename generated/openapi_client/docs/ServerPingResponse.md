# ServerPingResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**res** | **str** |  | [readonly] 

## Example

```python
from openapi_client.models.server_ping_response import ServerPingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServerPingResponse from a JSON string
server_ping_response_instance = ServerPingResponse.from_json(json)
# print the JSON string representation of the object
print ServerPingResponse.to_json()

# convert the object into a dict
server_ping_response_dict = server_ping_response_instance.to_dict()
# create an instance of ServerPingResponse from a dict
server_ping_response_form_dict = server_ping_response.from_dict(server_ping_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


