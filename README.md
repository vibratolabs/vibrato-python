# vibrato-python

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/advanced-setup/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

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

res = s.calls.list_calls()

if res.call_list is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [calls](docs/sdks/calls/README.md)

* [list_calls](docs/sdks/calls/README.md#list_calls) - List all calls
* [create_call](docs/sdks/calls/README.md#create_call) - Create a new call
* [retrieve_call](docs/sdks/calls/README.md#retrieve_call) - Retrieve a specific call
* [update_call](docs/sdks/calls/README.md#update_call) - Update an existing call
* [delete_call](docs/sdks/calls/README.md#delete_call) - Delete a specific call
* [end_call](docs/sdks/calls/README.md#end_call) - End a specific call
* [get_transcript](docs/sdks/calls/README.md#get_transcript) - Get transcript for a specific call
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
    res = s.calls.list_calls()
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.call_list is not None:
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

res = s.calls.list_calls()

if res.call_list is not None:
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

res = s.calls.list_calls()

if res.call_list is not None:
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

res = s.calls.list_calls()

if res.call_list is not None:
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
