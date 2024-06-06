# SystemConfigServerDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_domain** | **str** |  | 
**login_page_message** | **str** |  | 

## Example

```python
from openapi_client.models.system_config_server_dto import SystemConfigServerDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigServerDto from a JSON string
system_config_server_dto_instance = SystemConfigServerDto.from_json(json)
# print the JSON string representation of the object
print(SystemConfigServerDto.to_json())

# convert the object into a dict
system_config_server_dto_dict = system_config_server_dto_instance.to_dict()
# create an instance of SystemConfigServerDto from a dict
system_config_server_dto_from_dict = SystemConfigServerDto.from_dict(system_config_server_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


