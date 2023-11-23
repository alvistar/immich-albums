# FileReportDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extras** | **List[str]** |  | 
**orphans** | [**List[FileReportItemDto]**](FileReportItemDto.md) |  | 

## Example

```python
from openapi_client.models.file_report_dto import FileReportDto

# TODO update the JSON string below
json = "{}"
# create an instance of FileReportDto from a JSON string
file_report_dto_instance = FileReportDto.from_json(json)
# print the JSON string representation of the object
print FileReportDto.to_json()

# convert the object into a dict
file_report_dto_dict = file_report_dto_instance.to_dict()
# create an instance of FileReportDto from a dict
file_report_dto_form_dict = file_report_dto.from_dict(file_report_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


