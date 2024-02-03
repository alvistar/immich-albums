# SearchAssetResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**facets** | [**List[SearchFacetResponseDto]**](SearchFacetResponseDto.md) |  | 
**items** | [**List[AssetResponseDto]**](AssetResponseDto.md) |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.search_asset_response_dto import SearchAssetResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchAssetResponseDto from a JSON string
search_asset_response_dto_instance = SearchAssetResponseDto.from_json(json)
# print the JSON string representation of the object
print SearchAssetResponseDto.to_json()

# convert the object into a dict
search_asset_response_dto_dict = search_asset_response_dto_instance.to_dict()
# create an instance of SearchAssetResponseDto from a dict
search_asset_response_dto_form_dict = search_asset_response_dto.from_dict(search_asset_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


