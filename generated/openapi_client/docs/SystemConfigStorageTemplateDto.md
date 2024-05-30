# SystemConfigStorageTemplateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**hash_verification_enabled** | **bool** |  | 
**template** | **str** |  | 

## Example

```python
from openapi_client.models.system_config_storage_template_dto import SystemConfigStorageTemplateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigStorageTemplateDto from a JSON string
system_config_storage_template_dto_instance = SystemConfigStorageTemplateDto.from_json(json)
# print the JSON string representation of the object
print(SystemConfigStorageTemplateDto.to_json())

# convert the object into a dict
system_config_storage_template_dto_dict = system_config_storage_template_dto_instance.to_dict()
# create an instance of SystemConfigStorageTemplateDto from a dict
system_config_storage_template_dto_from_dict = SystemConfigStorageTemplateDto.from_dict(system_config_storage_template_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


