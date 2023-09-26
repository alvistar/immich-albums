# TimeBucketResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**time_bucket** | **str** |  | 

## Example

```python
from openapi_client.models.time_bucket_response_dto import TimeBucketResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of TimeBucketResponseDto from a JSON string
time_bucket_response_dto_instance = TimeBucketResponseDto.from_json(json)
# print the JSON string representation of the object
print TimeBucketResponseDto.to_json()

# convert the object into a dict
time_bucket_response_dto_dict = time_bucket_response_dto_instance.to_dict()
# create an instance of TimeBucketResponseDto from a dict
time_bucket_response_dto_form_dict = time_bucket_response_dto.from_dict(time_bucket_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


