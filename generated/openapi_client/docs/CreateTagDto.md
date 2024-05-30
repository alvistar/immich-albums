# CreateTagDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**TagTypeEnum**](TagTypeEnum.md) |  | 

## Example

```python
from openapi_client.models.create_tag_dto import CreateTagDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTagDto from a JSON string
create_tag_dto_instance = CreateTagDto.from_json(json)
# print the JSON string representation of the object
print(CreateTagDto.to_json())

# convert the object into a dict
create_tag_dto_dict = create_tag_dto_instance.to_dict()
# create an instance of CreateTagDto from a dict
create_tag_dto_from_dict = CreateTagDto.from_dict(create_tag_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


