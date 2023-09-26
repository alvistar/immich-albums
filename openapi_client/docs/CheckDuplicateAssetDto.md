# CheckDuplicateAssetDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_asset_id** | **str** |  | 
**device_id** | **str** |  | 

## Example

```python
from openapi_client.models.check_duplicate_asset_dto import CheckDuplicateAssetDto

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDuplicateAssetDto from a JSON string
check_duplicate_asset_dto_instance = CheckDuplicateAssetDto.from_json(json)
# print the JSON string representation of the object
print CheckDuplicateAssetDto.to_json()

# convert the object into a dict
check_duplicate_asset_dto_dict = check_duplicate_asset_dto_instance.to_dict()
# create an instance of CheckDuplicateAssetDto from a dict
check_duplicate_asset_dto_form_dict = check_duplicate_asset_dto.from_dict(check_duplicate_asset_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


