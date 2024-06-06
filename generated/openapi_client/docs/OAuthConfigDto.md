# OAuthConfigDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_uri** | **str** |  | 

## Example

```python
from openapi_client.models.o_auth_config_dto import OAuthConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthConfigDto from a JSON string
o_auth_config_dto_instance = OAuthConfigDto.from_json(json)
# print the JSON string representation of the object
print(OAuthConfigDto.to_json())

# convert the object into a dict
o_auth_config_dto_dict = o_auth_config_dto_instance.to_dict()
# create an instance of OAuthConfigDto from a dict
o_auth_config_dto_from_dict = OAuthConfigDto.from_dict(o_auth_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


