# AssetJobsDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_ids** | **List[str]** |  | 
**name** | [**AssetJobName**](AssetJobName.md) |  | 

## Example

```python
from openapi_client.models.asset_jobs_dto import AssetJobsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetJobsDto from a JSON string
asset_jobs_dto_instance = AssetJobsDto.from_json(json)
# print the JSON string representation of the object
print AssetJobsDto.to_json()

# convert the object into a dict
asset_jobs_dto_dict = asset_jobs_dto_instance.to_dict()
# create an instance of AssetJobsDto from a dict
asset_jobs_dto_form_dict = asset_jobs_dto.from_dict(asset_jobs_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


