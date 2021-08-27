from etherscan_api import etherscanApi
from etherscan_api import etherscanApiExceptions

class Proxy(etherscanApi):
    def __init__(self,  apikey, address=''):
        etherscanApi.__init__(self, apikey, address)

    def get_most_recent_block(self):
        self.url_bits = ['proxy',
        self.action,'eth_blockNumber',
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            return self.response['result']

    def get_block_info(self, tag, boolean):
        #tag = blockno in hx, boolean :'true' or 'false'
        if boolean:
            boolean = 'true'
        elif not boolean:
            boolean = 'false'

        self.url_bits = ['proxy',
        self.action, 'eth_getBlockByNumber',
        self.tag, str(tag),
        self.boolean, boolean,
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            return self.response['result']

    def get_uncle_info(self, tag, index):
        '''tag = blockno in hex,index: position of the uncle's index 
        in the block in hex'''
        self.url_bits = ['proxy',
        self.action, 'eth_getUncleByBlockNumberAndIndex',
        self.tag, str(tag),
        self.index, str(index),
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            return self.response['result']

    def get_no_of_transactions_blk(self, tag):#tag: block no in hex
        self.url_bits = ['proxy',
        self.action, 'eth_getBlockTransactionCountByNumber',
        self.tag, str(tag),
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            return self.response['result']

    def get_transaction_info_byhash(self, txhash):
        self.url_bits = ['proxy',
        self.action,'eth_getTransactionByHash',
        self.txhash, txhash,
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            return self.response['result']

    def get_transaction_info_blkno_index(self, tag, index):
        '''tag = blockno in hex, index: position of uncle's 
        index in block, in hex'''
        self.url_bits = ['proxy',
        self.action, 'eth_getTransactionByBlockNumberAndIndex',
        self.tag, str(tag),
        self.index, str(index),
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            return self.response['result']

    def eth_submit_rawtransactions(self, hex_data): 
        #hex = string representing signed raw data.
        #not sure thisworks
        self.url_bits = ['proxy',
        self.action, 'eth_sendRawTransaction',
        self._hex, str(hex_data),
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            return self.response['result']

    def eth_getTransactionReceipt(self, txhash):
        self.url_bits = ['proxy',
        self.action, 'eth_getTransactionReceipt',
        self.txhash, txhash,
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            return self.response['result']

    def eth_call(self, data, tag, to=''):
        #have't been able to test this
        #to = address to interact with
        
        if not to:
            to = self.blk_address
        self.url_bits = ['proxy',
        self.action, 'eth_call',
        self.to, to,
        self.data, data,
        self.tag, tag,
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            return self.response['result']

    def eth_getCode(self, tag, _address=''):
        #tag can either be 'earliest' or 'latest'
        if not _address:
            _address = self.blk_address
        self.url_bits = ['proxy',
        self.action, 'eth_getCode',
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
            return self.response['result']

    def eth_getstorageAt(self, position, tag, _address=''):
        '''This endpoint is still experimental and may have potential issues
        position = hex code of position in storage
        tag = ''earliest' or 'latest' '''

        if not _address:
            _address = self.blk_address

        self.url_bits = ['proxy',
        self.action, 'eth_getStorageAt',
        self.address, _address,
        self.position, str(position),
        self.tag, tag,
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            return self.response['result']

    def eth_gasPrice(self):
        self.url_bits = ['proxy',
        self.action, 'eth_gasPrice',
        self.apikey, self.key]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)           
        else:
            print(self.response['result'])
            return self.response['result']
        
    def eth_estimateGas(self, data, value, gas, gasPrice, to=''):
        ''' to = address to interact with; data = hash of the 
        method signature and encoded parameters; value = value  
        sent in this, transaction, in hex; gas = amount of gas 
        provided for this transaction in hex, gasPrice is in wei'''

        if not to:
            to = self.blk_address

        self.url_bits = ['proxy',
        self.action, 'eth_estimateGas',
        self.data, str(data),
        self.to, to,
        self.value, str(value),
        self.gasPrice, str(gasPrice),
        self.gas, str(gas),
        self.apikey, self.key
        ]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print (e)
        else:
            return self.response
