# ServerVersionResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**major** | **int** |  | 
**minor** | **int** |  | 
**patch** | **int** |  | 

## Example

```python
from openapi_client.models.server_version_response_dto import ServerVersionResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServerVersionResponseDto from a JSON string
server_version_response_dto_instance = ServerVersionResponseDto.from_json(json)
# print the JSON string representation of the object
print(ServerVersionResponseDto.to_json())

# convert the object into a dict
server_version_response_dto_dict = server_version_response_dto_instance.to_dict()
# create an instance of ServerVersionResponseDto from a dict
server_version_response_dto_from_dict = ServerVersionResponseDto.from_dict(server_version_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


