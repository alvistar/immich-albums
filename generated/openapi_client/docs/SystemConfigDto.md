# SystemConfigDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ffmpeg** | [**SystemConfigFFmpegDto**](SystemConfigFFmpegDto.md) |  | 
**image** | [**SystemConfigImageDto**](SystemConfigImageDto.md) |  | 
**job** | [**SystemConfigJobDto**](SystemConfigJobDto.md) |  | 
**library** | [**SystemConfigLibraryDto**](SystemConfigLibraryDto.md) |  | 
**logging** | [**SystemConfigLoggingDto**](SystemConfigLoggingDto.md) |  | 
**machine_learning** | [**SystemConfigMachineLearningDto**](SystemConfigMachineLearningDto.md) |  | 
**map** | [**SystemConfigMapDto**](SystemConfigMapDto.md) |  | 
**new_version_check** | [**SystemConfigNewVersionCheckDto**](SystemConfigNewVersionCheckDto.md) |  | 
**notifications** | [**SystemConfigNotificationsDto**](SystemConfigNotificationsDto.md) |  | 
**oauth** | [**SystemConfigOAuthDto**](SystemConfigOAuthDto.md) |  | 
**password_login** | [**SystemConfigPasswordLoginDto**](SystemConfigPasswordLoginDto.md) |  | 
**reverse_geocoding** | [**SystemConfigReverseGeocodingDto**](SystemConfigReverseGeocodingDto.md) |  | 
**server** | [**SystemConfigServerDto**](SystemConfigServerDto.md) |  | 
**storage_template** | [**SystemConfigStorageTemplateDto**](SystemConfigStorageTemplateDto.md) |  | 
**theme** | [**SystemConfigThemeDto**](SystemConfigThemeDto.md) |  | 
**trash** | [**SystemConfigTrashDto**](SystemConfigTrashDto.md) |  | 
**user** | [**SystemConfigUserDto**](SystemConfigUserDto.md) |  | 

## Example

```python
from openapi_client.models.system_config_dto import SystemConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigDto from a JSON string
system_config_dto_instance = SystemConfigDto.from_json(json)
# print the JSON string representation of the object
print(SystemConfigDto.to_json())

# convert the object into a dict
system_config_dto_dict = system_config_dto_instance.to_dict()
# create an instance of SystemConfigDto from a dict
system_config_dto_from_dict = SystemConfigDto.from_dict(system_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


