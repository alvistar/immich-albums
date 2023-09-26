# ClassificationConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**min_score** | **int** |  | 
**model_name** | **str** |  | 
**model_type** | [**ModelType**](ModelType.md) |  | [optional] 

## Example

```python
from openapi_client.models.classification_config import ClassificationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ClassificationConfig from a JSON string
classification_config_instance = ClassificationConfig.from_json(json)
# print the JSON string representation of the object
print ClassificationConfig.to_json()

# convert the object into a dict
classification_config_dict = classification_config_instance.to_dict()
# create an instance of ClassificationConfig from a dict
classification_config_form_dict = classification_config.from_dict(classification_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


