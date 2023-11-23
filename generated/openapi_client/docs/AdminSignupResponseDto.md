# AdminSignupResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**email** | **str** |  | 
**first_name** | **str** |  | 
**id** | **str** |  | 
**last_name** | **str** |  | 

## Example

```python
from openapi_client.models.admin_signup_response_dto import AdminSignupResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSignupResponseDto from a JSON string
admin_signup_response_dto_instance = AdminSignupResponseDto.from_json(json)
# print the JSON string representation of the object
print AdminSignupResponseDto.to_json()

# convert the object into a dict
admin_signup_response_dto_dict = admin_signup_response_dto_instance.to_dict()
# create an instance of AdminSignupResponseDto from a dict
admin_signup_response_dto_form_dict = admin_signup_response_dto.from_dict(admin_signup_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


