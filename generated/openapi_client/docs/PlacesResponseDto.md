# PlacesResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin1name** | **str** |  | [optional] 
**admin2name** | **str** |  | [optional] 
**latitude** | **float** |  | 
**longitude** | **float** |  | 
**name** | **str** |  | 

## Example

```python
from openapi_client.models.places_response_dto import PlacesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlacesResponseDto from a JSON string
places_response_dto_instance = PlacesResponseDto.from_json(json)
# print the JSON string representation of the object
print(PlacesResponseDto.to_json())

# convert the object into a dict
places_response_dto_dict = places_response_dto_instance.to_dict()
# create an instance of PlacesResponseDto from a dict
places_response_dto_from_dict = PlacesResponseDto.from_dict(places_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


