# SystemConfigLibraryScanDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_expression** | **str** |  | 
**enabled** | **bool** |  | 

## Example

```python
from openapi_client.models.system_config_library_scan_dto import SystemConfigLibraryScanDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigLibraryScanDto from a JSON string
system_config_library_scan_dto_instance = SystemConfigLibraryScanDto.from_json(json)
# print the JSON string representation of the object
print(SystemConfigLibraryScanDto.to_json())

# convert the object into a dict
system_config_library_scan_dto_dict = system_config_library_scan_dto_instance.to_dict()
# create an instance of SystemConfigLibraryScanDto from a dict
system_config_library_scan_dto_from_dict = SystemConfigLibraryScanDto.from_dict(system_config_library_scan_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


