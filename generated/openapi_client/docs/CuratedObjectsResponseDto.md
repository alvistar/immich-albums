# CuratedObjectsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_asset_id** | **str** |  | 
**device_id** | **str** |  | 
**id** | **str** |  | 
**object** | **str** |  | 
**resize_path** | **str** |  | 

## Example

```python
from openapi_client.models.curated_objects_response_dto import CuratedObjectsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CuratedObjectsResponseDto from a JSON string
curated_objects_response_dto_instance = CuratedObjectsResponseDto.from_json(json)
# print the JSON string representation of the object
print CuratedObjectsResponseDto.to_json()

# convert the object into a dict
curated_objects_response_dto_dict = curated_objects_response_dto_instance.to_dict()
# create an instance of CuratedObjectsResponseDto from a dict
curated_objects_response_dto_form_dict = curated_objects_response_dto.from_dict(curated_objects_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


