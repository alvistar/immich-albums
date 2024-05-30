# FileChecksumResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checksum** | **str** |  | 
**filename** | **str** |  | 

## Example

```python
from openapi_client.models.file_checksum_response_dto import FileChecksumResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of FileChecksumResponseDto from a JSON string
file_checksum_response_dto_instance = FileChecksumResponseDto.from_json(json)
# print the JSON string representation of the object
print(FileChecksumResponseDto.to_json())

# convert the object into a dict
file_checksum_response_dto_dict = file_checksum_response_dto_instance.to_dict()
# create an instance of FileChecksumResponseDto from a dict
file_checksum_response_dto_from_dict = FileChecksumResponseDto.from_dict(file_checksum_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


