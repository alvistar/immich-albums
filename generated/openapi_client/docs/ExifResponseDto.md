# ExifResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**date_time_original** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**exif_image_height** | **float** |  | [optional] 
**exif_image_width** | **float** |  | [optional] 
**exposure_time** | **str** |  | [optional] 
**f_number** | **float** |  | [optional] 
**file_size_in_byte** | **int** |  | [optional] 
**focal_length** | **float** |  | [optional] 
**iso** | **float** |  | [optional] 
**latitude** | **float** |  | [optional] 
**lens_model** | **str** |  | [optional] 
**longitude** | **float** |  | [optional] 
**make** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**modify_date** | **datetime** |  | [optional] 
**orientation** | **str** |  | [optional] 
**projection_type** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.exif_response_dto import ExifResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExifResponseDto from a JSON string
exif_response_dto_instance = ExifResponseDto.from_json(json)
# print the JSON string representation of the object
print ExifResponseDto.to_json()

# convert the object into a dict
exif_response_dto_dict = exif_response_dto_instance.to_dict()
# create an instance of ExifResponseDto from a dict
exif_response_dto_form_dict = exif_response_dto.from_dict(exif_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


