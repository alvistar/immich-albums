# ScanLibraryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_all_files** | **bool** |  | [optional] 
**refresh_modified_files** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.scan_library_dto import ScanLibraryDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScanLibraryDto from a JSON string
scan_library_dto_instance = ScanLibraryDto.from_json(json)
# print the JSON string representation of the object
print(ScanLibraryDto.to_json())

# convert the object into a dict
scan_library_dto_dict = scan_library_dto_instance.to_dict()
# create an instance of ScanLibraryDto from a dict
scan_library_dto_from_dict = ScanLibraryDto.from_dict(scan_library_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


