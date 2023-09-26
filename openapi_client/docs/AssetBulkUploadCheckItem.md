# AssetBulkUploadCheckItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checksum** | **str** | base64 or hex encoded sha1 hash | 
**id** | **str** |  | 

## Example

```python
from openapi_client.models.asset_bulk_upload_check_item import AssetBulkUploadCheckItem

# TODO update the JSON string below
json = "{}"
# create an instance of AssetBulkUploadCheckItem from a JSON string
asset_bulk_upload_check_item_instance = AssetBulkUploadCheckItem.from_json(json)
# print the JSON string representation of the object
print AssetBulkUploadCheckItem.to_json()

# convert the object into a dict
asset_bulk_upload_check_item_dict = asset_bulk_upload_check_item_instance.to_dict()
# create an instance of AssetBulkUploadCheckItem from a dict
asset_bulk_upload_check_item_form_dict = asset_bulk_upload_check_item.from_dict(asset_bulk_upload_check_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


