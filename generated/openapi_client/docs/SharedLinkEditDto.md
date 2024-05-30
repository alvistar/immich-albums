# SharedLinkEditDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_download** | **bool** |  | [optional] 
**allow_upload** | **bool** |  | [optional] 
**change_expiry_time** | **bool** | Few clients cannot send null to set the expiryTime to never. Setting this flag and not sending expiryAt is considered as null instead. Clients that can send null values can ignore this. | [optional] 
**description** | **str** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**password** | **str** |  | [optional] 
**show_metadata** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.shared_link_edit_dto import SharedLinkEditDto

# TODO update the JSON string below
json = "{}"
# create an instance of SharedLinkEditDto from a JSON string
shared_link_edit_dto_instance = SharedLinkEditDto.from_json(json)
# print the JSON string representation of the object
print(SharedLinkEditDto.to_json())

# convert the object into a dict
shared_link_edit_dto_dict = shared_link_edit_dto_instance.to_dict()
# create an instance of SharedLinkEditDto from a dict
shared_link_edit_dto_from_dict = SharedLinkEditDto.from_dict(shared_link_edit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


