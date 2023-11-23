# ActivityCreateDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**album_id** | **str** |  | 
**asset_id** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**type** | [**ReactionType**](ReactionType.md) |  | 

## Example

```python
from openapi_client.models.activity_create_dto import ActivityCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityCreateDto from a JSON string
activity_create_dto_instance = ActivityCreateDto.from_json(json)
# print the JSON string representation of the object
print ActivityCreateDto.to_json()

# convert the object into a dict
activity_create_dto_dict = activity_create_dto_instance.to_dict()
# create an instance of ActivityCreateDto from a dict
activity_create_dto_form_dict = activity_create_dto.from_dict(activity_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


