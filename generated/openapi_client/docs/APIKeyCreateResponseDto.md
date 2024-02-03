# APIKeyCreateResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | [**APIKeyResponseDto**](APIKeyResponseDto.md) |  | 
**secret** | **str** |  | 

## Example

```python
from openapi_client.models.api_key_create_response_dto import APIKeyCreateResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyCreateResponseDto from a JSON string
api_key_create_response_dto_instance = APIKeyCreateResponseDto.from_json(json)
# print the JSON string representation of the object
print APIKeyCreateResponseDto.to_json()

# convert the object into a dict
api_key_create_response_dto_dict = api_key_create_response_dto_instance.to_dict()
# create an instance of APIKeyCreateResponseDto from a dict
api_key_create_response_dto_form_dict = api_key_create_response_dto.from_dict(api_key_create_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


