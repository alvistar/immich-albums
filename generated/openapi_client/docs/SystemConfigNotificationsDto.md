# SystemConfigNotificationsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**smtp** | [**SystemConfigSmtpDto**](SystemConfigSmtpDto.md) |  | 

## Example

```python
from openapi_client.models.system_config_notifications_dto import SystemConfigNotificationsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigNotificationsDto from a JSON string
system_config_notifications_dto_instance = SystemConfigNotificationsDto.from_json(json)
# print the JSON string representation of the object
print(SystemConfigNotificationsDto.to_json())

# convert the object into a dict
system_config_notifications_dto_dict = system_config_notifications_dto_instance.to_dict()
# create an instance of SystemConfigNotificationsDto from a dict
system_config_notifications_dto_from_dict = SystemConfigNotificationsDto.from_dict(system_config_notifications_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


