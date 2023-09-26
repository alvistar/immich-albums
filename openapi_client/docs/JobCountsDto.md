# JobCountsDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **int** |  | 
**completed** | **int** |  | 
**delayed** | **int** |  | 
**failed** | **int** |  | 
**paused** | **int** |  | 
**waiting** | **int** |  | 

## Example

```python
from openapi_client.models.job_counts_dto import JobCountsDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobCountsDto from a JSON string
job_counts_dto_instance = JobCountsDto.from_json(json)
# print the JSON string representation of the object
print JobCountsDto.to_json()

# convert the object into a dict
job_counts_dto_dict = job_counts_dto_instance.to_dict()
# create an instance of JobCountsDto from a dict
job_counts_dto_form_dict = job_counts_dto.from_dict(job_counts_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


