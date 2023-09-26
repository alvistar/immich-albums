# AuditDeletesResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | 
**needs_full_sync** | **bool** |  | 

## Example

```python
from openapi_client.models.audit_deletes_response_dto import AuditDeletesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuditDeletesResponseDto from a JSON string
audit_deletes_response_dto_instance = AuditDeletesResponseDto.from_json(json)
# print the JSON string representation of the object
print AuditDeletesResponseDto.to_json()

# convert the object into a dict
audit_deletes_response_dto_dict = audit_deletes_response_dto_instance.to_dict()
# create an instance of AuditDeletesResponseDto from a dict
audit_deletes_response_dto_form_dict = audit_deletes_response_dto.from_dict(audit_deletes_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


