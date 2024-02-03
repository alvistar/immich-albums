# SearchExploreResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | 
**items** | [**List[SearchExploreItem]**](SearchExploreItem.md) |  | 

## Example

```python
from openapi_client.models.search_explore_response_dto import SearchExploreResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchExploreResponseDto from a JSON string
search_explore_response_dto_instance = SearchExploreResponseDto.from_json(json)
# print the JSON string representation of the object
print SearchExploreResponseDto.to_json()

# convert the object into a dict
search_explore_response_dto_dict = search_explore_response_dto_instance.to_dict()
# create an instance of SearchExploreResponseDto from a dict
search_explore_response_dto_form_dict = search_explore_response_dto.from_dict(search_explore_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


