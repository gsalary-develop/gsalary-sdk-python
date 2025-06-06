# GSalary SDK for Python 3.x

API Document:

- [CN version](https://api.gsalary.com/doc/index.html?lang=cn)
- [EN version](https://api.gsalary.com/doc/index.html?lang=en)

## Import

```bash
pip install gsalary-sdk
```

## Prepare

Configure your appid, client-side private key, server-side public key and endpoint to the GSalary Client.

The endpoint shall not contain the context path.

```python
from gsalary_sdk import GSalaryClient, GSalaryConfig

config = GSalaryConfig()
config.appid = 'aaaaaaa'
config.config_client_private_key_pem_file('/path/to/client_private_key.pem')
config.config_server_public_key_pem_file('/path/to/server_public_key.pem')
# or you can load pem directly
config.config_client_private_key_pem('-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----')
config.config_server_public_key_pem('-----BEGIN PUBLIC KEY-----\n...\n-----END PUBLIC KEY-----')
_cli = GSalaryClient(config)
```

## Make A Request

### POST request example

```python
from gsalary_sdk import GSalaryRequest

path = "/v1/exchange/quotes"
request_body = dict(sell_currency='USD',
                    buy_currency='CNY',
                    sell_amount=0.1)

request = GSalaryRequest('POST', path, body=request_body)
resp = _cli.request(request)
```

### GET request example

```python
from gsalary_sdk import GSalaryRequest

path = "/v1/cards"

args = dict(create_start="2024-02-01T00:00:00+00:00",
            create_end="2024-05-01T00:00:00+00:00",
            page='1',
            limit='20')

request = GSalaryRequest('GET', path, query_args=args)
resp = _cli.request(request)
```