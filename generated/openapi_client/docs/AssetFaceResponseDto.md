# AssetFaceResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounding_box_x1** | **int** |  | 
**bounding_box_x2** | **int** |  | 
**bounding_box_y1** | **int** |  | 
**bounding_box_y2** | **int** |  | 
**id** | **str** |  | 
**image_height** | **int** |  | 
**image_width** | **int** |  | 
**person** | [**PersonResponseDto**](PersonResponseDto.md) |  | 

## Example

```python
from openapi_client.models.asset_face_response_dto import AssetFaceResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFaceResponseDto from a JSON string
asset_face_response_dto_instance = AssetFaceResponseDto.from_json(json)
# print the JSON string representation of the object
print AssetFaceResponseDto.to_json()

# convert the object into a dict
asset_face_response_dto_dict = asset_face_response_dto_instance.to_dict()
# create an instance of AssetFaceResponseDto from a dict
asset_face_response_dto_form_dict = asset_face_response_dto.from_dict(asset_face_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


