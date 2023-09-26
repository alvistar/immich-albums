# PeopleUpdateDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**people** | [**List[PeopleUpdateItem]**](PeopleUpdateItem.md) |  | 

## Example

```python
from openapi_client.models.people_update_dto import PeopleUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleUpdateDto from a JSON string
people_update_dto_instance = PeopleUpdateDto.from_json(json)
# print the JSON string representation of the object
print PeopleUpdateDto.to_json()

# convert the object into a dict
people_update_dto_dict = people_update_dto_instance.to_dict()
# create an instance of PeopleUpdateDto from a dict
people_update_dto_form_dict = people_update_dto.from_dict(people_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


