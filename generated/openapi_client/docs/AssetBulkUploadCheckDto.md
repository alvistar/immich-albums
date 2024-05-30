# AssetBulkUploadCheckDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[AssetBulkUploadCheckItem]**](AssetBulkUploadCheckItem.md) |  | 

## Example

```python
from openapi_client.models.asset_bulk_upload_check_dto import AssetBulkUploadCheckDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetBulkUploadCheckDto from a JSON string
asset_bulk_upload_check_dto_instance = AssetBulkUploadCheckDto.from_json(json)
# print the JSON string representation of the object
print(AssetBulkUploadCheckDto.to_json())

# convert the object into a dict
asset_bulk_upload_check_dto_dict = asset_bulk_upload_check_dto_instance.to_dict()
# create an instance of AssetBulkUploadCheckDto from a dict
asset_bulk_upload_check_dto_from_dict = AssetBulkUploadCheckDto.from_dict(asset_bulk_upload_check_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


