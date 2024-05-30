# SystemConfigSmtpDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**var_from** | **str** |  | 
**reply_to** | **str** |  | 
**transport** | [**SystemConfigSmtpTransportDto**](SystemConfigSmtpTransportDto.md) |  | 

## Example

```python
from openapi_client.models.system_config_smtp_dto import SystemConfigSmtpDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigSmtpDto from a JSON string
system_config_smtp_dto_instance = SystemConfigSmtpDto.from_json(json)
# print the JSON string representation of the object
print(SystemConfigSmtpDto.to_json())

# convert the object into a dict
system_config_smtp_dto_dict = system_config_smtp_dto_instance.to_dict()
# create an instance of SystemConfigSmtpDto from a dict
system_config_smtp_dto_from_dict = SystemConfigSmtpDto.from_dict(system_config_smtp_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


