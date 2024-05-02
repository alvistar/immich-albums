# SmartInfoResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | **List[str]** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.smart_info_response_dto import SmartInfoResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SmartInfoResponseDto from a JSON string
smart_info_response_dto_instance = SmartInfoResponseDto.from_json(json)
# print the JSON string representation of the object
print(SmartInfoResponseDto.to_json())

# convert the object into a dict
smart_info_response_dto_dict = smart_info_response_dto_instance.to_dict()
# create an instance of SmartInfoResponseDto from a dict
smart_info_response_dto_from_dict = SmartInfoResponseDto.from_dict(smart_info_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


