# Campaigns
(*campaigns*)

### Available Operations

* [list_campaigns](#list_campaigns) - List all campaigns
* [create_campaign](#create_campaign) - Create a new campaign
* [retrieve_campaign](#retrieve_campaign) - Retrieve a specific campaign
* [update_campaign](#update_campaign) - Update an existing campaign
* [delete_campaign](#delete_campaign) - Delete a specific campaign

## list_campaigns

List all campaigns

### Example Usage

```python
import vibrato

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.campaigns.list_campaigns()

if res.campaign_list is not None:
    # handle response
    pass

```


### Response

**[operations.ListCampaignsResponse](../../models/operations/listcampaignsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_campaign

Create a new campaign

### Example Usage

```python
import vibrato
from vibrato.models import components

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.campaigns.create_campaign(request=components.CampaignInput(
    name='<value>',
    task_property_to_contact_field={
        'key': '<value>',
    },
    task_template_uuid='fcb815f3-1aff-4138-bc70-f4cb520fc2e9',
    daily_availability=[
        components.DailyAvailability(),
    ],
    timezone='America/New_York',
))

if res.campaign is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [components.CampaignInput](../../models/components/campaigninput.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateCampaignResponse](../../models/operations/createcampaignresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## retrieve_campaign

Retrieve a specific campaign

### Example Usage

```python
import vibrato

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.campaigns.retrieve_campaign(uuid='<value>')

if res.campaign is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `uuid`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.RetrieveCampaignResponse](../../models/operations/retrievecampaignresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_campaign

Update an existing campaign

### Example Usage

```python
import vibrato
from vibrato.models import components

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.campaigns.update_campaign(uuid='<value>', campaign=components.CampaignInput(
    name='<value>',
    task_property_to_contact_field={
        'key': '<value>',
    },
    task_template_uuid='706fe693-8083-4d12-ab4e-5c7215f5e15a',
    daily_availability=[
        components.DailyAvailability(),
    ],
    timezone='America/New_York',
))

if res.campaign is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `uuid`                                                               | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `campaign`                                                           | [components.CampaignInput](../../models/components/campaigninput.md) | :heavy_check_mark:                                                   | N/A                                                                  |


### Response

**[operations.UpdateCampaignResponse](../../models/operations/updatecampaignresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_campaign

Delete a specific campaign

### Example Usage

```python
import vibrato

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.campaigns.delete_campaign(uuid='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `uuid`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteCampaignResponse](../../models/operations/deletecampaignresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
