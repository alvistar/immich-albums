# SearchFacetCountResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**value** | **str** |  | 

## Example

```python
from openapi_client.models.search_facet_count_response_dto import SearchFacetCountResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFacetCountResponseDto from a JSON string
search_facet_count_response_dto_instance = SearchFacetCountResponseDto.from_json(json)
# print the JSON string representation of the object
print SearchFacetCountResponseDto.to_json()

# convert the object into a dict
search_facet_count_response_dto_dict = search_facet_count_response_dto_instance.to_dict()
# create an instance of SearchFacetCountResponseDto from a dict
search_facet_count_response_dto_form_dict = search_facet_count_response_dto.from_dict(search_facet_count_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


