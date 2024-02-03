# SystemConfigTemplateStorageOptionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_options** | **List[str]** |  | 
**hour_options** | **List[str]** |  | 
**minute_options** | **List[str]** |  | 
**month_options** | **List[str]** |  | 
**preset_options** | **List[str]** |  | 
**second_options** | **List[str]** |  | 
**week_options** | **List[str]** |  | 
**year_options** | **List[str]** |  | 

## Example

```python
from openapi_client.models.system_config_template_storage_option_dto import SystemConfigTemplateStorageOptionDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigTemplateStorageOptionDto from a JSON string
system_config_template_storage_option_dto_instance = SystemConfigTemplateStorageOptionDto.from_json(json)
# print the JSON string representation of the object
print SystemConfigTemplateStorageOptionDto.to_json()

# convert the object into a dict
system_config_template_storage_option_dto_dict = system_config_template_storage_option_dto_instance.to_dict()
# create an instance of SystemConfigTemplateStorageOptionDto from a dict
system_config_template_storage_option_dto_form_dict = system_config_template_storage_option_dto.from_dict(system_config_template_storage_option_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


