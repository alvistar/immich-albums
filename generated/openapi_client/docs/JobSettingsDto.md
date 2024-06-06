# JobSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concurrency** | **int** |  | 

## Example

```python
from openapi_client.models.job_settings_dto import JobSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobSettingsDto from a JSON string
job_settings_dto_instance = JobSettingsDto.from_json(json)
# print the JSON string representation of the object
print(JobSettingsDto.to_json())

# convert the object into a dict
job_settings_dto_dict = job_settings_dto_instance.to_dict()
# create an instance of JobSettingsDto from a dict
job_settings_dto_from_dict = JobSettingsDto.from_dict(job_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


