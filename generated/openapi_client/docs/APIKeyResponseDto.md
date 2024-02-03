# APIKeyResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.api_key_response_dto import APIKeyResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyResponseDto from a JSON string
api_key_response_dto_instance = APIKeyResponseDto.from_json(json)
# print the JSON string representation of the object
print APIKeyResponseDto.to_json()

# convert the object into a dict
api_key_response_dto_dict = api_key_response_dto_instance.to_dict()
# create an instance of APIKeyResponseDto from a dict
api_key_response_dto_form_dict = api_key_response_dto.from_dict(api_key_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


