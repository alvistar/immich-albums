# LoginResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**is_admin** | **bool** |  | 
**name** | **str** |  | 
**profile_image_path** | **str** |  | 
**should_change_password** | **bool** |  | 
**user_email** | **str** |  | 
**user_id** | **str** |  | 

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


