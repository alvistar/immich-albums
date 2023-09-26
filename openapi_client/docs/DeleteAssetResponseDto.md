# DeleteAssetResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | [**DeleteAssetStatus**](DeleteAssetStatus.md) |  | 

## Example

```python
from openapi_client.models.delete_asset_response_dto import DeleteAssetResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAssetResponseDto from a JSON string
delete_asset_response_dto_instance = DeleteAssetResponseDto.from_json(json)
# print the JSON string representation of the object
print DeleteAssetResponseDto.to_json()

# convert the object into a dict
delete_asset_response_dto_dict = delete_asset_response_dto_instance.to_dict()
# create an instance of DeleteAssetResponseDto from a dict
delete_asset_response_dto_form_dict = delete_asset_response_dto.from_dict(delete_asset_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


