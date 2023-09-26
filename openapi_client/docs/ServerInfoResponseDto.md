# ServerInfoResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_available** | **str** |  | 
**disk_available_raw** | **int** |  | 
**disk_size** | **str** |  | 
**disk_size_raw** | **int** |  | 
**disk_usage_percentage** | **float** |  | 
**disk_use** | **str** |  | 
**disk_use_raw** | **int** |  | 

## Example

```python
from openapi_client.models.server_info_response_dto import ServerInfoResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServerInfoResponseDto from a JSON string
server_info_response_dto_instance = ServerInfoResponseDto.from_json(json)
# print the JSON string representation of the object
print ServerInfoResponseDto.to_json()

# convert the object into a dict
server_info_response_dto_dict = server_info_response_dto_instance.to_dict()
# create an instance of ServerInfoResponseDto from a dict
server_info_response_dto_form_dict = server_info_response_dto.from_dict(server_info_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


