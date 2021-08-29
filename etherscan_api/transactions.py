from etherscan_api import etherscanApi
from etherscan_api import etherscanApiExceptions

class Transactions(etherscanApi):
    def __init__(self, apikey):
        etherscanApi.__init__(self, apikey=apikey)

    def get_contract_execution_status(self, txhash):
        self.url_bits = ['transaction',
        self.action, 'getstatus',
        self.txhash, txhash,
        self.apikey,self.key
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

    def get_transaction_receipt_status(self, txhash):
        self.url_bits = ['transaction',
        self.action, 'gettxreceiptstatus',
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
                return self.response['result']
            else:
                self.print_error_message()
