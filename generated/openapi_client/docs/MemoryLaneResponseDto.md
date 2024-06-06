# MemoryLaneResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[AssetResponseDto]**](AssetResponseDto.md) |  | 
**title** | **str** | This property was deprecated in v1.100.0 | 
**years_ago** | **int** |  | 

## Example

```python
from openapi_client.models.memory_lane_response_dto import MemoryLaneResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryLaneResponseDto from a JSON string
memory_lane_response_dto_instance = MemoryLaneResponseDto.from_json(json)
# print the JSON string representation of the object
print(MemoryLaneResponseDto.to_json())

# convert the object into a dict
memory_lane_response_dto_dict = memory_lane_response_dto_instance.to_dict()
# create an instance of MemoryLaneResponseDto from a dict
memory_lane_response_dto_from_dict = MemoryLaneResponseDto.from_dict(memory_lane_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


