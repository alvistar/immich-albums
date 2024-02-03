# LogoutResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_uri** | **str** |  | 
**successful** | **bool** |  | 

## Example

```python
from openapi_client.models.logout_response_dto import LogoutResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of LogoutResponseDto from a JSON string
logout_response_dto_instance = LogoutResponseDto.from_json(json)
# print the JSON string representation of the object
print LogoutResponseDto.to_json()

# convert the object into a dict
logout_response_dto_dict = logout_response_dto_instance.to_dict()
# create an instance of LogoutResponseDto from a dict
logout_response_dto_form_dict = logout_response_dto.from_dict(logout_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


