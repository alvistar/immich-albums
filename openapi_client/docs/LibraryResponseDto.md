# LibraryResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_count** | **int** |  | 
**created_at** | **datetime** |  | 
**exclusion_patterns** | **List[str]** |  | 
**id** | **str** |  | 
**import_paths** | **List[str]** |  | 
**name** | **str** |  | 
**owner_id** | **str** |  | 
**refreshed_at** | **datetime** |  | 
**type** | [**LibraryType**](LibraryType.md) |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.library_response_dto import LibraryResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryResponseDto from a JSON string
library_response_dto_instance = LibraryResponseDto.from_json(json)
# print the JSON string representation of the object
print LibraryResponseDto.to_json()

# convert the object into a dict
library_response_dto_dict = library_response_dto_instance.to_dict()
# create an instance of LibraryResponseDto from a dict
library_response_dto_form_dict = library_response_dto.from_dict(library_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


