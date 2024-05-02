# ValidateLibraryResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_paths** | [**List[ValidateLibraryImportPathResponseDto]**](ValidateLibraryImportPathResponseDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.validate_library_response_dto import ValidateLibraryResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateLibraryResponseDto from a JSON string
validate_library_response_dto_instance = ValidateLibraryResponseDto.from_json(json)
# print the JSON string representation of the object
print(ValidateLibraryResponseDto.to_json())

# convert the object into a dict
validate_library_response_dto_dict = validate_library_response_dto_instance.to_dict()
# create an instance of ValidateLibraryResponseDto from a dict
validate_library_response_dto_from_dict = ValidateLibraryResponseDto.from_dict(validate_library_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


