# ValidateLibraryImportPathResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_path** | **str** |  | 
**is_valid** | **bool** |  | [default to False]
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.validate_library_import_path_response_dto import ValidateLibraryImportPathResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateLibraryImportPathResponseDto from a JSON string
validate_library_import_path_response_dto_instance = ValidateLibraryImportPathResponseDto.from_json(json)
# print the JSON string representation of the object
print(ValidateLibraryImportPathResponseDto.to_json())

# convert the object into a dict
validate_library_import_path_response_dto_dict = validate_library_import_path_response_dto_instance.to_dict()
# create an instance of ValidateLibraryImportPathResponseDto from a dict
validate_library_import_path_response_dto_from_dict = ValidateLibraryImportPathResponseDto.from_dict(validate_library_import_path_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


