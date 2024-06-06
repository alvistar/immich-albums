# ReverseGeocodingStateResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_import_file_name** | **str** |  | 
**last_update** | **str** |  | 

## Example

```python
from openapi_client.models.reverse_geocoding_state_response_dto import ReverseGeocodingStateResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReverseGeocodingStateResponseDto from a JSON string
reverse_geocoding_state_response_dto_instance = ReverseGeocodingStateResponseDto.from_json(json)
# print the JSON string representation of the object
print(ReverseGeocodingStateResponseDto.to_json())

# convert the object into a dict
reverse_geocoding_state_response_dto_dict = reverse_geocoding_state_response_dto_instance.to_dict()
# create an instance of ReverseGeocodingStateResponseDto from a dict
reverse_geocoding_state_response_dto_from_dict = ReverseGeocodingStateResponseDto.from_dict(reverse_geocoding_state_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


