# TaskTemplates
(*task_templates*)

### Available Operations

* [list_task_templates](#list_task_templates) - List all task templates
* [create_task_template](#create_task_template) - Create a new task template
* [retrieve_task_template](#retrieve_task_template) - Retrieve a specific task template
* [update_task_template](#update_task_template) - Update an existing task template
* [delete_task_template](#delete_task_template) - Delete a specific task template
* [create_task_template_from_call](#create_task_template_from_call) - Create a task template from a call

## list_task_templates

List all task templates

### Example Usage

```python
import vibrato

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.task_templates.list_task_templates()

if res.task_template_list is not None:
    # handle response
    pass

```


### Response

**[operations.ListTaskTemplatesResponse](../../models/operations/listtasktemplatesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_task_template

Create a new task template

### Example Usage

```python
import vibrato
from vibrato.models import components

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.task_templates.create_task_template(request=components.TaskTemplateInput())

if res.task_template is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [components.TaskTemplateInput](../../models/components/tasktemplateinput.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.CreateTaskTemplateResponse](../../models/operations/createtasktemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## retrieve_task_template

Retrieve a specific task template

### Example Usage

```python
import vibrato

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.task_templates.retrieve_task_template(uuid='<value>')

if res.task_template is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `uuid`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.RetrieveTaskTemplateResponse](../../models/operations/retrievetasktemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_task_template

Update an existing task template

### Example Usage

```python
import vibrato
from vibrato.models import components

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.task_templates.update_task_template(uuid='<value>', task_template=components.TaskTemplateInput())

if res.task_template is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `uuid`                                                                       | *str*                                                                        | :heavy_check_mark:                                                           | N/A                                                                          |
| `task_template`                                                              | [components.TaskTemplateInput](../../models/components/tasktemplateinput.md) | :heavy_check_mark:                                                           | N/A                                                                          |


### Response

**[operations.UpdateTaskTemplateResponse](../../models/operations/updatetasktemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_task_template

Delete a specific task template

### Example Usage

```python
import vibrato

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.task_templates.delete_task_template(uuid='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `uuid`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteTaskTemplateResponse](../../models/operations/deletetasktemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_task_template_from_call

Create a task template from a call

### Example Usage

```python
import vibrato
from vibrato.models import operations

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.task_templates.create_task_template_from_call(request=operations.CreateTaskTemplateFromCallRequestBody())

if res.task_template is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.CreateTaskTemplateFromCallRequestBody](../../models/operations/createtasktemplatefromcallrequestbody.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.CreateTaskTemplateFromCallResponse](../../models/operations/createtasktemplatefromcallresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
