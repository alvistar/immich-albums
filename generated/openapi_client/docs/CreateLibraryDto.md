# CreateLibraryDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusion_patterns** | **List[str]** |  | [optional] 
**import_paths** | **List[str]** |  | [optional] 
**is_visible** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**LibraryType**](LibraryType.md) |  | 

## Example

```python
from openapi_client.models.create_library_dto import CreateLibraryDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLibraryDto from a JSON string
create_library_dto_instance = CreateLibraryDto.from_json(json)
# print the JSON string representation of the object
print CreateLibraryDto.to_json()

# convert the object into a dict
create_library_dto_dict = create_library_dto_instance.to_dict()
# create an instance of CreateLibraryDto from a dict
create_library_dto_form_dict = create_library_dto.from_dict(create_library_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


