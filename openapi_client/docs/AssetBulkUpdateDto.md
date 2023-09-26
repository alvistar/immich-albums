# AssetBulkUpdateDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | 
**is_archived** | **bool** |  | [optional] 
**is_favorite** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.asset_bulk_update_dto import AssetBulkUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetBulkUpdateDto from a JSON string
asset_bulk_update_dto_instance = AssetBulkUpdateDto.from_json(json)
# print the JSON string representation of the object
print AssetBulkUpdateDto.to_json()

# convert the object into a dict
asset_bulk_update_dto_dict = asset_bulk_update_dto_instance.to_dict()
# create an instance of AssetBulkUpdateDto from a dict
asset_bulk_update_dto_form_dict = asset_bulk_update_dto.from_dict(asset_bulk_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


