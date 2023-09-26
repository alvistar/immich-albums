# LoginResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [readonly] 
**first_name** | **str** |  | [readonly] 
**is_admin** | **bool** |  | [readonly] 
**last_name** | **str** |  | [readonly] 
**profile_image_path** | **str** |  | [readonly] 
**should_change_password** | **bool** |  | [readonly] 
**user_email** | **str** |  | [readonly] 
**user_id** | **str** |  | [readonly] 

## Example

```python
from openapi_client.models.login_response_dto import LoginResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginResponseDto from a JSON string
login_response_dto_instance = LoginResponseDto.from_json(json)
# print the JSON string representation of the object
print LoginResponseDto.to_json()

# convert the object into a dict
login_response_dto_dict = login_response_dto_instance.to_dict()
# create an instance of LoginResponseDto from a dict
login_response_dto_form_dict = login_response_dto.from_dict(login_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


