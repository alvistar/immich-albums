# BulkIdResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**id** | **str** |  | 
**success** | **bool** |  | 

## Example

```python
from openapi_client.models.bulk_id_response_dto import BulkIdResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkIdResponseDto from a JSON string
bulk_id_response_dto_instance = BulkIdResponseDto.from_json(json)
# print the JSON string representation of the object
print BulkIdResponseDto.to_json()

# convert the object into a dict
bulk_id_response_dto_dict = bulk_id_response_dto_instance.to_dict()
# create an instance of BulkIdResponseDto from a dict
bulk_id_response_dto_form_dict = bulk_id_response_dto.from_dict(bulk_id_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


