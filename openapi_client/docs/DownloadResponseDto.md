# DownloadResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archives** | [**List[DownloadArchiveInfo]**](DownloadArchiveInfo.md) |  | 
**total_size** | **int** |  | 

## Example

```python
from openapi_client.models.download_response_dto import DownloadResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadResponseDto from a JSON string
download_response_dto_instance = DownloadResponseDto.from_json(json)
# print the JSON string representation of the object
print DownloadResponseDto.to_json()

# convert the object into a dict
download_response_dto_dict = download_response_dto_instance.to_dict()
# create an instance of DownloadResponseDto from a dict
download_response_dto_form_dict = download_response_dto.from_dict(download_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


