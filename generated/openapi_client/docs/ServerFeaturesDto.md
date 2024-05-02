# ServerFeaturesDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_file** | **bool** |  | 
**facial_recognition** | **bool** |  | 
**map** | **bool** |  | 
**oauth** | **bool** |  | 
**oauth_auto_launch** | **bool** |  | 
**password_login** | **bool** |  | 
**reverse_geocoding** | **bool** |  | 
**search** | **bool** |  | 
**sidecar** | **bool** |  | 
**smart_search** | **bool** |  | 
**trash** | **bool** |  | 

## Example

```python
from openapi_client.models.server_features_dto import ServerFeaturesDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServerFeaturesDto from a JSON string
server_features_dto_instance = ServerFeaturesDto.from_json(json)
# print the JSON string representation of the object
print(ServerFeaturesDto.to_json())

# convert the object into a dict
server_features_dto_dict = server_features_dto_instance.to_dict()
# create an instance of ServerFeaturesDto from a dict
server_features_dto_from_dict = ServerFeaturesDto.from_dict(server_features_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


