# pyxJetAPI

## Authors
- [@xJetLabs](https://github.com/xJetLabs) (forked from)
- [@nik-1x](https://www.github.com/nik-1x)
 
## Usage/Examples  
```python
api = pyxJet(
    api_key="API_KEY",
    private_key="PRIVATE_KEY", 
    mainnet=xJetNet.TESTNET # or xJetNet.MAINNET
)
```

```python
# Account methods
await api.me() # get API Application information.
await api.balance() # get balance
await api.submit_deposit() # check for deposit
await api.withdraw(ton_address, currency, amount) # check for deposit
```

```python
# Cheques methods
await api.cheque_create(currency, amount, expires, description, activates_count, groups_id, personal_id, password) # create cheque
await api.cheque_status(cheque_id) # get cheque status
await api.cheque_list() # get cheques on account
await api.cheque_cancel(cheque_id) # delete cheque
```

```python
# Invoice methods
await api.invoice_create(currency, amount, description, max_payments) # create invoice
await api.invoice_status(invoice_status) # get invoice status
await api.invoice_list() # get invoices on account
```

## License
[GNUv3](https://github.com/nik-1x/pyxJetAPI/blob/main/LICENSE)  
