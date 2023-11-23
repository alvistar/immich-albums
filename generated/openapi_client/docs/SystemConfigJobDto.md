# SystemConfigJobDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_task** | [**JobSettingsDto**](JobSettingsDto.md) |  | 
**clip_encoding** | [**JobSettingsDto**](JobSettingsDto.md) |  | 
**library** | [**JobSettingsDto**](JobSettingsDto.md) |  | 
**metadata_extraction** | [**JobSettingsDto**](JobSettingsDto.md) |  | 
**migration** | [**JobSettingsDto**](JobSettingsDto.md) |  | 
**object_tagging** | [**JobSettingsDto**](JobSettingsDto.md) |  | 
**recognize_faces** | [**JobSettingsDto**](JobSettingsDto.md) |  | 
**search** | [**JobSettingsDto**](JobSettingsDto.md) |  | 
**sidecar** | [**JobSettingsDto**](JobSettingsDto.md) |  | 
**storage_template_migration** | [**JobSettingsDto**](JobSettingsDto.md) |  | 
**thumbnail_generation** | [**JobSettingsDto**](JobSettingsDto.md) |  | 
**video_conversion** | [**JobSettingsDto**](JobSettingsDto.md) |  | 

## Example

```python
from openapi_client.models.system_config_job_dto import SystemConfigJobDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigJobDto from a JSON string
system_config_job_dto_instance = SystemConfigJobDto.from_json(json)
# print the JSON string representation of the object
print SystemConfigJobDto.to_json()

# convert the object into a dict
system_config_job_dto_dict = system_config_job_dto_instance.to_dict()
# create an instance of SystemConfigJobDto from a dict
system_config_job_dto_form_dict = system_config_job_dto.from_dict(system_config_job_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


