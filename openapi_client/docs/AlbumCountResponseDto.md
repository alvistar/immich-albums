# AlbumCountResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_shared** | **int** |  | 
**owned** | **int** |  | 
**shared** | **int** |  | 

## Example

```python
from openapi_client.models.album_count_response_dto import AlbumCountResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumCountResponseDto from a JSON string
album_count_response_dto_instance = AlbumCountResponseDto.from_json(json)
# print the JSON string representation of the object
print AlbumCountResponseDto.to_json()

# convert the object into a dict
album_count_response_dto_dict = album_count_response_dto_instance.to_dict()
# create an instance of AlbumCountResponseDto from a dict
album_count_response_dto_form_dict = album_count_response_dto.from_dict(album_count_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


