
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

    async def withdraw(self, ton_address: str, currency: str, amount: float):
        """ Withdraw funds 
        
        :param `ton_address` [str]: TON address
        :param `currency` [str]: Currency of withdraw
        :param `amount` [float]: Amount of withdraw
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

    async def cheque_create(self, currency: str, amount: int, expires: int = None, description: str = '', activates_count: int = 1, groups_id: list = None, personal_id: str = None, password: str = None, **kwargs):
        """ Create cheques 
        
        :param `currency` [str]: Currency of cheque
        :param `amount` [int]: Amount of cheque
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

    async def invoice_create(self, currency: str, amount: int, description: str = None, max_payments: int = 1):
        """ Create invoice 
        
        :param `currency` [str]: Currency of invoice
        :param `amount` [int]: Amount of invoice
        :param `description` [str]: Description of invoice
        :param `max_payments` [int]: Max payments
        """
        return await self.request(
            method = 'invoice.create', 
            json = {
                'currency': currency.lower(),
                'amount': amount,
                'description': description,
                'max_payments': max_payments
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

