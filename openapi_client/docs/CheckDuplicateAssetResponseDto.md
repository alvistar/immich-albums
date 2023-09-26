# CheckDuplicateAssetResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**is_exist** | **bool** |  | 

## Example

```python
from openapi_client.models.check_duplicate_asset_response_dto import CheckDuplicateAssetResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDuplicateAssetResponseDto from a JSON string
check_duplicate_asset_response_dto_instance = CheckDuplicateAssetResponseDto.from_json(json)
# print the JSON string representation of the object
print CheckDuplicateAssetResponseDto.to_json()

# convert the object into a dict
check_duplicate_asset_response_dto_dict = check_duplicate_asset_response_dto_instance.to_dict()
# create an instance of CheckDuplicateAssetResponseDto from a dict
check_duplicate_asset_response_dto_form_dict = check_duplicate_asset_response_dto.from_dict(check_duplicate_asset_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


