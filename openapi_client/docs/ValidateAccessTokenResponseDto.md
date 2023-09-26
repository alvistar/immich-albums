# ValidateAccessTokenResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_status** | **bool** |  | 

## Example

```python
from openapi_client.models.validate_access_token_response_dto import ValidateAccessTokenResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateAccessTokenResponseDto from a JSON string
validate_access_token_response_dto_instance = ValidateAccessTokenResponseDto.from_json(json)
# print the JSON string representation of the object
print ValidateAccessTokenResponseDto.to_json()

# convert the object into a dict
validate_access_token_response_dto_dict = validate_access_token_response_dto_instance.to_dict()
# create an instance of ValidateAccessTokenResponseDto from a dict
validate_access_token_response_dto_form_dict = validate_access_token_response_dto.from_dict(validate_access_token_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


