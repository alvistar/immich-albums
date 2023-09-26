# TagResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | [**TagTypeEnum**](TagTypeEnum.md) |  | 
**user_id** | **str** |  | 

## Example

```python
from openapi_client.models.tag_response_dto import TagResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of TagResponseDto from a JSON string
tag_response_dto_instance = TagResponseDto.from_json(json)
# print the JSON string representation of the object
print TagResponseDto.to_json()

# convert the object into a dict
tag_response_dto_dict = tag_response_dto_instance.to_dict()
# create an instance of TagResponseDto from a dict
tag_response_dto_form_dict = tag_response_dto.from_dict(tag_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


