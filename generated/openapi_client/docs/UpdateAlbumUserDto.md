# UpdateAlbumUserDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**AlbumUserRole**](AlbumUserRole.md) |  | 

## Example

```python
from openapi_client.models.update_album_user_dto import UpdateAlbumUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAlbumUserDto from a JSON string
update_album_user_dto_instance = UpdateAlbumUserDto.from_json(json)
# print the JSON string representation of the object
print(UpdateAlbumUserDto.to_json())

# convert the object into a dict
update_album_user_dto_dict = update_album_user_dto_instance.to_dict()
# create an instance of UpdateAlbumUserDto from a dict
update_album_user_dto_from_dict = UpdateAlbumUserDto.from_dict(update_album_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


