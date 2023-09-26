# PersonResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birth_date** | **date** |  | 
**id** | **str** |  | 
**is_hidden** | **bool** |  | 
**name** | **str** |  | 
**thumbnail_path** | **str** |  | 

## Example

```python
from openapi_client.models.person_response_dto import PersonResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PersonResponseDto from a JSON string
person_response_dto_instance = PersonResponseDto.from_json(json)
# print the JSON string representation of the object
print PersonResponseDto.to_json()

# convert the object into a dict
person_response_dto_dict = person_response_dto_instance.to_dict()
# create an instance of PersonResponseDto from a dict
person_response_dto_form_dict = person_response_dto.from_dict(person_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


