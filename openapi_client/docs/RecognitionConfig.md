# RecognitionConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**max_distance** | **int** |  | 
**min_faces** | **int** |  | 
**min_score** | **int** |  | 
**model_name** | **str** |  | 
**model_type** | [**ModelType**](ModelType.md) |  | [optional] 

## Example

```python
from openapi_client.models.recognition_config import RecognitionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecognitionConfig from a JSON string
recognition_config_instance = RecognitionConfig.from_json(json)
# print the JSON string representation of the object
print RecognitionConfig.to_json()

# convert the object into a dict
recognition_config_dict = recognition_config_instance.to_dict()
# create an instance of RecognitionConfig from a dict
recognition_config_form_dict = recognition_config.from_dict(recognition_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


