<!-- Start SDK Example Usage [usage] -->
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