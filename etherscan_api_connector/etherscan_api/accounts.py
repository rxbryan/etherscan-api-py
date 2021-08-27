from etherscan_api import etherscanApi 
from etherscan_api import etherscanApiExceptions

class Accounts (etherscanApi):

    #keys for the result dictionary
    multi_bal = [
            'account',
            'balance'
            ]
    tx_keys = [
            'blockNumber',
            'timeStamp',
            'hash',
            'nonce',
            'blockHash',
            'transactionIndex',
            'from',
            'to',
            'value',
            'gas',
            'gasPrice',
            'isError',
            'txreceipt_status',
            'input',
            'contractAddress',
            'cumulativeGasUsed',
            'gasUsed',
            'confirmations'
            ]
    internal_tx_keys = [
            'blockNumber',
            'timeStamp',
            'hash',
            'from',
            'to',
            'value',
            'contractAddress',
            'input',
            'type',
            'gas',
            'gasUsed',
            'traceId',
            'isError',
            'errCode'
            ]
    erc20_tx_keys = [
            'blockNumber',
            'timeStamp',
            'hash',
            'nonce',
            'blockHash',
            'from',
            'contractAddress',
            'to',
            'value',
            'tokenName',
            'tokenSymbol',
            'tokenDecimal',
            'transactionIndex',
            'gas',
            'gasPrice',
            'gasUsed',
            'cumulativeGasUsed',
            'input',
            'confirmations'
            ]
    erc721_tx_keys = [
            'blockNumber',
            'timeStamp',
            'hash',
            'nonce',
            'blockHash',
            'from',
            'contractAddress',
            'to',
            'tokenID',
            'tokenName',
            'tokenSymbol',
            'tokenDecimal',
            'transactionIndex',
            'gas',
            'gasPrice',
            'gasUsed',
            'cumulativeGasUsed',
            'input',
            'confirmations'
            ]
    minedblocks_keys = [
            'blockNumber',
            'timeStamp',
            'blockReward'
            ]
    
    def __init__(self, apikey, address):
        etherscanApi.__init__(self, apikey, address)

    def get_balance(self, tag='latest', _address='', _action = 'balance'):
        if not  _address:
            _address = self.blk_address
        self.url_bits = ['account',
        self.action, _action,
        self.address, _address,
        self.tag, tag,
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            if  self.response['message'] == 'OK':
                if _action == 'balancemulti':
                    return self.create_csv(self.response['result'], self.multi_bal)
                else:
                    return self.response['result']
            else:
                self.print_error_message()

    def get_multiple_balances(self, _address='', tag='latest'):
        ret = self.get_balance(tag=tag, _address=_address, _action='balancemulti')
        return ret

    def get_all_transactions(self, startblock=0, endblock=99999999, sort='asc'):
        txlist = []
        self.url_bits = ['account',
        self.action, 'txlist',
        self.address, self.blk_address,
        self.startblock, str(startblock), 
        self.endblock, str(endblock), 
        self.sort, sort,
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
                print(e)
        else:
            if self.response['message'] == 'OK':
                txlist=self.response['result']
            else:
                self.print_error_message()
        return self.create_csv(txlist, self.tx_keys)
        

    def get_internal_transactions(self, endblock, startblock=0, sort='asc'):
        txlist = []
        self.url_bits = ['account',
        self.action, 'txlistinternal',
        self.address, self.blk_address,
        self.startblock, str(startblock), 
        self.endblock, str(endblock), 
        self.sort, sort,
        self.apikey, self.key
        ]
        self.generate_url()       
        try:
            self.get()
        except etherscanApiExceptions as e:
                print(e)
        else:
            if self.response['message'] == 'OK':
                txlist.append(self.response['result'])
            else:
                self.print_error_message()
        return self.create_csv(txlist, self.internal_tx_keys)

    def get_internal_txhash(self, txhash):
        self.url_bits = ['account',
        self.action, 'txlistinternal',
        self.txhash, txhash,
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            if self.response['message'] == 'OK':
                return self.parse_dump(self.response['result'], self.internal_tx_keys)
            else:
                self.print_error_message()

    def get_internal_blk(self, endblock, startblock=0, sort='asc'):
        txlist = []
        self.url_bits = ['account',
        self.action, 'txlistinternal',
        self.startblock, str(startblock), 
        self.endblock, str(endblock), 
        self.sort, sort,
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)

        else:
            if self.response['message'] == 'OK':
                txlist.append(self.response['result'])
            else:
                self.print_error_message()
        return self.create_csv(txlist, self.internal_tx_keys)
        
    def get_erc20_transfer_events(self, contractaddress='', sort='asc'):
        temp_address = ''
        temp_contractaddress = ''
        if self.blk_address and contractaddress:
            temp_address = self.address
            temp_contractaddress = self.contractaddress
        elif contractaddress:
            temp_contractaddress = self.contractaddress
        elif self.blk_address:
            temp_address = self.address
        else:
            raise etherscanApiExceptions('parameters for get_erc20_transfer_events invalid')
    
        txlist = []
        self.url_bits = ['account',
        self.action, 'tokentx',
        temp_contractaddress, contractaddress,
        temp_address, self.blk_address,
        self.sort, sort,
        self.apikey, self.key
        ]
        self.generate_url()       
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            if self.response['message'] == 'OK':
                txlist.append(self.response['result'])
            else:
                self.print_error_message()
        return self.create_csv(txlist, self.erc20_tx_keys)

    def get_erc721_transfer_events(self, contractaddress = '', sort='asc'):
        
        temp_address = ''
        temp_contractaddress = ''
        if self.blk_address and contractaddress:
            temp_address = self.address
            temp_contractaddress = self.contractaddress
        elif contractaddress:
            temp_contractaddress = self.contractaddress
        elif self.blk_address:
            temp_address = self.address
        else:
            raise etherscanApiExceptions('parameters for get_erc721_transfer_events invalid')

        txlist = []
        self.url_bits = ['account',
        self.action, 'tokennfttx',
        temp_contractaddress, contractaddress,
        temp_address, self.blk_address,
        self.page, str(page),
        self.offset, str(offset),
        self.sort, sort,
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            if self.response['message'] == 'OK':
                txlist.append(self.response['result'])
            else:
                self.print_error_message()
        return self.create_csv(txlist, self.erc721_tx_keys)

    def get_blocks_mined(self, blocktype='blocks'):
        blks_mined = []
        self.url_bits = ['account',
        self.action, 'getminedblocks',
        self.address, self.blk_address,
        self.blocktype, blocktype,
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            if self.response['message'] == 'OK':
                blks_mined.append(self.response['result'])
            else:
                self.print_error_message()
        return self.create_csv(blks_mined, self.minedblocks_keys)
        
    def get_historical_ether_balance(self, blockno):  #requires pro api
        self.url_bits = ['account',
        self.action, 'balancehistory',
        self.address, self.blk_address,
        self.blockno,str(blockno),
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            if self.response['message'] == 'OK':
                return self.response['result']
            else:
                self.print_error_message()
