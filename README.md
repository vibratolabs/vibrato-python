# vibrato-python (Beta)

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+<UNSET>.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import vibrato

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.users.retrieve_current_user()

if res.user is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [users](docs/sdks/users/README.md)

* [retrieve_current_user](docs/sdks/users/README.md#retrieve_current_user) - Retrieve current user profile

### [calls](docs/sdks/calls/README.md)

* [list_calls](docs/sdks/calls/README.md#list_calls) - List all calls
* [create_call](docs/sdks/calls/README.md#create_call) - Create a new call
* [create_call_from_task_template](docs/sdks/calls/README.md#create_call_from_task_template) - Create a new call from a task template
* [retrieve_call](docs/sdks/calls/README.md#retrieve_call) - Retrieve a specific call
* [update_call](docs/sdks/calls/README.md#update_call) - Update an existing call
* [delete_call](docs/sdks/calls/README.md#delete_call) - Delete a specific call
* [end_call](docs/sdks/calls/README.md#end_call) - End a specific call
* [get_transcript](docs/sdks/calls/README.md#get_transcript) - Get transcript for a specific call

### [task_templates](docs/sdks/tasktemplates/README.md)

* [list_task_templates](docs/sdks/tasktemplates/README.md#list_task_templates) - List all task templates
* [create_task_template](docs/sdks/tasktemplates/README.md#create_task_template) - Create a new task template
* [retrieve_task_template](docs/sdks/tasktemplates/README.md#retrieve_task_template) - Retrieve a specific task template
* [update_task_template](docs/sdks/tasktemplates/README.md#update_task_template) - Update an existing task template
* [delete_task_template](docs/sdks/tasktemplates/README.md#delete_task_template) - Delete a specific task template
* [create_task_template_from_call](docs/sdks/tasktemplates/README.md#create_task_template_from_call) - Create a task template from a call

### [campaigns](docs/sdks/campaigns/README.md)

* [list_campaigns](docs/sdks/campaigns/README.md#list_campaigns) - List all campaigns
* [create_campaign](docs/sdks/campaigns/README.md#create_campaign) - Create a new campaign
* [retrieve_campaign](docs/sdks/campaigns/README.md#retrieve_campaign) - Retrieve a specific campaign
* [update_campaign](docs/sdks/campaigns/README.md#update_campaign) - Update an existing campaign
* [delete_campaign](docs/sdks/campaigns/README.md#delete_campaign) - Delete a specific campaign

### [contacts](docs/sdks/contacts/README.md)

* [list_contacts](docs/sdks/contacts/README.md#list_contacts) - List all contacts
* [create_contact](docs/sdks/contacts/README.md#create_contact) - Create a new contact
* [retrieve_contact](docs/sdks/contacts/README.md#retrieve_contact) - Retrieve a specific contact
* [update_contact](docs/sdks/contacts/README.md#update_contact) - Update an existing contact
* [delete_contact](docs/sdks/contacts/README.md#delete_contact) - Delete a specific contact
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

### Example

```python
import vibrato
from vibrato.models import errors

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = None
try:
    res = s.users.retrieve_current_user()

except errors.SDKError as e:
    # handle exception
    raise(e)

if res.user is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.getvibrato.com/api/v1` | None |

#### Example

```python
import vibrato

s = vibrato.Vibrato(
    server_idx=0,
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.users.retrieve_current_user()

if res.user is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import vibrato

s = vibrato.Vibrato(
    server_url="https://api.getvibrato.com/api/v1",
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.users.retrieve_current_user()

if res.user is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import vibrato
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = vibrato.Vibrato(client=http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `bearer_auth` | http          | HTTP Bearer   |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
import vibrato

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.users.retrieve_current_user()

if res.user is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
