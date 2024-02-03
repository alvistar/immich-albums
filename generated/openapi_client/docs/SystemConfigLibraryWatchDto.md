# SystemConfigLibraryWatchDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**interval** | **int** |  | 
**use_polling** | **bool** |  | 

## Example

```python
from openapi_client.models.system_config_library_watch_dto import SystemConfigLibraryWatchDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigLibraryWatchDto from a JSON string
system_config_library_watch_dto_instance = SystemConfigLibraryWatchDto.from_json(json)
# print the JSON string representation of the object
print SystemConfigLibraryWatchDto.to_json()

# convert the object into a dict
system_config_library_watch_dto_dict = system_config_library_watch_dto_instance.to_dict()
# create an instance of SystemConfigLibraryWatchDto from a dict
system_config_library_watch_dto_form_dict = system_config_library_watch_dto.from_dict(system_config_library_watch_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


