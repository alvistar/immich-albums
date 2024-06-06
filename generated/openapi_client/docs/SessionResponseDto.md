# SessionResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | 
**current** | **bool** |  | 
**device_os** | **str** |  | 
**device_type** | **str** |  | 
**id** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from openapi_client.models.session_response_dto import SessionResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SessionResponseDto from a JSON string
session_response_dto_instance = SessionResponseDto.from_json(json)
# print the JSON string representation of the object
print(SessionResponseDto.to_json())

# convert the object into a dict
session_response_dto_dict = session_response_dto_instance.to_dict()
# create an instance of SessionResponseDto from a dict
session_response_dto_from_dict = SessionResponseDto.from_dict(session_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


