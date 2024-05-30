# AlbumUserResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**AlbumUserRole**](AlbumUserRole.md) |  | 
**user** | [**UserResponseDto**](UserResponseDto.md) |  | 

## Example

```python
from openapi_client.models.album_user_response_dto import AlbumUserResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumUserResponseDto from a JSON string
album_user_response_dto_instance = AlbumUserResponseDto.from_json(json)
# print the JSON string representation of the object
print(AlbumUserResponseDto.to_json())

# convert the object into a dict
album_user_response_dto_dict = album_user_response_dto_instance.to_dict()
# create an instance of AlbumUserResponseDto from a dict
album_user_response_dto_from_dict = AlbumUserResponseDto.from_dict(album_user_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


