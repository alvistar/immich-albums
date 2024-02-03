# SystemConfigThumbnailDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**colorspace** | [**Colorspace**](Colorspace.md) |  | 
**jpeg_size** | **int** |  | 
**quality** | **int** |  | 
**webp_size** | **int** |  | 

## Example

```python
from openapi_client.models.system_config_thumbnail_dto import SystemConfigThumbnailDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigThumbnailDto from a JSON string
system_config_thumbnail_dto_instance = SystemConfigThumbnailDto.from_json(json)
# print the JSON string representation of the object
print SystemConfigThumbnailDto.to_json()

# convert the object into a dict
system_config_thumbnail_dto_dict = system_config_thumbnail_dto_instance.to_dict()
# create an instance of SystemConfigThumbnailDto from a dict
system_config_thumbnail_dto_form_dict = system_config_thumbnail_dto.from_dict(system_config_thumbnail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


