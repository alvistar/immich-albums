# ServerConfigDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_page_message** | **str** |  | 
**map_tile_url** | **str** |  | 
**oauth_button_text** | **str** |  | 

## Example

```python
from openapi_client.models.server_config_dto import ServerConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServerConfigDto from a JSON string
server_config_dto_instance = ServerConfigDto.from_json(json)
# print the JSON string representation of the object
print ServerConfigDto.to_json()

# convert the object into a dict
server_config_dto_dict = server_config_dto_instance.to_dict()
# create an instance of ServerConfigDto from a dict
server_config_dto_form_dict = server_config_dto.from_dict(server_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


