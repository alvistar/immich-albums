# SharedLinkCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**album_id** | **str** |  | [optional] 
**allow_download** | **bool** |  | [optional] [default to True]
**allow_upload** | **bool** |  | [optional] 
**asset_ids** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**password** | **str** |  | [optional] 
**show_metadata** | **bool** |  | [optional] [default to True]
**type** | [**SharedLinkType**](SharedLinkType.md) |  | 

## Example

```python
from openapi_client.models.shared_link_create_dto import SharedLinkCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SharedLinkCreateDto from a JSON string
shared_link_create_dto_instance = SharedLinkCreateDto.from_json(json)
# print the JSON string representation of the object
print(SharedLinkCreateDto.to_json())

# convert the object into a dict
shared_link_create_dto_dict = shared_link_create_dto_instance.to_dict()
# create an instance of SharedLinkCreateDto from a dict
shared_link_create_dto_from_dict = SharedLinkCreateDto.from_dict(shared_link_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


