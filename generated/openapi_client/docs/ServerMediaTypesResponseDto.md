# ServerMediaTypesResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **List[str]** |  | 
**sidecar** | **List[str]** |  | 
**video** | **List[str]** |  | 

## Example

```python
from openapi_client.models.server_media_types_response_dto import ServerMediaTypesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServerMediaTypesResponseDto from a JSON string
server_media_types_response_dto_instance = ServerMediaTypesResponseDto.from_json(json)
# print the JSON string representation of the object
print ServerMediaTypesResponseDto.to_json()

# convert the object into a dict
server_media_types_response_dto_dict = server_media_types_response_dto_instance.to_dict()
# create an instance of ServerMediaTypesResponseDto from a dict
server_media_types_response_dto_form_dict = server_media_types_response_dto.from_dict(server_media_types_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


