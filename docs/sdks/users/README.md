# Users
(*users*)

### Available Operations

* [retrieve_current_user](#retrieve_current_user) - Retrieve current user profile

## retrieve_current_user

Retrieve current user profile

### Example Usage

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


### Response

**[operations.RetrieveCurrentUserResponse](../../models/operations/retrievecurrentuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
