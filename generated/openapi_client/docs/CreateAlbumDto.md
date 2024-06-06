# CreateAlbumDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**album_name** | **str** |  | 
**album_users** | [**List[AlbumUserCreateDto]**](AlbumUserCreateDto.md) | This property was added in v1.104.0 | [optional] 
**asset_ids** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**shared_with_user_ids** | **List[str]** | This property was deprecated in v1.104.0 | [optional] 

## Example

```python
from openapi_client.models.create_album_dto import CreateAlbumDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAlbumDto from a JSON string
create_album_dto_instance = CreateAlbumDto.from_json(json)
# print the JSON string representation of the object
print(CreateAlbumDto.to_json())

# convert the object into a dict
create_album_dto_dict = create_album_dto_instance.to_dict()
# create an instance of CreateAlbumDto from a dict
create_album_dto_from_dict = CreateAlbumDto.from_dict(create_album_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


