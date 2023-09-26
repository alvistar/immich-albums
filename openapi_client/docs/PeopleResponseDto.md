# PeopleResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**people** | [**List[PersonResponseDto]**](PersonResponseDto.md) |  | 
**total** | **int** |  | 
**visible** | **int** |  | 

## Example

```python
from openapi_client.models.people_response_dto import PeopleResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleResponseDto from a JSON string
people_response_dto_instance = PeopleResponseDto.from_json(json)
# print the JSON string representation of the object
print PeopleResponseDto.to_json()

# convert the object into a dict
people_response_dto_dict = people_response_dto_instance.to_dict()
# create an instance of PeopleResponseDto from a dict
people_response_dto_form_dict = people_response_dto.from_dict(people_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


