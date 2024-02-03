# UpdateUserDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_color** | [**UserAvatarColor**](UserAvatarColor.md) |  | [optional] 
**email** | **str** |  | [optional] 
**external_path** | **str** |  | [optional] 
**id** | **str** |  | 
**is_admin** | **bool** |  | [optional] 
**memories_enabled** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**quota_size_in_bytes** | **int** |  | [optional] 
**should_change_password** | **bool** |  | [optional] 
**storage_label** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.update_user_dto import UpdateUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserDto from a JSON string
update_user_dto_instance = UpdateUserDto.from_json(json)
# print the JSON string representation of the object
print UpdateUserDto.to_json()

# convert the object into a dict
update_user_dto_dict = update_user_dto_instance.to_dict()
# create an instance of UpdateUserDto from a dict
update_user_dto_form_dict = update_user_dto.from_dict(update_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


