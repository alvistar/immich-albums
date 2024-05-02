# JobStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_counts** | [**JobCountsDto**](JobCountsDto.md) |  | 
**queue_status** | [**QueueStatusDto**](QueueStatusDto.md) |  | 

## Example

```python
from openapi_client.models.job_status_dto import JobStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatusDto from a JSON string
job_status_dto_instance = JobStatusDto.from_json(json)
# print the JSON string representation of the object
print(JobStatusDto.to_json())

# convert the object into a dict
job_status_dto_dict = job_status_dto_instance.to_dict()
# create an instance of JobStatusDto from a dict
job_status_dto_from_dict = JobStatusDto.from_dict(job_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


