# JobCommandDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | [**JobCommand**](JobCommand.md) |  | 
**force** | **bool** |  | 

## Example

```python
from openapi_client.models.job_command_dto import JobCommandDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobCommandDto from a JSON string
job_command_dto_instance = JobCommandDto.from_json(json)
# print the JSON string representation of the object
print JobCommandDto.to_json()

# convert the object into a dict
job_command_dto_dict = job_command_dto_instance.to_dict()
# create an instance of JobCommandDto from a dict
job_command_dto_form_dict = job_command_dto.from_dict(job_command_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


