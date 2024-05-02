# MemoryResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[AssetResponseDto]**](AssetResponseDto.md) |  | 
**created_at** | **datetime** |  | 
**data** | [**OnThisDayDto**](OnThisDayDto.md) |  | 
**deleted_at** | **datetime** |  | [optional] 
**id** | **str** |  | 
**is_saved** | **bool** |  | 
**memory_at** | **datetime** |  | 
**owner_id** | **str** |  | 
**seen_at** | **datetime** |  | [optional] 
**type** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.memory_response_dto import MemoryResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryResponseDto from a JSON string
memory_response_dto_instance = MemoryResponseDto.from_json(json)
# print the JSON string representation of the object
print(MemoryResponseDto.to_json())

# convert the object into a dict
memory_response_dto_dict = memory_response_dto_instance.to_dict()
# create an instance of MemoryResponseDto from a dict
memory_response_dto_from_dict = MemoryResponseDto.from_dict(memory_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


