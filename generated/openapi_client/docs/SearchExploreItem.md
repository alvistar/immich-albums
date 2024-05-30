# SearchExploreItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AssetResponseDto**](AssetResponseDto.md) |  | 
**value** | **str** |  | 

## Example

```python
from openapi_client.models.search_explore_item import SearchExploreItem

# TODO update the JSON string below
json = "{}"
# create an instance of SearchExploreItem from a JSON string
search_explore_item_instance = SearchExploreItem.from_json(json)
# print the JSON string representation of the object
print(SearchExploreItem.to_json())

# convert the object into a dict
search_explore_item_dict = search_explore_item_instance.to_dict()
# create an instance of SearchExploreItem from a dict
search_explore_item_from_dict = SearchExploreItem.from_dict(search_explore_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


