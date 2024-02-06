# AssetFaceUpdateDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AssetFaceUpdateItem]**](AssetFaceUpdateItem.md) |  | 

## Example

```python
from openapi_client.models.asset_face_update_dto import AssetFaceUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFaceUpdateDto from a JSON string
asset_face_update_dto_instance = AssetFaceUpdateDto.from_json(json)
# print the JSON string representation of the object
print AssetFaceUpdateDto.to_json()

# convert the object into a dict
asset_face_update_dto_dict = asset_face_update_dto_instance.to_dict()
# create an instance of AssetFaceUpdateDto from a dict
asset_face_update_dto_form_dict = asset_face_update_dto.from_dict(asset_face_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


