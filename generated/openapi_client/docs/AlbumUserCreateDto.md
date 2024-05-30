# AlbumUserCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**AlbumUserRole**](AlbumUserRole.md) |  | 
**user_id** | **str** |  | 

## Example

```python
from openapi_client.models.album_user_create_dto import AlbumUserCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumUserCreateDto from a JSON string
album_user_create_dto_instance = AlbumUserCreateDto.from_json(json)
# print the JSON string representation of the object
print(AlbumUserCreateDto.to_json())

# convert the object into a dict
album_user_create_dto_dict = album_user_create_dto_instance.to_dict()
# create an instance of AlbumUserCreateDto from a dict
album_user_create_dto_from_dict = AlbumUserCreateDto.from_dict(album_user_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


