from etherscan_api import etherscanApi
from etherscan_api import etherscanApiExceptions

class Tokens(etherscanApi):
    def __init__(self,apikey, address=''):
        etherscanApi.__init__(self, address=address, apikey=apikey)

    def get_tokensupply(self, contractaddress):
        self.url_bits = ['stats',
        self.action, 'tokensupply',
        self.contractaddress, contractaddress, 
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
         
    def get_erc20_tokenbalance(self, contractaddress, tag='latest', address=''):
        if not address:
            address = self.blk_address
        self.url_bits = ['account', 
        self.action, 'tokenbalance',
        self.contractaddress, contractaddress, 
        self.address, address,
        self.tag, tag, 
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

    def get_tokensupplyhistory(self, contractaddress, blockno):
        self.url_bits = ['stats', 
        self.action,'tokensupplyhistory',
        self.contractaddress, contractaddress, 
        self.blockno, str(blockno),
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

    def get_tokenbalancehistory(self,contractaddress, blockno, address=''):
        if not address:
            address = self.blk_address
        
        self.url_bits = ['account', 
        self.action, 'tokenbalancehistory',
        self.contractaddress, contractaddress, 
        self.address, address,
        self.blockno, str(blockno), 
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

    def get_tokeninfo(self, contractaddress):
        self.url_bits = ['token', 
        self.action, 'tokeninfo',
        self.contractaddress, contractaddress, 
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
                     
