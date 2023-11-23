# SystemConfigOAuthDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_launch** | **bool** |  | 
**auto_register** | **bool** |  | 
**button_text** | **str** |  | 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**enabled** | **bool** |  | 
**issuer_url** | **str** |  | 
**mobile_override_enabled** | **bool** |  | 
**mobile_redirect_uri** | **str** |  | 
**scope** | **str** |  | 
**storage_label_claim** | **str** |  | 

## Example

```python
from openapi_client.models.system_config_o_auth_dto import SystemConfigOAuthDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigOAuthDto from a JSON string
system_config_o_auth_dto_instance = SystemConfigOAuthDto.from_json(json)
# print the JSON string representation of the object
print SystemConfigOAuthDto.to_json()

# convert the object into a dict
system_config_o_auth_dto_dict = system_config_o_auth_dto_instance.to_dict()
# create an instance of SystemConfigOAuthDto from a dict
system_config_o_auth_dto_form_dict = system_config_o_auth_dto.from_dict(system_config_o_auth_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


