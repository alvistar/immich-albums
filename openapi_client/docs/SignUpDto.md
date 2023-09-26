# SignUpDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from openapi_client.models.sign_up_dto import SignUpDto

# TODO update the JSON string below
json = "{}"
# create an instance of SignUpDto from a JSON string
sign_up_dto_instance = SignUpDto.from_json(json)
# print the JSON string representation of the object
print SignUpDto.to_json()

# convert the object into a dict
sign_up_dto_dict = sign_up_dto_instance.to_dict()
# create an instance of SignUpDto from a dict
sign_up_dto_form_dict = sign_up_dto.from_dict(sign_up_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


