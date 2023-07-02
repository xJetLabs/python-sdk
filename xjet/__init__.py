import time
import json

from .api import Account, Cheques, Invoices, System, NFT, Exchanges

from ecdsa import SigningKey, Ed25519
from httpx import AsyncClient


class JetAPI(Account, Cheques, Invoices, System, NFT, Exchanges):
    """
    Class for working with t.me/xJetSwapBot API.

    :author: Nick [t.me/crypt_nick]
    :author: Doc. Delpy [t.me/delpydoc]

    :license: GNUv3
    """

    def __init__(self, api_key: str, private_key: str = None, network: str = 'mainnet'):
        """
        Class initialization.

        :param `api_key` [str]: API key
        :param `private_key` [str]: Private key
        :param `mainnet` [bool or `xJetNet`]: Mainnet or testnet (`True`/`xJetNet.MAINNET` for mainnet, else - `False`/`xJetNet.TESTNET`)
        """

        if network in ["mainnet", "testnet", "localnet"]:
            network = {
                "mainnet": 1,
                "testnet": 2,
                "localnet": 3
            }[network]
        
        assert network in [1,2,3], 'Invalid "network" value!'
                        
        assert type(api_key) in [str, bytes], 'Invalid "api_key" value!'
        if type(api_key) == bytes: api_key = api_key.decode('utf-8')
        
        assert type(private_key) in [str, bytes], 'Invalid "private_key" value!'
        if type(private_key) == bytes: private_key = private_key.decode('utf-8')
        
        self.api_key = api_key
        self.private_key = bytes.fromhex(private_key) if type(private_key) == str else private_key
        self.network: str = {
                        "1": 'https://xjet.app/api/v1',
                        "2": 'https://testnet.xjet.app/api/v1',
                        "3": 'https://127.0.0.1:5000/api/v1',
                    }[str(network)] 
        self.client = AsyncClient(headers={'X-API-Key': self.api_key})

    async def request(self, method: str, request_method = "POST", **kwargs):
        """ Send request to API xJet 
        
        :param `method` [str]: Method of API
        :param `*kwargs`: Other params
        """
        try:
            request = await self.client.request(
                method = request_method,
                url = self.network + "/" + method.replace('/', ''),
                **kwargs
            )

            res = request.json()
            if res.get('error'): 
                return res['error']
            return res
        except Exception as e:
            return {'error': e}

    def sign_message(self, message: dict = {}) -> dict:
        """ Sign json body of reques
        
        :param `message` [dict]: Message for signing"""
        message['query_id']  = (int(time.time() + 60) << 16) if 'query_id' not in message else message['query_id']
        message['signature'] = SigningKey.from_string(self.private_key, curve=Ed25519).sign(json.dumps(message).encode()).hex()
        return message
