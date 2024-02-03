# AllJobStatusResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_task** | [**JobStatusDto**](JobStatusDto.md) |  | 
**face_detection** | [**JobStatusDto**](JobStatusDto.md) |  | 
**facial_recognition** | [**JobStatusDto**](JobStatusDto.md) |  | 
**library** | [**JobStatusDto**](JobStatusDto.md) |  | 
**metadata_extraction** | [**JobStatusDto**](JobStatusDto.md) |  | 
**migration** | [**JobStatusDto**](JobStatusDto.md) |  | 
**search** | [**JobStatusDto**](JobStatusDto.md) |  | 
**sidecar** | [**JobStatusDto**](JobStatusDto.md) |  | 
**smart_search** | [**JobStatusDto**](JobStatusDto.md) |  | 
**storage_template_migration** | [**JobStatusDto**](JobStatusDto.md) |  | 
**thumbnail_generation** | [**JobStatusDto**](JobStatusDto.md) |  | 
**video_conversion** | [**JobStatusDto**](JobStatusDto.md) |  | 

## Example

```python
from openapi_client.models.all_job_status_response_dto import AllJobStatusResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AllJobStatusResponseDto from a JSON string
all_job_status_response_dto_instance = AllJobStatusResponseDto.from_json(json)
# print the JSON string representation of the object
print AllJobStatusResponseDto.to_json()

# convert the object into a dict
all_job_status_response_dto_dict = all_job_status_response_dto_instance.to_dict()
# create an instance of AllJobStatusResponseDto from a dict
all_job_status_response_dto_form_dict = all_job_status_response_dto.from_dict(all_job_status_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


