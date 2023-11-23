# AuthDeviceResponseDto


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
from openapi_client.models.auth_device_response_dto import AuthDeviceResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthDeviceResponseDto from a JSON string
auth_device_response_dto_instance = AuthDeviceResponseDto.from_json(json)
# print the JSON string representation of the object
print AuthDeviceResponseDto.to_json()

# convert the object into a dict
auth_device_response_dto_dict = auth_device_response_dto_instance.to_dict()
# create an instance of AuthDeviceResponseDto from a dict
auth_device_response_dto_form_dict = auth_device_response_dto.from_dict(auth_device_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


