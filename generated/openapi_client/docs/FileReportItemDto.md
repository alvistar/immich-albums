# FileReportItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checksum** | **str** |  | [optional] 
**entity_id** | **str** |  | 
**entity_type** | [**PathEntityType**](PathEntityType.md) |  | 
**path_type** | [**PathType**](PathType.md) |  | 
**path_value** | **str** |  | 

## Example

```python
from openapi_client.models.file_report_item_dto import FileReportItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of FileReportItemDto from a JSON string
file_report_item_dto_instance = FileReportItemDto.from_json(json)
# print the JSON string representation of the object
print FileReportItemDto.to_json()

# convert the object into a dict
file_report_item_dto_dict = file_report_item_dto_instance.to_dict()
# create an instance of FileReportItemDto from a dict
file_report_item_dto_form_dict = file_report_item_dto.from_dict(file_report_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


