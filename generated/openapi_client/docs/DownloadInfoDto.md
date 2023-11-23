# DownloadInfoDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**album_id** | **str** |  | [optional] 
**archive_size** | **int** |  | [optional] 
**asset_ids** | **List[str]** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.download_info_dto import DownloadInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadInfoDto from a JSON string
download_info_dto_instance = DownloadInfoDto.from_json(json)
# print the JSON string representation of the object
print DownloadInfoDto.to_json()

# convert the object into a dict
download_info_dto_dict = download_info_dto_instance.to_dict()
# create an instance of DownloadInfoDto from a dict
download_info_dto_form_dict = download_info_dto.from_dict(download_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


