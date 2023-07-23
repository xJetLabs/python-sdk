# Python SDK for xJet Connect API

## Authors
- [@xJetLabs](https://github.com/xJetLabs) (forked from)
- [@nik-1x](https://www.github.com/nik-1x)
 
## Installation
```shell
pip install xjet
```
If requires <b>nacl</b> package, install it <i>manually</i>:
```shell
pip install pynacl
```

## Webhook analog
```python
while True:
    res = httpx.get(
        'https://api.xjet.io/v1/account.events',
        params={'timeout': 10},
        headers={
            'X-API-Key': api_key,
        },
        timeout=11,
    )
    print(res.json)

    time.sleep(3)
```


## Usage/Examples  
[Live example](https://replit.com/@delpydoc/xJetAPI)

### Initialization
```python
from xjet import JetAPI

# api_key: str
# private_key: str
api = JetAPI(
    api_key="API_KEY",
    private_key="PRIVATE_KEY",
    network='mainnet'  # mainnet / testnet
)
```


### Info
```python
await xjet.currencies() # Shows all saved xJetSwap currencies
```


### Account
```python
await api.me() # get API Application information.
# {'id': <str>, 'name: <str>, 'service_wallet': <str>}

await api.balance() # get balance
# {
#   'balances': [
#       {'currency': <int>, 'amount': <float>, 
#           'values': {'byn': 0.0, 'cny': 0.0, 'eur': 0.0, 'gbp': 0.0, 'kzt': 0.0, 'rub': 0.0, 'uah': 0.0, 'usd': 0.0}}], 
#   'timestamp': <int>
# }

await api.submit_deposit() # check for deposit
# {'success': <bool>}

# ton_address: str
# currency: str
# amount: float
await api.withdraw(ton_address, currency, amount) # check for deposit

# limit: int
# offset: int
await xjet.operations(limit, offset) # operations
```

### Cheque
```python
# currency: str
# amount: float
# expires: [int, None]
# description: [str, None]
# activates_count: [int, None]
# groups_id: [int, None]
# personal_id: [int, None]
# password: [str, None]

await api.cheque_create(currency, amount, expires, description, activates_count, groups_id, personal_id, password) # create cheque
# {'cheque_id': <str>, 'external_link': 'https://t.me/xJetSwapBot?start=c_<cheque_id>'}

await api.cheque_status(cheque_id) # get cheque status
# {
#   'id': <str>, 
#   'issuer_id': <str>, 
#   'amount': <float>, 
#   'activates_count': <int>, 
#   'activates: <list[str]>, 
#   'locked_value': <float>, 
#   'currency': <Str>, 
#   'expires': <bool>, 
#   'description': <str>, 
#   'status': 'activated/canceled/expired/active', 
#   'password': <str | None>, 
#   'groups_id': <list[str] | None>, 
#   'personal_id': <int | None>, 
#   'is_for_premium': <bool>
# }


await api.cheque_list() # get cheques on account
# list of cheque_status

await api.cheque_cancel(cheque_id) # delete cheque
# returns cheque_status
```


### Invoice
```python
# currency: str
# amount: float
# description: [str, None]
# max_payments: [int, None]
await api.invoice_create(currency, amount, description, max_payments) # create invoice
# {'invoice_id': <str>, 'external_link': 'https://t.me/xJetSwapBot?start=inv_<cheque_id>'}

await api.invoice_status(invoice_status) # get invoice status
# {
#   'id': <str>, 
#   'description': <str>, 
#   'currency': <str>, 
#   'amount': <float>, 
#   'max_amount': None, 
#   'min_amount': None, 
#   'payments': [{'telegram_id': <int>, 'amount': <float>, 'comment': [str | None}, ... ], 
#   'max_payments': 1, 
#   'after_pay': [], 
#   'created': '2023-04-20T22:55:24.313000'
# }

await api.invoice_list() # get invoices on account
# list of invoice_status
```

```python
# NFT methods
await api.nft_list()
await api.nft_transfer(nft_address, to_address)
```

## License
[GNUv3](https://github.com/nik-1x/pyxJetAPI/blob/main/LICENSE)  
