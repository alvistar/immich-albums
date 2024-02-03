# CreateProfileImageResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_image_path** | **str** |  | 
**user_id** | **str** |  | 

## Example

```python
from openapi_client.models.create_profile_image_response_dto import CreateProfileImageResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProfileImageResponseDto from a JSON string
create_profile_image_response_dto_instance = CreateProfileImageResponseDto.from_json(json)
# print the JSON string representation of the object
print CreateProfileImageResponseDto.to_json()

# convert the object into a dict
create_profile_image_response_dto_dict = create_profile_image_response_dto_instance.to_dict()
# create an instance of CreateProfileImageResponseDto from a dict
create_profile_image_response_dto_form_dict = create_profile_image_response_dto.from_dict(create_profile_image_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


