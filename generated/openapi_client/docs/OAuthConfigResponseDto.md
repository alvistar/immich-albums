# OAuthConfigResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_launch** | **bool** |  | [optional] 
**button_text** | **str** |  | [optional] 
**enabled** | **bool** |  | 
**password_login_enabled** | **bool** |  | 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.o_auth_config_response_dto import OAuthConfigResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthConfigResponseDto from a JSON string
o_auth_config_response_dto_instance = OAuthConfigResponseDto.from_json(json)
# print the JSON string representation of the object
print OAuthConfigResponseDto.to_json()

# convert the object into a dict
o_auth_config_response_dto_dict = o_auth_config_response_dto_instance.to_dict()
# create an instance of OAuthConfigResponseDto from a dict
o_auth_config_response_dto_form_dict = o_auth_config_response_dto.from_dict(o_auth_config_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


