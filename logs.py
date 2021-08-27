from etherscan_api import etherscanApi
from etherscan_api import etherscanApiExceptions

class Logs(etherscanApi):
    log = {}
    
    def __init__(self, log_address, apikey):
        etherscanApi.__init__(self, address=log_address, apikey=apikey)
        
    '''#fromBlock, toBlock = block no in decimal; topic(opr) can either
    be 'and' or 'or'; visit https://docs.etherscan.io/api-endpoints/logs
    for more up to date docs'''
    def get_event_logs(self, fromBlock, toBlock='latest', topic0='',
            topic0_1_opr = 'and',topic1='', topic1_2_opr='and',
            topic2='', topic2_3_opr='and',topic3='', topic0_2_opr='and',
            topic0_3_opr='and', topic1_3_opr='and'):
            
        self.url_bits = ['logs',
        self.action, 'getlogs', 
        self.fromBlock, fromBlock, 
        self.toBlock, toBlock, 
        self.address, self.blk_address, 
        self.topic0, topic0]
        hold = []
        if topic1 and topic2 and topic3:
            hold.extend([ 
            self.topic0_1_opr, topic0_1_opr, 
            self.topic1, topic1,
            self.topic1_2_opr, topic1_2_opr,
            self.topic2, topic2,
            self.topic2_3_opr, topic2_3_opr,
            self.topic3, topic3])
        elif topic1 and topic2:
            hold.extend([ self.topic0_1_opr, topic0_1_opr,
            self.topic1, topic1,
            self.topic1_2_opr, topic1_2_opr, 
            self.topic2, topic2])
        elif topic1:
            hold.extend([ 
            self.topic0_1_opr, topic0_1_opr, 
            self.topic1, topic1])
        hold.extend([self.apikey, self.key])
        self.url_bits.extend(hold)
        self.generate_url()
        try:
            self.get()
        except etherscanApiExceptions as e:
                print(e)
                return None
        else:
                print(self.response)
                return self.response
           #i'm unable to test this for now
