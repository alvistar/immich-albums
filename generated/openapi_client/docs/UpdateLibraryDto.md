# UpdateLibraryDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusion_patterns** | **List[str]** |  | [optional] 
**import_paths** | **List[str]** |  | [optional] 
**is_visible** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.update_library_dto import UpdateLibraryDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLibraryDto from a JSON string
update_library_dto_instance = UpdateLibraryDto.from_json(json)
# print the JSON string representation of the object
print UpdateLibraryDto.to_json()

# convert the object into a dict
update_library_dto_dict = update_library_dto_instance.to_dict()
# create an instance of UpdateLibraryDto from a dict
update_library_dto_form_dict = update_library_dto.from_dict(update_library_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


