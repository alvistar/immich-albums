# SystemConfigMachineLearningDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | [**ClassificationConfig**](ClassificationConfig.md) |  | 
**clip** | [**CLIPConfig**](CLIPConfig.md) |  | 
**enabled** | **bool** |  | 
**facial_recognition** | [**RecognitionConfig**](RecognitionConfig.md) |  | 
**url** | **str** |  | 

## Example

```python
from openapi_client.models.system_config_machine_learning_dto import SystemConfigMachineLearningDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigMachineLearningDto from a JSON string
system_config_machine_learning_dto_instance = SystemConfigMachineLearningDto.from_json(json)
# print the JSON string representation of the object
print SystemConfigMachineLearningDto.to_json()

# convert the object into a dict
system_config_machine_learning_dto_dict = system_config_machine_learning_dto_instance.to_dict()
# create an instance of SystemConfigMachineLearningDto from a dict
system_config_machine_learning_dto_form_dict = system_config_machine_learning_dto.from_dict(system_config_machine_learning_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


