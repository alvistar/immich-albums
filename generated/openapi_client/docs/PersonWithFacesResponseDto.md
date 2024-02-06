# PersonWithFacesResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birth_date** | **date** |  | 
**faces** | [**List[AssetFaceWithoutPersonResponseDto]**](AssetFaceWithoutPersonResponseDto.md) |  | 
**id** | **str** |  | 
**is_hidden** | **bool** |  | 
**name** | **str** |  | 
**thumbnail_path** | **str** |  | 

## Example

```python
from openapi_client.models.person_with_faces_response_dto import PersonWithFacesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PersonWithFacesResponseDto from a JSON string
person_with_faces_response_dto_instance = PersonWithFacesResponseDto.from_json(json)
# print the JSON string representation of the object
print PersonWithFacesResponseDto.to_json()

# convert the object into a dict
person_with_faces_response_dto_dict = person_with_faces_response_dto_instance.to_dict()
# create an instance of PersonWithFacesResponseDto from a dict
person_with_faces_response_dto_form_dict = person_with_faces_response_dto.from_dict(person_with_faces_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


