# AssetDeltaSyncDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_after** | **datetime** |  | 
**user_ids** | **List[str]** |  | 

## Example

```python
from openapi_client.models.asset_delta_sync_dto import AssetDeltaSyncDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetDeltaSyncDto from a JSON string
asset_delta_sync_dto_instance = AssetDeltaSyncDto.from_json(json)
# print the JSON string representation of the object
print(AssetDeltaSyncDto.to_json())

# convert the object into a dict
asset_delta_sync_dto_dict = asset_delta_sync_dto_instance.to_dict()
# create an instance of AssetDeltaSyncDto from a dict
asset_delta_sync_dto_from_dict = AssetDeltaSyncDto.from_dict(asset_delta_sync_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


