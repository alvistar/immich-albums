# AddUsersDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**album_users** | [**List[AlbumUserAddDto]**](AlbumUserAddDto.md) |  | 
**shared_user_ids** | **List[str]** | This property was deprecated in v1.102.0 | [optional] 

## Example

```python
from openapi_client.models.add_users_dto import AddUsersDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddUsersDto from a JSON string
add_users_dto_instance = AddUsersDto.from_json(json)
# print the JSON string representation of the object
print(AddUsersDto.to_json())

# convert the object into a dict
add_users_dto_dict = add_users_dto_instance.to_dict()
# create an instance of AddUsersDto from a dict
add_users_dto_from_dict = AddUsersDto.from_dict(add_users_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


