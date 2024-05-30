# PersonCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birth_date** | **date** | Person date of birth. Note: the mobile app cannot currently set the birth date to null. | [optional] 
**is_hidden** | **bool** | Person visibility | [optional] 
**name** | **str** | Person name. | [optional] 

## Example

```python
from openapi_client.models.person_create_dto import PersonCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PersonCreateDto from a JSON string
person_create_dto_instance = PersonCreateDto.from_json(json)
# print the JSON string representation of the object
print(PersonCreateDto.to_json())

# convert the object into a dict
person_create_dto_dict = person_create_dto_instance.to_dict()
# create an instance of PersonCreateDto from a dict
person_create_dto_from_dict = PersonCreateDto.from_dict(person_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


