# CheckExistingAssetsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_asset_ids** | **List[str]** |  | 
**device_id** | **str** |  | 

## Example

```python
from openapi_client.models.check_existing_assets_dto import CheckExistingAssetsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CheckExistingAssetsDto from a JSON string
check_existing_assets_dto_instance = CheckExistingAssetsDto.from_json(json)
# print the JSON string representation of the object
print(CheckExistingAssetsDto.to_json())

# convert the object into a dict
check_existing_assets_dto_dict = check_existing_assets_dto_instance.to_dict()
# create an instance of CheckExistingAssetsDto from a dict
check_existing_assets_dto_from_dict = CheckExistingAssetsDto.from_dict(check_existing_assets_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


