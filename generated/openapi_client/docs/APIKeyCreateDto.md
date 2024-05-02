# APIKeyCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_key_create_dto import APIKeyCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyCreateDto from a JSON string
api_key_create_dto_instance = APIKeyCreateDto.from_json(json)
# print the JSON string representation of the object
print(APIKeyCreateDto.to_json())

# convert the object into a dict
api_key_create_dto_dict = api_key_create_dto_instance.to_dict()
# create an instance of APIKeyCreateDto from a dict
api_key_create_dto_from_dict = APIKeyCreateDto.from_dict(api_key_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


