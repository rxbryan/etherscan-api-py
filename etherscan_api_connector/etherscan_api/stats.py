from etherscan_api import etherscanApi
from etherscan_api import etherscanApiExceptions

class Stats(etherscanApi):
    def __init__(self, apikey, address=''):
        etherscanApi.__init__(self, apikey, address)

    def eth_stats(self, _action):
        self.url_bits = ['stats',
            self.action,_action,
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
                
    def eth_totalsupply(self):
        return self.eth_stats('ethsupply')
        
    def eth_lastprice(self):
        return self.eth_stats('ethprice')
        
    '''startdate, enddate is date in the format yyyy-MM-dd; sort: sorting
    preference can be either 'asc' or'desc'; clienttype: the Etherum node
    client to use, either 'geth' or 'parity'; syncmode: type of no to run
    on, either 'default' or 'archive' '''
    def eth_nodesize(self, startdate, enddate, clienttype, 
        syncmode, sort='asc'):
        self.url_bits = ['stats', 
        self.action, 'chainsize',
        self.startdate, startdate,
        self.enddate, enddate,
        self.clienttype, clienttype,
        self.syncmode, syncmode,
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
        
    def eth_total_nodecount(self):
        return self.eth_stats('nodecount')
    
    '''startdate, enddate is date in the format yyyy-MM-dd; sort: sorting
    preference can be either 'asc' or'desc' '''
    def etherscan_pro_stats_apis(self, _action, startdate, enddate, sort):
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
        
        
    def daily_txn_fee(self, startdate, enddate, sort='asc'):
        return self.etherscan_pro_stats_apis('dailytxnfee', startdate, enddate, sort)
        
    def eth_daily_newaddress_cnt(self, startdate, enddate, sort='asc'):
        return self.etherscan_pro_stats_apis('dailynewaddress', startdate, enddate, sort)
        
    def eth_daily_network_utilisation(self, startdate, enddate, sort='asc'):
        return self.etherscan_pro_stats_apis('dailynetutilization', startdate, enddate, sort)
        
    def eth_daily_avg_hash_rate(self, startdate, enddate, sort='asc'):
        return self.etherscan_pro_stats_apis('dailyavghashrate', startdate, enddate, sort)
        
    def eth_daily_txn_cnt(self, startdate, enddate, sort='asc'):
        return self.etherscan_pro_stats_apis('dailytx', startdate, enddate, sort)
        
    def eth_daily_avg_net_difficulty(self, startdate, enddate, sort='asc'):
        return self.etherscan_pro_stats_apis('dailyavgnetdifficulty', startdate, enddate, sort)
        
    def eth_hist_daily_mktcap(self, startdate, enddate, sort='asc'):
        return self.etherscan_pro_stats_apis('ethdailymarketcap', startdate, enddate, sort)
    
    def eth_hist_daily_price(self, startdate, enddate, sort='asc'):
        return self.etherscan_pro_stats_apis('ethdailyprice', startdate, enddate, sort)
