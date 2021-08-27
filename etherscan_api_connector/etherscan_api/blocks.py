from etherscan_api import etherscanApi
from etherscan_api import etherscanApiExceptions

class Blocks(etherscanApi):
    def __init__(self, apikey):
        etherscanApi.__init__(self, apikey)

    def get_blk_uncle_reward(self, blockno):
        self.url_bits = ['block',
        self.action, 'getblockreward',
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
        
    def get_estimated_blk_cntdwn_time(self, blockno):
        self.url_bits = ['block',
        self.action, 'getblockcountdown',
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
        
    def get_blk_no_by_timestamp(self, timestamp, closest='before'):
        #timesamp = unix timestamp in secs
        self.url_bits = ['block',
        self.action, 'getblocknobytime',
        self.timestamp, str(timestamp),
        self.closest, closest,
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
        
    def get_daily_avg(self, _action, startdate, enddate, sort):
        ''' startdate, enddate is in yyyy-MM-dd format, sort = 'asc'
        or 'desc' '''
        self.url_bits = ['stats',
        self.action, _action,
        self.startdate, startdate,
        self.enddate, enddate,
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
                return self.response['result']
            else:
                self.print_error_message()

    def get_daily_avg_blk_size(self, startdate, enddate, sort='asc'):
        ''' startdate, enddate is in yyyy-MM-dd format, sort = 'asc'
        or 'desc' '''
        return self.get_daily_avg('dailyavgblocksize', startdate, enddate, sort)
     
    def get_daily_blk_cnt_rewards(self, startdate, enddate, sort='asc'):
        ''' startdate, enddate is in yyyy-MM-dd format, sort = 'asc'
        or 'desc' '''
        return self.get_daily_avg('dailyblkcount', startdate, enddate, sort)
        
    def get_daily_blk_rewards(self, startdate, enddate, sort='asc'):
        return self.get_daily_avg('dailyblockrewards', startdate, enddate, sort)
        
    def get_blk_mining_time(self, startdate, enddate, sort='asc'):
        return self.get_daily_avg('dailyavgblocktime', startdate, enddate, sort)
        
    def get_uncle_blk_cnt_rewards(self, startdate, enddate, sort='asc'):
        return self.get_daily_avg('dailyuncleblkcount', startdate, enddate, sort)
