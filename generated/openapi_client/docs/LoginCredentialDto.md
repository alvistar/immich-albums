# LoginCredentialDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from openapi_client.models.login_credential_dto import LoginCredentialDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginCredentialDto from a JSON string
login_credential_dto_instance = LoginCredentialDto.from_json(json)
# print the JSON string representation of the object
print LoginCredentialDto.to_json()

# convert the object into a dict
login_credential_dto_dict = login_credential_dto_instance.to_dict()
# create an instance of LoginCredentialDto from a dict
login_credential_dto_form_dict = login_credential_dto.from_dict(login_credential_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


