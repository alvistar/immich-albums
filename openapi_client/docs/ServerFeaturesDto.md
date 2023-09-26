# ServerFeaturesDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clip_encode** | **bool** |  | 
**config_file** | **bool** |  | 
**facial_recognition** | **bool** |  | 
**map** | **bool** |  | 
**oauth** | **bool** |  | 
**oauth_auto_launch** | **bool** |  | 
**password_login** | **bool** |  | 
**search** | **bool** |  | 
**sidecar** | **bool** |  | 
**tag_image** | **bool** |  | 

## Example

```python
from openapi_client.models.server_features_dto import ServerFeaturesDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServerFeaturesDto from a JSON string
server_features_dto_instance = ServerFeaturesDto.from_json(json)
# print the JSON string representation of the object
print ServerFeaturesDto.to_json()

# convert the object into a dict
server_features_dto_dict = server_features_dto_instance.to_dict()
# create an instance of ServerFeaturesDto from a dict
server_features_dto_form_dict = server_features_dto.from_dict(server_features_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


