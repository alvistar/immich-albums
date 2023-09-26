# AssetResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checksum** | **str** | base64 encoded sha1 hash | 
**device_asset_id** | **str** |  | 
**device_id** | **str** |  | 
**duration** | **str** |  | 
**exif_info** | [**ExifResponseDto**](ExifResponseDto.md) |  | [optional] 
**file_created_at** | **datetime** |  | 
**file_modified_at** | **datetime** |  | 
**id** | **str** |  | 
**is_archived** | **bool** |  | 
**is_external** | **bool** |  | 
**is_favorite** | **bool** |  | 
**is_offline** | **bool** |  | 
**is_read_only** | **bool** |  | 
**library_id** | **str** |  | 
**live_photo_video_id** | **str** |  | [optional] 
**original_file_name** | **str** |  | 
**original_path** | **str** |  | 
**owner** | [**UserResponseDto**](UserResponseDto.md) |  | [optional] 
**owner_id** | **str** |  | 
**people** | [**List[PersonResponseDto]**](PersonResponseDto.md) |  | [optional] 
**resized** | **bool** |  | 
**smart_info** | [**SmartInfoResponseDto**](SmartInfoResponseDto.md) |  | [optional] 
**tags** | [**List[TagResponseDto]**](TagResponseDto.md) |  | [optional] 
**thumbhash** | **str** | base64 encoded thumbhash | 
**type** | [**AssetTypeEnum**](AssetTypeEnum.md) |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.asset_response_dto import AssetResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetResponseDto from a JSON string
asset_response_dto_instance = AssetResponseDto.from_json(json)
# print the JSON string representation of the object
print AssetResponseDto.to_json()

# convert the object into a dict
asset_response_dto_dict = asset_response_dto_instance.to_dict()
# create an instance of AssetResponseDto from a dict
asset_response_dto_form_dict = asset_response_dto.from_dict(asset_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


