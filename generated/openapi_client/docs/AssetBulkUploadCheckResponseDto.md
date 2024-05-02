# AssetBulkUploadCheckResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AssetBulkUploadCheckResult]**](AssetBulkUploadCheckResult.md) |  | 

## Example

```python
from openapi_client.models.asset_bulk_upload_check_response_dto import AssetBulkUploadCheckResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetBulkUploadCheckResponseDto from a JSON string
asset_bulk_upload_check_response_dto_instance = AssetBulkUploadCheckResponseDto.from_json(json)
# print the JSON string representation of the object
print(AssetBulkUploadCheckResponseDto.to_json())

# convert the object into a dict
asset_bulk_upload_check_response_dto_dict = asset_bulk_upload_check_response_dto_instance.to_dict()
# create an instance of AssetBulkUploadCheckResponseDto from a dict
asset_bulk_upload_check_response_dto_from_dict = AssetBulkUploadCheckResponseDto.from_dict(asset_bulk_upload_check_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


