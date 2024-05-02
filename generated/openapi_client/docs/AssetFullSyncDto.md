# AssetFullSyncDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_creation_date** | **datetime** |  | [optional] 
**last_id** | **str** |  | [optional] 
**limit** | **int** |  | 
**updated_until** | **datetime** |  | 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.asset_full_sync_dto import AssetFullSyncDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFullSyncDto from a JSON string
asset_full_sync_dto_instance = AssetFullSyncDto.from_json(json)
# print the JSON string representation of the object
print(AssetFullSyncDto.to_json())

# convert the object into a dict
asset_full_sync_dto_dict = asset_full_sync_dto_instance.to_dict()
# create an instance of AssetFullSyncDto from a dict
asset_full_sync_dto_from_dict = AssetFullSyncDto.from_dict(asset_full_sync_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


