from etherscan_api import etherscanApi

class Transactions(etherscanApi):
    def __init__(self, apikey):
        etherscanApi.__init__(self, apikey=apikey)

    def get_contract_execution_status(self, txhash):
        self.url_bits = ['transaction',
        self.action, 'getstatus',
        self.txhash, txhash,
        self.apikey,self.key]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
                print(e)
                return None
        else:
            if self.response['message'] == 'OK':
                print(self.response['result'])
                return self.response['result']
            else:
                self.print_error_message()
                return None

    def get_transaction_receipt_status(self, txhash):
        self.url_bits = ['transaction',
        self.action, 'gettxreceiptstatus',
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
                print(self.response['result'])
                return self.response['result']
            else:
                self.print_error_message()
                return None
