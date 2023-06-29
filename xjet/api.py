from typing import Union


class System:

    """ System class.

    Available methods:

    * `currencies` - Get list of currencies

    """

    async def currencies(self):
        """ Get list of currencies

        :return: List of currencies

        """
        return await self.request(method = 'system.currencies')


class Account:

    """ Account methods wrapper. 
    
    Available methods:

    * `me` - Get information about API application
    * `balances` - Get balances
    * `submit_deposit` - Check for deposit
    * `withdraw` - Withdraw funds
    
    """
    
    async def me(self):
        """ Get information about API application. """
        return await self.request(method = 'account.me')

    async def balance(self):
        """ Get balance """
        return await self.request(method = 'account.balances')

    async def submit_deposit(self):
        """ Check for deposit """
        return await self.request(method = 'account.submitDeposit')

    async def withdraw(self, ton_address: str, currency: str, amount: Union[int, float]):
        """ Withdraw funds 
        
        :param `ton_address` [str]: TON address
        :param `currency` [str]: Currency of withdraw
        :param `amount` Union[int, float]: Amount of withdraw
        """
        return await self.request(
            method = 'account.withdraw', 
            json = self.sign_message({
                'ton_address': ton_address, 'currency': currency, 'amount': amount
            })
        )

    async def operations(self, limit: int = 100, offset: int = 0):
        """ Get operations history """
        return await self.request(
            method = 'account.operations',
            json = {
                'limit': limit, 'offset': offset
            }
        )


class Cheques:

    """ Cheques methods wrapper. 
    
    Available methods:

    * `cheque_create` - Create cheques
    * `cheque_status` - Get cheque status
    * `cheque_list` - Get list of cheques
    * `cheque_activate` - Activate cheque
    
    """

    async def cheque_create(self, currency: str, amount: Union[int, float], expires: int = None, description: str = '', activates_count: int = 1, groups_id: list = None, personal_id: str = None, password: str = None, **kwargs):
        """ Create cheques 
        
        :param `currency` [str]: Currency of cheque
        :param `amount` Union[int, float]: Amount of cheque
        :param `expires` [int]: Expiration time of cheque
        :param `description` [str]: Description of cheque
        :param `activates_count` [int]: Number of activations
        :param `groups_id` [list]: List of groups
        :param `personal_id` [str]: Personal id
        :param `password` [str]: Password

        """
        return await self.request(
            method='cheque.create', 
            json=self.sign_message({
                'currency': currency,
                'amount': amount,
                'expires': expires,
                'description': description,
                'activates_count': activates_count,
                'groups_id': groups_id,
                'personal_id': personal_id,
                'password': password,
                **kwargs
            })
        )

    async def cheque_status(self, cheque_id: str):
        """ Get cheque status 
        
        :param `cheque_id` [str]: Cheque id
        """
        return await self.request(method = 'cheque.status', params = {'cheque_id': cheque_id})

    async def cheque_list(self):
        """ Get list of cheques """
        return await self.request(method = 'cheque.list')

    async def cheque_cancel(self, cheque_id: str):
        """ Cancel cheque 
        
        :param `cheque_id` [str]: Cheque id
        """
        return await self.request(method = 'cheque.cancel', json = {'cheque_id': cheque_id})


class Invoices:

    """ Invoice methods wrapper. 
    
    Available methods:
    
    * invoice_create()
    * invoice_status()
    * invoice_list()

    """

    async def invoice_create(self, currency: str, amount: Union[int, float], description: str = None, max_payments: int = 1, expires: int = None):
        """ Create invoice 
        
        :param `currency` [str]: Currency of invoice
        :param `amount` Union[int, float]: Amount of invoice
        :param `description` [str]: Description of invoice
        :param `max_payments` [int]: Max payments
        """
        return await self.request(
            method = 'invoice.create', 
            json = {
                'currency': currency.lower(),
                'amount': amount,
                'description': description,
                'max_payments': max_payments,
                'expires': expires
            }
        )

    async def invoice_status(self, invoice_id: str):
        """ Get invoice status
        
        :param `invoice_id` [str]: Invoice id
        """
        return await self.request(method = 'invoice.status', params = {'invoice_id': invoice_id})

    async def invoice_list(self):
        """ Get invoice list """
        return await self.request(method = 'invoice.list')


class NFT:

    """ NFT methods wrapper. 
    
    Available methods:
    
    * nft_list()
    * nft_transfer()

    """

    async def nft_list(self):
        """ List your NFTs """
        return await self.request(method = 'nft.list')

    async def nft_transfer(self, nft_address: str, to_address: str):
        """nft_transfer

        Args:
            nft_address (str): NFT Item contract address
            to_address (str): Transfer recipient address
        """
        return await self.request(
            method = 'nft.transfer',
            json = self.sign_message({
                'nft_address': nft_address,
                'to_address': to_address
            }) 
        )
        

class Exchanges:

    """ Exchange methods wrapper. 
    
    Available methods:
    
    * pairs()
    * estimate()
    * create_order()
    * order_status()

    """

    async def pairs(self):
        """ Get list of pairs """
        return await self.request(method = 'exchanges.pairs', request_method = 'GET')

    async def estimate(self, pair: list, action_type: str, amount: Union[int, float]):
        """ Estimate

        :param `pair` [list]: Pair
        :param `type` [str]: Type
        :param `amount` Union[int, float]: Amount
        
        """
        return await self.request(
            method = 'exchanges.estimate', 
            json = {
                'pair': pair, 'type': action_type, 'amount': amount
            }
        )

    async def create_order(self, pair: list, action_type: str, amount: Union[int, float], min_excepted_amount: Union[int, float]):
        """ Create order

        :param `pair` [list]: Pair
        :param `action_type` [str]: Action type
        :param `amount` Union[int, float]: Amount
        :param `min_excepted_amount` Union[int, float]: Min excepted amount
        
        """
        return await self.request(
            method = 'exchanges.createOrder', 
            json = self.sign_message({
                'pair': pair, 'type': action_type, 'amount': amount, 'min_expected_amount': min_excepted_amount
            })
        )

    async def order_status(self, order_id: str):
        """ Get order status
        
        :param `order_id` [str]: Order id
        """
        return await self.request(method = 'exchanges.orderStatus', params = {'id': order_id})
