# SystemConfigLibraryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scan** | [**SystemConfigLibraryScanDto**](SystemConfigLibraryScanDto.md) |  | 
**watch** | [**SystemConfigLibraryWatchDto**](SystemConfigLibraryWatchDto.md) |  | 

## Example

```python
from openapi_client.models.system_config_library_dto import SystemConfigLibraryDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigLibraryDto from a JSON string
system_config_library_dto_instance = SystemConfigLibraryDto.from_json(json)
# print the JSON string representation of the object
print(SystemConfigLibraryDto.to_json())

# convert the object into a dict
system_config_library_dto_dict = system_config_library_dto_instance.to_dict()
# create an instance of SystemConfigLibraryDto from a dict
system_config_library_dto_from_dict = SystemConfigLibraryDto.from_dict(system_config_library_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


