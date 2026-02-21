# Calls
(*calls*)

### Available Operations

* [list_calls](#list_calls) - List all calls
* [create_call](#create_call) - Create a new call
* [create_call_from_task_template](#create_call_from_task_template) - Create a new call from a task template
* [retrieve_call](#retrieve_call) - Retrieve a specific call
* [update_call](#update_call) - Update an existing call
* [delete_call](#delete_call) - Delete a specific call
* [end_call](#end_call) - End a specific call
* [get_transcript](#get_transcript) - Get transcript for a specific call

## list_calls

List all calls

### Example Usage

```python
import vibrato

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.calls.list_calls()

if res.call_list is not None:
    # handle response
    pass

```


### Response

**[operations.ListCallsResponse](../../models/operations/listcallsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_call

Create a new call

### Example Usage

```python
import dateutil.parser
import vibrato
from vibrato.models import components

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.calls.create_call(request=components.CallInput(
    country_code='1',
    phone_number='7607916516',
    prompt='Call my internet provider and ask for a lower bill.',
    locale='en-us',
    labels=[
        'billing',
        'retention',
    ],
    api_idempotency_key='call-12345',
    tags=[
        'utilities',
        'negotiation',
    ],
    voice_id='ErXwobaYiN019PkySvjV',
    voice_clone_uuid='d4e5f6a7-b8c9-4d0e-a1f2-b3c4d5e6f7a8',
    leave_voicemail_message=False,
    voicemail_message='Hi, this is David. Please call me back.',
    handoff_condition='When reaching a human representative',
    handoff_phone_number_uuid='5f88e942-50ed-43f8-9ce0-6f9e3c5a4dea',
    handoff_phone_number='17607916516',
    retries=2,
    retry_delay_seconds=300,
    scheduled_at=dateutil.parser.isoparse('2026-12-31T18:30:00Z'),
    outbound_twilio_phone_number_uuid='c49af1ad-e9b3-47b7-b45e-6f8832a1f293',
    outbound_twilio_phone_number='17607916516',
))

if res.call is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [components.CallInput](../../models/components/callinput.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.CreateCallResponse](../../models/operations/createcallresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_call_from_task_template

Create a new call from a task template

### Example Usage

```python
import dateutil.parser
import vibrato
from vibrato.models import components

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.calls.create_call_from_task_template(request=components.CreateFromTaskTemplate(
    task_template_uuid='a3f76070-c81b-4e34-acd8-30e70b1d2a42',
    recipient_name='Comcast Support',
    recipient_phone_number='7607916516',
    recipient_country_code='1',
    contact_uuid='e7a1b2c3-d4e5-4f6a-8b9c-0d1e2f3a4b5c',
    voice_id='ErXwobaYiN019PkySvjV',
    voice_clone_uuid='d4e5f6a7-b8c9-4d0e-a1f2-b3c4d5e6f7a8',
    leave_voicemail_message=True,
    voicemail_message='Please call me back when available.',
    handoff_phone_number_uuid='5f88e942-50ed-43f8-9ce0-6f9e3c5a4dea',
    handoff_phone_number='17607916516',
    handoff_condition='When reaching a human representative',
    retries=2,
    retry_delay_seconds=300,
    scheduled_at=dateutil.parser.isoparse('2026-12-31T18:30:00Z'),
    outbound_twilio_phone_number_uuid='c49af1ad-e9b3-47b7-b45e-6f8832a1f293',
    outbound_twilio_phone_number='17607916516',
))

if res.call is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.CreateFromTaskTemplate](../../models/components/createfromtasktemplate.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateCallFromTaskTemplateResponse](../../models/operations/createcallfromtasktemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## retrieve_call

Retrieve a specific call

### Example Usage

```python
import vibrato

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.calls.retrieve_call(id='<value>')

if res.call is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.RetrieveCallResponse](../../models/operations/retrievecallresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_call

Update an existing call

### Example Usage

```python
import dateutil.parser
import vibrato
from vibrato.models import components

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.calls.update_call(id='<value>', call=components.CallInput(
    country_code='1',
    phone_number='7607916516',
    prompt='Call my internet provider and ask for a lower bill.',
    locale='en-us',
    labels=[
        'billing',
        'retention',
    ],
    api_idempotency_key='call-12345',
    tags=[
        'utilities',
        'negotiation',
    ],
    voice_id='ErXwobaYiN019PkySvjV',
    voice_clone_uuid='d4e5f6a7-b8c9-4d0e-a1f2-b3c4d5e6f7a8',
    leave_voicemail_message=False,
    voicemail_message='Hi, this is David. Please call me back.',
    handoff_condition='When reaching a human representative',
    handoff_phone_number_uuid='5f88e942-50ed-43f8-9ce0-6f9e3c5a4dea',
    handoff_phone_number='17607916516',
    retries=2,
    retry_delay_seconds=300,
    scheduled_at=dateutil.parser.isoparse('2026-12-31T18:30:00Z'),
    outbound_twilio_phone_number_uuid='c49af1ad-e9b3-47b7-b45e-6f8832a1f293',
    outbound_twilio_phone_number='17607916516',
))

if res.call is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          |
| `call`                                                       | [components.CallInput](../../models/components/callinput.md) | :heavy_check_mark:                                           | N/A                                                          |


### Response

**[operations.UpdateCallResponse](../../models/operations/updatecallresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_call

Delete a specific call

### Example Usage

```python
import vibrato

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.calls.delete_call(id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteCallResponse](../../models/operations/deletecallresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## end_call

End a specific call

### Example Usage

```python
import vibrato

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.calls.end_call(id='<value>')

if res.call is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.EndCallResponse](../../models/operations/endcallresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_transcript

Returns the full current transcript snapshot for the call. For live incremental updates, subscribe to the websocket stream after fetching this snapshot.

### Example Usage

```python
import vibrato

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.calls.get_transcript(id='<value>')

if res.transcript is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetTranscriptResponse](../../models/operations/gettranscriptresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
