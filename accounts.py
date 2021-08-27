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
            return None
        else:
            if  self.response['message'] == 'OK':
                if _action == 'balancemulti':
                    return create_csv(self.response['result'], self.multi_bal)
                else:
                    return self.response['result']
            else:
                self.print_error_message()
                return None

    def get_multiple_balances(self, _address='', tag='latest'):
        ret = self.get_balance(tag=tag, _address=_address, _action='balancemulti')
        return ret

    def get_all_transactions(self, startblock=0, endblock=99999999, page=1, offset=1000, sort='asc'):
        txlist = []
        while 1:
            module_action = 'txlist'
            self.url_bits = ['account',
            self.action, module_action,
            self.address, self.blk_address,
            self.startblock, str(startblock), 
            self.endblock, str(endblock), 
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
                break
            else:
                if self.response['message'] == 'OK':
                    txlist.append(self.response['result'])
                    print('{}'.format(page))
                else:
                    self.print_error_message()
                    break
            page += 1
        return create_csv(txlist, self.tx_keys)
        

    def get_internal_transactions(self, endblock, startblock=0, page=1, offset=1000, sort='asc'):
        txlist = []
        while 1:
            module_action = 'txlistinternal'
            self.url_bits = ['account',
            self.action, module_action,
            self.address, self.blk_address,
            self.startblock, str(startblock), 
            self.endblock, str(endblock), 
            self.page, str(page),
            self.offset, str(offset),
            self.sort, sort,
            self.apikey, self.key]
            
            self.generate_url()       
            try:
                self.get()
            except etherscanApiExceptions as e:
                print(e)
                break
            else:
                if self.response['message'] == 'OK':
                    txlist.append(self.response['result'])
                    print('{}'.format(page))
                else:
                    self.error_message()
                    break
            page += 1
        return create_csv(txlist, self.internal_tx_keys)

    def get_internal_txhash(self, txhash):
        module_action = 'txlistinternal'
        self.url_bits = ['account',
        self.action, module_action,
        self.txhash, txhash,
        self.apikey, self.key]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
            return None
        else:
            if self.response['message'] == 'OK':
                return parse_dump(self.response['result'], self.internal_tx_keys)
            else:
                self.print_error_message()
            return None
         

    def get_internal_blk(self, endblock, startblock=0, page=1, offset=1000, sort='asc'):
        txlist = []
        while 1:
            module_action = 'txlistinternal'
            self.url_bits = ['account',
            self.action, module_action,
            self.startblock, str(startblock), 
            self.endblock, str(endblock), 
            self.page, str(page),
            self.offset, str(offset),
            self.sort, sort,
            self.apikey, self.key]
             
            self.generate_url()
            try:
                self.get()
            except etherscanApiExceptions as e:
                print(e)
                break
            else:
                if self.response['message'] == 'OK':
                    txlist.append(self.response['result'])
                    print('{}'.format(page))
                else:
                    self.print_error_message()
                    break
            page += 1
        return create_csv(txlist, self.internal_tx_keys)
        
    def get_erc20_transfer_events(self, contractaddress='', page=1, offset=1000, sort='asc'):

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
        while 1:
            module_action = 'tokentx'
            self.url_bits = ['account',
            self.action, module_action,
            temp_contractaddress, contractaddress,
            temp_address, self.blk_address,
            self.page, str(page),
            self.offset, str(offset),
            self.sort, sort,
            self.apikey, self.key]

            self.generate_url()       
            try:
                self.get()
            except etherscanApiExceptions as e:
                print(e)
                break
            else:
                if self.response['message'] == 'OK':
                    txlist.append(self.response['result'])
                    print('{}'.format(page))
                else:
                    self.print_error_message()
                    break
            page += 1
        return create_csv(txlist, self.erc20_tx_keys)
        
    def get_erc721_transfer_events(self, contractaddress = '', page=1, offset=1000, sort='asc'):
        
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
        while 1:
            module_action = 'tokennfttx'
            self.url_bits = ['account',
            self.action, module_action,
            temp_contractaddress, contractaddress,
            temp_address, self.blk_address,
            self.page, str(page),
            self.offset, str(offset),
            self.sort, sort,
            self.apikey, self.key]
            
            self.generate_url()
            try:
                self.get()
            except etherscanApiExceptions as e:
                print(e)
                break
            else:
                if self.response['message'] == 'OK':
                    txlist.append(self.response['result'])
                    print('{}'.format(page))
                else:
                    self.print_error_message()
                    break
            page += 1
        return create_csv(txlist, self.erc721_tx_keys)
        

    def get_blocks_mined(self, blocktype='blocks', page=1, offset=1000):
        
        blks_mined = []
        while 1:
            module_action = 'getminedblocks'
            self.url_bits = ['account',
            self.action, module_action,
            self.address, self.blk_address,
            self.blocktype, blocktype,
            self.page, str(page),
            self.offset, str(offset),
            self.apikey, self.key]
            
            self.generate_url()
            try:
                self.get()
            except etherscanApiExceptions as e:
                print(e)
                break
            else:
                if self.response['message'] == 'OK':
                    blks_mined.append(self.response['result'])
                    print('{}'.format(page))
                else:
                    self.print_error_message()
                    break
            page += 1
        return create_csv(blks_mined, self.minedblocks_keys)
        
    def get_historical_ether_balance(self, blockno):  #requires pro api
        module_action = 'balancehistory'
        self.url_bits = ['account',
        self.action, module_action,
        self.address, self.blk_address,
        self.blockno,str(blockno),
        self.apikey, self.key]
        
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
            return None
        else:
            if self.response['message'] == 'OK':
                print(self.response['result'])
            else:
                self.print_error_message

        return self.response['result']
        
