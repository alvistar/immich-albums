# PartnerResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_color** | [**UserAvatarColor**](UserAvatarColor.md) |  | 
**created_at** | **datetime** |  | 
**deleted_at** | **datetime** |  | 
**email** | **str** |  | 
**id** | **str** |  | 
**in_timeline** | **bool** |  | [optional] 
**is_admin** | **bool** |  | 
**memories_enabled** | **bool** |  | [optional] 
**name** | **str** |  | 
**oauth_id** | **str** |  | 
**profile_image_path** | **str** |  | 
**quota_size_in_bytes** | **int** |  | 
**quota_usage_in_bytes** | **int** |  | 
**should_change_password** | **bool** |  | 
**status** | [**UserStatus**](UserStatus.md) |  | 
**storage_label** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.partner_response_dto import PartnerResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerResponseDto from a JSON string
partner_response_dto_instance = PartnerResponseDto.from_json(json)
# print the JSON string representation of the object
print(PartnerResponseDto.to_json())

# convert the object into a dict
partner_response_dto_dict = partner_response_dto_instance.to_dict()
# create an instance of PartnerResponseDto from a dict
partner_response_dto_from_dict = PartnerResponseDto.from_dict(partner_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


