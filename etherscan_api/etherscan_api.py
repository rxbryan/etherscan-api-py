import time
import requests
from requests.exceptions import RequestException

class etherscanApiExceptions(RequestException):
    '''An error occurred'''
    pass

class etherscanApi (object):
    
    url = ''
    url_bits = []
    response = {}
    csv = []

    prefix = 'https://api.etherscan.io/api'
    module = '?module='
    action = '&action='
    address = '&address='
    tag = '&tag='
    apikey = '&apikey='
    startblock = '&startblock='
    endblock = '&endblock='
    page = '&page='
    offset = '&offset='
    sort = '&sort='
    txhash = '&txhash='
    contractaddress = '&contractaddress='
    blocktype = '&blocktype='
    blockno = '&blockno='
    guid = ''
    timestamp = '&timestamp='
    closest = '&closest='
    startdate = '&startdate='
    enddate = '&enddate='
    fromBlock = '&fromBlock='
    toBlock = '&toBlock='
    topic0 = '&topic0='
    topic1 = '&topic1='
    topic2 = '&topic2='
    topic3 = '&topic3='
    topic0_1_opr = '&topic0_1_opr='
    topic1_2_opr = '&topic1_2_opr='
    topic2_3_opr = '&topic2_3_opr='
    topic0_2_opr = '&topic0_2_opr='
    topic0_3_opr = '&topic0_3_opr='
    topic1_3_opr = '&topic1_3_opr='
    boolean = '&boolean='
    index = '&index='
    _hex = '&hex='
    to = '&to='
    data = '&data='
    position = '&position='
    value = '&value='
    gasPrice = '&gasPrice='
    gasprice = '&gasPrice='
    gas = '&gas='
    clienttype = '&clienttype='
    syncmode = '&syncmode='

    def __init__(self, apikey, address=''):
        self.key = apikey
        self.blk_address = address
        
    def generate_url(self):
        self.url = self.prefix + self.module
        for bit in self.url_bits:
            self.url += bit
        print(self.url)
        
    def get(self):
        with requests.Session() as session:
            try:
                self.response = session.get(self.url, timeout=(5,5))
            except RequestException as e:
                raise etherscanApiExceptions(e)
            else:
                self.response = self.response.json()

    def parse_dump(self, dump, dict_keys):
        pl = []
        for ln in dump:
            for key in dict_keys:
                pl.append('{}: {}\n'.format(key, ln[key]))
        return pl

    def create_csv(self, dump, dict_keys):
        #write header
        #return dump
        ln = ''
        csv = []
        csv_header = ''
        for key in dict_keys:
            csv_header += key + ','
        csv_header += '\n'
        csv.append(csv_header)

        for c in dump:
            #print(dump)
            for key in dict_keys:
                if key in c:
                    ln += c[key] + ','
            ln += '\n'
            csv.append(ln)
            time.sleep(0.01)
        return csv

    def post():
        pass

    def print_error_message(self):
        print('{} returned error message {}'.format(self.url, self.response['message']))
