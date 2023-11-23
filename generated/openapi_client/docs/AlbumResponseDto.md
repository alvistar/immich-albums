# AlbumResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**album_name** | **str** |  | 
**album_thumbnail_asset_id** | **str** |  | 
**asset_count** | **int** |  | 
**assets** | [**List[AssetResponseDto]**](AssetResponseDto.md) |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**end_date** | **datetime** |  | [optional] 
**has_shared_link** | **bool** |  | 
**id** | **str** |  | 
**is_activity_enabled** | **bool** |  | 
**last_modified_asset_timestamp** | **datetime** |  | [optional] 
**owner** | [**UserResponseDto**](UserResponseDto.md) |  | 
**owner_id** | **str** |  | 
**shared** | **bool** |  | 
**shared_users** | [**List[UserResponseDto]**](UserResponseDto.md) |  | 
**start_date** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.album_response_dto import AlbumResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumResponseDto from a JSON string
album_response_dto_instance = AlbumResponseDto.from_json(json)
# print the JSON string representation of the object
print AlbumResponseDto.to_json()

# convert the object into a dict
album_response_dto_dict = album_response_dto_instance.to_dict()
# create an instance of AlbumResponseDto from a dict
album_response_dto_form_dict = album_response_dto.from_dict(album_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


