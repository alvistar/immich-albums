# AssetBulkUploadCheckResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**asset_id** | **str** |  | [optional] 
**id** | **str** |  | 
**reason** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.asset_bulk_upload_check_result import AssetBulkUploadCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of AssetBulkUploadCheckResult from a JSON string
asset_bulk_upload_check_result_instance = AssetBulkUploadCheckResult.from_json(json)
# print the JSON string representation of the object
print AssetBulkUploadCheckResult.to_json()

# convert the object into a dict
asset_bulk_upload_check_result_dict = asset_bulk_upload_check_result_instance.to_dict()
# create an instance of AssetBulkUploadCheckResult from a dict
asset_bulk_upload_check_result_form_dict = asset_bulk_upload_check_result.from_dict(asset_bulk_upload_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


