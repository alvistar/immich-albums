# UpdateStackParentDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_parent_id** | **str** |  | 
**old_parent_id** | **str** |  | 

## Example

```python
from openapi_client.models.update_stack_parent_dto import UpdateStackParentDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStackParentDto from a JSON string
update_stack_parent_dto_instance = UpdateStackParentDto.from_json(json)
# print the JSON string representation of the object
print UpdateStackParentDto.to_json()

# convert the object into a dict
update_stack_parent_dto_dict = update_stack_parent_dto_instance.to_dict()
# create an instance of UpdateStackParentDto from a dict
update_stack_parent_dto_form_dict = update_stack_parent_dto.from_dict(update_stack_parent_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


