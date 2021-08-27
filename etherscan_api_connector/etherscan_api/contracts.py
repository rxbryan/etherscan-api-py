from etherscan_api import etherscanApi
from etherscan_api import etherscanApiExceptions

class Contracts (etherscanApi):
    
    #keys for parsing contract source code
    contract_src = [
                'SourceCode',
                'ABi',
                'ContractName',
                'CompilerVersion',
                'OptimizationUsed',
                'Runs',
                'ConstructorArguments',
                'EVMVersion',
                'Library',
                'LicenseType',
                'Proxy',
                'Implementation',
                'SwarmSource'
                ]

    def __init__(self, contract_address, apikey):
        etherscanApi.__init__(self, apikey=apikey)
        self.contractaddress = contract_address
        
    def get_contract_ABI(self):
        self.url_bits = ['contract', 
        self.action, 'getabi', 
        self.address,self.contractaddress,
        self.apikey, self.key]
        self.generate_url()
        #not sure if this works
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            print(self.response['result']) #debug
            return self.response['result']
        
    def get_contract_source(self):
        self.url_bits = ['contract',
        self.action, 'getsourcecode',
        self.address, self.contractaddress,
        self.apikey, self.key]
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
            print(e)
        else:
            ret = self.parse_dump(self.response['result'], self.scontract_src)
            return ret
