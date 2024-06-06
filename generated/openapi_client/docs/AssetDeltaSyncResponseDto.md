# AssetDeltaSyncResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **List[str]** |  | 
**needs_full_sync** | **bool** |  | 
**upserted** | [**List[AssetResponseDto]**](AssetResponseDto.md) |  | 

## Example

```python
from openapi_client.models.asset_delta_sync_response_dto import AssetDeltaSyncResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetDeltaSyncResponseDto from a JSON string
asset_delta_sync_response_dto_instance = AssetDeltaSyncResponseDto.from_json(json)
# print the JSON string representation of the object
print(AssetDeltaSyncResponseDto.to_json())

# convert the object into a dict
asset_delta_sync_response_dto_dict = asset_delta_sync_response_dto_instance.to_dict()
# create an instance of AssetDeltaSyncResponseDto from a dict
asset_delta_sync_response_dto_from_dict = AssetDeltaSyncResponseDto.from_dict(asset_delta_sync_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


