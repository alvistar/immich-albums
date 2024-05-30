# SystemConfigSmtpTransportDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | 
**ignore_cert** | **bool** |  | 
**password** | **str** |  | 
**port** | **float** |  | 
**username** | **str** |  | 

## Example

```python
from openapi_client.models.system_config_smtp_transport_dto import SystemConfigSmtpTransportDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigSmtpTransportDto from a JSON string
system_config_smtp_transport_dto_instance = SystemConfigSmtpTransportDto.from_json(json)
# print the JSON string representation of the object
print(SystemConfigSmtpTransportDto.to_json())

# convert the object into a dict
system_config_smtp_transport_dto_dict = system_config_smtp_transport_dto_instance.to_dict()
# create an instance of SystemConfigSmtpTransportDto from a dict
system_config_smtp_transport_dto_from_dict = SystemConfigSmtpTransportDto.from_dict(system_config_smtp_transport_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


