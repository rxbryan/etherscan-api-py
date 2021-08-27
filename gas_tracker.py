from etherscan_api import etherscanApi
from etherscan_api import etherscanApiExceptions

class GasTracker(etherscanApi):
    def __init__(self, apikey):
        etherscanApi.__init__(self, apikey)
    
    def estimate_confirmation_time(self, gasprice):
        #gas price = price paid per unit of gas, in wei
        self.url_bits = ['gastracker',
            self.action,'gasestimate',
            self.gasprice, str(gasprice),
            self.apikey, self.key]
            
        self.generate_url()
        
        try:
            self.get()
        except etherscanApiExceptions as e:
                print(e)
        else:
            if self.response['message'] == 'OK':
                print(self.response['result'])
                return self.response['result']
            else:
                self.print_error_message()
        return None
        
    def gasoracle(self):
        self.url_bits = ['gastracker',
            self.action, 'gasoracle',
            self.apikey, self.key]
            
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
                print(e)
        else:
            print(self.response)
            return self.response
        return None
    
    '''date is in the format yyyy-MM-dd, sort : use 'asc' to sort by ascending
    and 'desc' to sort by descending'''   
    def eth_daily_avg(self, startdate, enddate, sort, mode):
        _action = ''
        if mode == 'gaslimit':
            _action = 'dailyavggaslimit'
        elif mode == 'gasused':
            _action = 'dailygasused'
        elif mode == 'gasprice':
            _action = 'dailyavggasprice'
        
        self.url_bits = ['stats', 
        self.action, _action,
        self.startdate, startdate,
        self.enddate, enddate,
        self.sort, sort,
        self.apikey, self.key]
        
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
                print(e)
        else:
            if self.response['message'] == 'OK':
                print(self.response['result'])
                return self.response['result']
            else:
                self.print_error_message()
        return None
        
    def eth_daily_avg_gaslimit(self, startdate, enddate, sort='asc'):
        return self.eth_daily_avg(startdate, enddate, sort, mode='gaslimit')
        
    def eth_daily_gasused(self, startdate, enddate, sort='asc'):
        return self.eth_daily_avg(startdate, enddate, sort, mode='gasused')
        
    def eth_daily_avg_gasprice(self, startdate, enddate, sort='asc'):
        return self.eth_daily_avg(startdate, enddate, sort, mode='gasprice')
