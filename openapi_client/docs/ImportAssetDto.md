# ImportAssetDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_path** | **str** |  | 
**device_asset_id** | **str** |  | 
**device_id** | **str** |  | 
**duration** | **str** |  | [optional] 
**file_created_at** | **datetime** |  | 
**file_modified_at** | **datetime** |  | 
**is_archived** | **bool** |  | [optional] 
**is_external** | **bool** |  | [optional] 
**is_favorite** | **bool** |  | 
**is_offline** | **bool** |  | [optional] 
**is_read_only** | **bool** |  | [optional] [default to True]
**is_visible** | **bool** |  | [optional] 
**library_id** | **str** |  | [optional] 
**sidecar_path** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.import_asset_dto import ImportAssetDto

# TODO update the JSON string below
json = "{}"
# create an instance of ImportAssetDto from a JSON string
import_asset_dto_instance = ImportAssetDto.from_json(json)
# print the JSON string representation of the object
print ImportAssetDto.to_json()

# convert the object into a dict
import_asset_dto_dict = import_asset_dto_instance.to_dict()
# create an instance of ImportAssetDto from a dict
import_asset_dto_form_dict = import_asset_dto.from_dict(import_asset_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


