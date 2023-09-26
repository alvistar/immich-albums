# LibraryStatsResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**photos** | **int** |  | [default to 0]
**total** | **int** |  | [default to 0]
**usage** | **int** |  | [default to 0]
**videos** | **int** |  | [default to 0]

## Example

```python
from openapi_client.models.library_stats_response_dto import LibraryStatsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryStatsResponseDto from a JSON string
library_stats_response_dto_instance = LibraryStatsResponseDto.from_json(json)
# print the JSON string representation of the object
print LibraryStatsResponseDto.to_json()

# convert the object into a dict
library_stats_response_dto_dict = library_stats_response_dto_instance.to_dict()
# create an instance of LibraryStatsResponseDto from a dict
library_stats_response_dto_form_dict = library_stats_response_dto.from_dict(library_stats_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


