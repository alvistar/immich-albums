# QueueStatusDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** |  | 
**is_paused** | **bool** |  | 

## Example

```python
from openapi_client.models.queue_status_dto import QueueStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of QueueStatusDto from a JSON string
queue_status_dto_instance = QueueStatusDto.from_json(json)
# print the JSON string representation of the object
print QueueStatusDto.to_json()

# convert the object into a dict
queue_status_dto_dict = queue_status_dto_instance.to_dict()
# create an instance of QueueStatusDto from a dict
queue_status_dto_form_dict = queue_status_dto.from_dict(queue_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


