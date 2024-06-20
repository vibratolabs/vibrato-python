<!-- Start SDK Example Usage [usage] -->
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