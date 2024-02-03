# SearchResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**albums** | [**SearchAlbumResponseDto**](SearchAlbumResponseDto.md) |  | 
**assets** | [**SearchAssetResponseDto**](SearchAssetResponseDto.md) |  | 

## Example

```python
from openapi_client.models.search_response_dto import SearchResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponseDto from a JSON string
search_response_dto_instance = SearchResponseDto.from_json(json)
# print the JSON string representation of the object
print SearchResponseDto.to_json()

# convert the object into a dict
search_response_dto_dict = search_response_dto_instance.to_dict()
# create an instance of SearchResponseDto from a dict
search_response_dto_form_dict = search_response_dto.from_dict(search_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


