# SystemConfigMapDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dark_style** | **str** |  | 
**enabled** | **bool** |  | 
**light_style** | **str** |  | 

## Example

```python
from openapi_client.models.system_config_map_dto import SystemConfigMapDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigMapDto from a JSON string
system_config_map_dto_instance = SystemConfigMapDto.from_json(json)
# print the JSON string representation of the object
print SystemConfigMapDto.to_json()

# convert the object into a dict
system_config_map_dto_dict = system_config_map_dto_instance.to_dict()
# create an instance of SystemConfigMapDto from a dict
system_config_map_dto_form_dict = system_config_map_dto.from_dict(system_config_map_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


