# Calls
(*calls*)

### Available Operations

* [list_calls](#list_calls) - List all calls
* [create_call](#create_call) - Create a new call
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
import vibrato
from vibrato.models import components

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.calls.create_call(request=components.CallInput(
    country_code='PF',
    phone_number='<value>',
    prompt='<value>',
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
import vibrato
from vibrato.models import components

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.calls.update_call(id='<value>', call=components.CallInput(
    country_code='RS',
    phone_number='<value>',
    prompt='<value>',
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

Get transcript for a specific call

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
