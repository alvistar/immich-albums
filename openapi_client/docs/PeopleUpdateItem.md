# PeopleUpdateItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birth_date** | **date** | Person date of birth. Note: the mobile app cannot currently set the birth date to null. | [optional] 
**feature_face_asset_id** | **str** | Asset is used to get the feature face thumbnail. | [optional] 
**id** | **str** | Person id. | 
**is_hidden** | **bool** | Person visibility | [optional] 
**name** | **str** | Person name. | [optional] 

## Example

```python
from openapi_client.models.people_update_item import PeopleUpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleUpdateItem from a JSON string
people_update_item_instance = PeopleUpdateItem.from_json(json)
# print the JSON string representation of the object
print PeopleUpdateItem.to_json()

# convert the object into a dict
people_update_item_dict = people_update_item_instance.to_dict()
# create an instance of PeopleUpdateItem from a dict
people_update_item_form_dict = people_update_item.from_dict(people_update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


