# SystemConfigLoggingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**level** | [**LogLevel**](LogLevel.md) |  | 

## Example

```python
from openapi_client.models.system_config_logging_dto import SystemConfigLoggingDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigLoggingDto from a JSON string
system_config_logging_dto_instance = SystemConfigLoggingDto.from_json(json)
# print the JSON string representation of the object
print(SystemConfigLoggingDto.to_json())

# convert the object into a dict
system_config_logging_dto_dict = system_config_logging_dto_instance.to_dict()
# create an instance of SystemConfigLoggingDto from a dict
system_config_logging_dto_from_dict = SystemConfigLoggingDto.from_dict(system_config_logging_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


