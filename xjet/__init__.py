import time
import json

from .constants import xJetNet
from .api import Account, Cheques, Invoices, System

from nacl.signing import SigningKey
from httpx import AsyncClient


class JetAPI(Account, Cheques, Invoices, System):

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
        self.api_key = api_key
        self.host = getattr(xJetNet, network.upper())
        self.private_key = bytes.fromhex(private_key) if type(private_key) == str else private_key
        self.client = AsyncClient(headers={'X-API-Key': self.api_key})

    async def request(self, method: str, **kwargs):
        """ Send request to API xJet 
        
        :param `method` [str]: Method of API
        :param `*kwargs`: Other params
        """
        request = await self.client.request(
            method = "POST",
            url = self.host + "/" + method.replace('/', ''),
            **kwargs
        )

        res = request.json()
        if res.get('error'): 
            return res['error']
        return res

    def sign_message(self, message: dict = {}) -> dict:
        """ Sign json body of reques
        
        :param `message` [dict]: Message for signing"""
        if 'query_id' not in message: 
            message['query_id'] = int(time.time() + 60) << 16 

        message['signature'] = SigningKey(self.private_key).sign(
            json.dumps(message).encode()
        )._signature.hex()

        return message