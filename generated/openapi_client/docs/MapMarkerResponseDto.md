# MapMarkerResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**lat** | **float** |  | 
**lon** | **float** |  | 

## Example

```python
from openapi_client.models.map_marker_response_dto import MapMarkerResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of MapMarkerResponseDto from a JSON string
map_marker_response_dto_instance = MapMarkerResponseDto.from_json(json)
# print the JSON string representation of the object
print MapMarkerResponseDto.to_json()

# convert the object into a dict
map_marker_response_dto_dict = map_marker_response_dto_instance.to_dict()
# create an instance of MapMarkerResponseDto from a dict
map_marker_response_dto_form_dict = map_marker_response_dto.from_dict(map_marker_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


