# Contacts
(*contacts*)

### Available Operations

* [list_contacts](#list_contacts) - List all contacts
* [create_contact](#create_contact) - Create a new contact
* [retrieve_contact](#retrieve_contact) - Retrieve a specific contact
* [update_contact](#update_contact) - Update an existing contact
* [delete_contact](#delete_contact) - Delete a specific contact

## list_contacts

List all contacts

### Example Usage

```python
import vibrato

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.contacts.list_contacts()

if res.contact_list is not None:
    # handle response
    pass

```


### Response

**[operations.ListContactsResponse](../../models/operations/listcontactsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_contact

Create a new contact

### Example Usage

```python
import vibrato
from vibrato.models import components

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.contacts.create_contact(request=components.ContactInput(
    first_name='Rhianna',
))

if res.contact is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [components.ContactInput](../../models/components/contactinput.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.CreateContactResponse](../../models/operations/createcontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## retrieve_contact

Retrieve a specific contact

### Example Usage

```python
import vibrato

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.contacts.retrieve_contact(uuid='<value>')

if res.contact is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `uuid`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.RetrieveContactResponse](../../models/operations/retrievecontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_contact

Update an existing contact

### Example Usage

```python
import vibrato
from vibrato.models import components

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.contacts.update_contact(uuid='<value>', contact=components.ContactInput(
    first_name='Carley',
))

if res.contact is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `uuid`                                                             | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `contact`                                                          | [components.ContactInput](../../models/components/contactinput.md) | :heavy_check_mark:                                                 | N/A                                                                |


### Response

**[operations.UpdateContactResponse](../../models/operations/updatecontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_contact

Delete a specific contact

### Example Usage

```python
import vibrato

s = vibrato.Vibrato(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.contacts.delete_contact(uuid='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `uuid`             | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteContactResponse](../../models/operations/deletecontactresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
