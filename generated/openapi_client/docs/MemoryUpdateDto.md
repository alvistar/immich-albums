# MemoryUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_saved** | **bool** |  | [optional] 
**memory_at** | **datetime** |  | [optional] 
**seen_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.memory_update_dto import MemoryUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryUpdateDto from a JSON string
memory_update_dto_instance = MemoryUpdateDto.from_json(json)
# print the JSON string representation of the object
print(MemoryUpdateDto.to_json())

# convert the object into a dict
memory_update_dto_dict = memory_update_dto_instance.to_dict()
# create an instance of MemoryUpdateDto from a dict
memory_update_dto_from_dict = MemoryUpdateDto.from_dict(memory_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


