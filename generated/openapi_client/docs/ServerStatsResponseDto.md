# ServerStatsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**photos** | **int** |  | [default to 0]
**usage** | **int** |  | [default to 0]
**usage_by_user** | [**List[UsageByUserDto]**](UsageByUserDto.md) |  | [default to []]
**videos** | **int** |  | [default to 0]

## Example

```python
from openapi_client.models.server_stats_response_dto import ServerStatsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServerStatsResponseDto from a JSON string
server_stats_response_dto_instance = ServerStatsResponseDto.from_json(json)
# print the JSON string representation of the object
print(ServerStatsResponseDto.to_json())

# convert the object into a dict
server_stats_response_dto_dict = server_stats_response_dto_instance.to_dict()
# create an instance of ServerStatsResponseDto from a dict
server_stats_response_dto_from_dict = ServerStatsResponseDto.from_dict(server_stats_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


