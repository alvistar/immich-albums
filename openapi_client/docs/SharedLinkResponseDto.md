# SharedLinkResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**album** | [**AlbumResponseDto**](AlbumResponseDto.md) |  | [optional] 
**allow_download** | **bool** |  | 
**allow_upload** | **bool** |  | 
**assets** | [**List[AssetResponseDto]**](AssetResponseDto.md) |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**expires_at** | **datetime** |  | 
**id** | **str** |  | 
**key** | **str** |  | 
**show_exif** | **bool** |  | 
**type** | [**SharedLinkType**](SharedLinkType.md) |  | 
**user_id** | **str** |  | 

## Example

```python
from openapi_client.models.shared_link_response_dto import SharedLinkResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SharedLinkResponseDto from a JSON string
shared_link_response_dto_instance = SharedLinkResponseDto.from_json(json)
# print the JSON string representation of the object
print SharedLinkResponseDto.to_json()

# convert the object into a dict
shared_link_response_dto_dict = shared_link_response_dto_instance.to_dict()
# create an instance of SharedLinkResponseDto from a dict
shared_link_response_dto_form_dict = shared_link_response_dto.from_dict(shared_link_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


