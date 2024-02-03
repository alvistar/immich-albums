# PersonUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birth_date** | **date** | Person date of birth. Note: the mobile app cannot currently set the birth date to null. | [optional] 
**feature_face_asset_id** | **str** | Asset is used to get the feature face thumbnail. | [optional] 
**is_hidden** | **bool** | Person visibility | [optional] 
**name** | **str** | Person name. | [optional] 

## Example

```python
from openapi_client.models.person_update_dto import PersonUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PersonUpdateDto from a JSON string
person_update_dto_instance = PersonUpdateDto.from_json(json)
# print the JSON string representation of the object
print PersonUpdateDto.to_json()

# convert the object into a dict
person_update_dto_dict = person_update_dto_instance.to_dict()
# create an instance of PersonUpdateDto from a dict
person_update_dto_form_dict = person_update_dto.from_dict(person_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


