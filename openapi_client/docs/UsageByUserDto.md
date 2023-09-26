# UsageByUserDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**photos** | **int** |  | 
**usage** | **int** |  | 
**user_first_name** | **str** |  | 
**user_id** | **str** |  | 
**user_last_name** | **str** |  | 
**videos** | **int** |  | 

## Example

```python
from openapi_client.models.usage_by_user_dto import UsageByUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of UsageByUserDto from a JSON string
usage_by_user_dto_instance = UsageByUserDto.from_json(json)
# print the JSON string representation of the object
print UsageByUserDto.to_json()

# convert the object into a dict
usage_by_user_dto_dict = usage_by_user_dto_instance.to_dict()
# create an instance of UsageByUserDto from a dict
usage_by_user_dto_form_dict = usage_by_user_dto.from_dict(usage_by_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


