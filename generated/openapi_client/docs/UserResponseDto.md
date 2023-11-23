# UserResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_color** | [**UserAvatarColor**](UserAvatarColor.md) |  | 
**created_at** | **datetime** |  | 
**deleted_at** | **datetime** |  | 
**email** | **str** |  | 
**external_path** | **str** |  | 
**id** | **str** |  | 
**is_admin** | **bool** |  | 
**memories_enabled** | **bool** |  | [optional] 
**name** | **str** |  | 
**oauth_id** | **str** |  | 
**profile_image_path** | **str** |  | 
**should_change_password** | **bool** |  | 
**storage_label** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.user_response_dto import UserResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponseDto from a JSON string
user_response_dto_instance = UserResponseDto.from_json(json)
# print the JSON string representation of the object
print UserResponseDto.to_json()

# convert the object into a dict
user_response_dto_dict = user_response_dto_instance.to_dict()
# create an instance of UserResponseDto from a dict
user_response_dto_form_dict = user_response_dto.from_dict(user_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


