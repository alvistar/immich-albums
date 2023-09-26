# UserCountResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_count** | **int** |  | 

## Example

```python
from openapi_client.models.user_count_response_dto import UserCountResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserCountResponseDto from a JSON string
user_count_response_dto_instance = UserCountResponseDto.from_json(json)
# print the JSON string representation of the object
print UserCountResponseDto.to_json()

# convert the object into a dict
user_count_response_dto_dict = user_count_response_dto_instance.to_dict()
# create an instance of UserCountResponseDto from a dict
user_count_response_dto_form_dict = user_count_response_dto.from_dict(user_count_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


