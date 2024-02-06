# SystemConfigFFmpegDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accel** | [**TranscodeHWAccel**](TranscodeHWAccel.md) |  | 
**accepted_audio_codecs** | [**List[AudioCodec]**](AudioCodec.md) |  | 
**accepted_video_codecs** | [**List[VideoCodec]**](VideoCodec.md) |  | 
**bframes** | **int** |  | 
**cq_mode** | [**CQMode**](CQMode.md) |  | 
**crf** | **int** |  | 
**gop_size** | **int** |  | 
**max_bitrate** | **str** |  | 
**npl** | **int** |  | 
**preferred_hw_device** | **str** |  | 
**preset** | **str** |  | 
**refs** | **int** |  | 
**target_audio_codec** | [**AudioCodec**](AudioCodec.md) |  | 
**target_resolution** | **str** |  | 
**target_video_codec** | [**VideoCodec**](VideoCodec.md) |  | 
**temporal_aq** | **bool** |  | 
**threads** | **int** |  | 
**tonemap** | [**ToneMapping**](ToneMapping.md) |  | 
**transcode** | [**TranscodePolicy**](TranscodePolicy.md) |  | 
**two_pass** | **bool** |  | 

## Example

```python
from openapi_client.models.system_config_f_fmpeg_dto import SystemConfigFFmpegDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemConfigFFmpegDto from a JSON string
system_config_f_fmpeg_dto_instance = SystemConfigFFmpegDto.from_json(json)
# print the JSON string representation of the object
print SystemConfigFFmpegDto.to_json()

# convert the object into a dict
system_config_f_fmpeg_dto_dict = system_config_f_fmpeg_dto_instance.to_dict()
# create an instance of SystemConfigFFmpegDto from a dict
system_config_f_fmpeg_dto_form_dict = system_config_f_fmpeg_dto.from_dict(system_config_f_fmpeg_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


