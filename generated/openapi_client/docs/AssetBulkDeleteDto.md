# AssetBulkDeleteDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** |  | [optional] 
**ids** | **List[str]** |  | 

## Example

```python
from openapi_client.models.asset_bulk_delete_dto import AssetBulkDeleteDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetBulkDeleteDto from a JSON string
asset_bulk_delete_dto_instance = AssetBulkDeleteDto.from_json(json)
# print the JSON string representation of the object
print(AssetBulkDeleteDto.to_json())

# convert the object into a dict
asset_bulk_delete_dto_dict = asset_bulk_delete_dto_instance.to_dict()
# create an instance of AssetBulkDeleteDto from a dict
asset_bulk_delete_dto_from_dict = AssetBulkDeleteDto.from_dict(asset_bulk_delete_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


