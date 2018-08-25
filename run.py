""" Coinapi key generator and data downloader

Example, try:
python run.py --symbol=BITSTAMP_SPOT_LTC_USD  --source=ohlcv --from=2018-08-23 --proxy_type=rotate --period=1HRS --filetype=csv --timeout=20
python run.py --exchange=BITSTAMP  --source=ohlcv --from=2018-08-23 --proxy_type=rotate --period=1HRS --filetype=csv --limit=100000
python run.py --exchange=BITSTAMP  --source=trades --from=2018-08-23 --proxy_type=rotate --period=1HRS --filetype=csv --limit=100000
python run.py --symbol=BINANCE_SPOT_BTC_USDT,BINANCE_SPOT_ETH_USDT,BINANCE_SPOT_EOS_USDT,BINANCE_SPOT_ETH_BTC,BINANCE_SPOT_ONT_USDT,BINANCE_SPOT_BCC_USDT,BINANCE_SPOT_EOS_BTC,BINANCE_SPOT_ETC_USDT,BINANCE_SPOT_ONT_BTC,BINANCE_SPOT_NANO_BTC,BINANCE_SPOT_TRX_USDT,BINANCE_SPOT_BCC_BTC,BINANCE_SPOT_XRP_BTC,BINANCE_SPOT_ETC_BTC,BINANCE_SPOT_XRP_USDT,BINANCE_SPOT_VET_USDT,BINANCE_SPOT_TRX_BTC,BINANCE_SPOT_ADA_USDT,BINANCE_SPOT_NEO_USDT,BINANCE_SPOT_XLM_BTC,BINANCE_SPOT_CMT_BTC,BINANCE_SPOT_VET_BTC,BINANCE_SPOT_NEO_BTC,BINANCE_SPOT_ADA_BTC,BINANCE_SPOT_LTC_USDT,BINANCE_SPOT_THETA_BTC,BINANCE_SPOT_LTC_BTC,BINANCE_SPOT_IOTA_USDT,BINANCE_SPOT_BNB_BTC,BINANCE_SPOT_BNB_USDT,BINANCE_SPOT_XLM_USDT,BINANCE_SPOT_TUSD_USDT,BINANCE_SPOT_ICX_USDT,BINANCE_SPOT_IOTA_BTC,BINANCE_SPOT_ZRX_BTC,BINANCE_SPOT_ICX_BTC,BINANCE_SPOT_WTC_BTC,BINANCE_SPOT_XMR_BTC,BINANCE_SPOT_ARN_BTC,BINANCE_SPOT_TUSD_BTC,BINANCE_SPOT_LSK_BTC,BINANCE_SPOT_ZIL_BTC,BINANCE_SPOT_QKC_BTC,BINANCE_SPOT_DASH_BTC,BINANCE_SPOT_IOTX_BTC,BINANCE_SPOT_NANO_ETH,BINANCE_SPOT_DOCK_BTC,BINANCE_SPOT_NPXS_BTC,BINANCE_SPOT_NAS_BTC,BINANCE_SPOT_CMT_ETH,BINANCE_SPOT_YOYO_BTC,BINANCE_SPOT_EOS_ETH,BINANCE_SPOT_QTUM_USDT,BINANCE_SPOT_LINK_BTC,BINANCE_SPOT_GAS_BTC,BINANCE_SPOT_ELF_BTC,BINANCE_SPOT_IOST_BTC,BINANCE_SPOT_LOOM_BTC,BINANCE_SPOT_NCASH_BTC,BINANCE_SPOT_VET_ETH,BINANCE_SPOT_NULS_BTC,BINANCE_SPOT_WAN_BTC,BINANCE_SPOT_REP_BTC,BINANCE_SPOT_GTO_BTC,BINANCE_SPOT_KEY_BTC,BINANCE_SPOT_BNB_ETH,BINANCE_SPOT_CVC_BTC,BINANCE_SPOT_ADA_ETH,BINANCE_SPOT_DENT_BTC,BINANCE_SPOT_THETA_ETH,BINANCE_SPOT_XVG_BTC,BINANCE_SPOT_MDA_BTC,BINANCE_SPOT_POA_BTC,BINANCE_SPOT_IOST_ETH,BINANCE_SPOT_TRX_ETH,BINANCE_SPOT_BAT_BTC,BINANCE_SPOT_MFT_BTC,BINANCE_SPOT_ENG_BTC,BINANCE_SPOT_XRP_ETH,BINANCE_SPOT_XEM_BTC,BINANCE_SPOT_BQX_BTC,BINANCE_SPOT_NEO_ETH,BINANCE_SPOT_SNT_BTC,BINANCE_SPOT_NAS_ETH,BINANCE_SPOT_NULS_USDT,BINANCE_SPOT_ONT_ETH,BINANCE_SPOT_PPT_BTC,BINANCE_SPOT_AION_BTC,BINANCE_SPOT_SUB_BTC,BINANCE_SPOT_ADX_BTC,BINANCE_SPOT_QTUM_BTC,BINANCE_SPOT_LOOM_ETH,BINANCE_SPOT_ZRX_ETH,BINANCE_SPOT_ICX_ETH,BINANCE_SPOT_BCD_BTC,BINANCE_SPOT_STORM_BTC,BINANCE_SPOT_OMG_BTC,BINANCE_SPOT_BCC_ETH,BINANCE_SPOT_MTL_BTC,BINANCE_SPOT_ZEC_BTC --source=ohlcv --from=2018-08-23 --to=2018-08-24 --proxy_type=list --period=1HRS --filetype=csv --limit=100000 --timeout=10
python run.py --exchange=BINANCE --quote=USDT,BTC,ETH --base=BTC,ETH,EOS,ONT,BCC,ETC,NANO,TRX,XRP,VET,ADA,NEO,XLM,CMT,LTC,THETA,IOTA,BNB,TUSD,ICX,ZRX,WTC,XMR,ARN,LSK,ZIL,QKC,DASH,IOTX,DOCK,NPXS,NAS,YOYO,QTUM,LINK,GAS,ELF,IOST,LOOM,NCASH,NULS,WAN,REP,GTO,KEY,CVC,DENT,XVG,MDA,POA,BAT,MFT,ENG,XEM,BQX,SNT,PPT,AION,SUB,ADX,BCD,STORM,OMG,MTL,ZEC --source=ohlcv --from=2018-08-23 --to=2018-08-24 --proxy_type=list --period=1HRS --filetype=csv --limit=100000 --timeout=10


Usage:
  run.py (--symbol=<string> | [--exchange=<string>] [--base=<string>] [--quote=<string>] [--type=<string>]) --source=<string> --from=<date> [--to=<date>] [--period=<string>]  [--limit=<int>]  [--levels=<int>]  [--path=<path>] [--filetype=<string>] [--proxy_type=<string>] [--timeout=<int>] [--generate_keys=<int>] [--find_n_proxy=<int>] [--proxy_dnsbl] [--proxy_strict]
  run.py --continue [--path=<path>]
  run.py (-h | --help)

Arguments:
  --symbol=<string>     Symbol id for requested timeseries, comma separated, check https://docs.coinapi.io/#list-all-symbols
  --exchange=<string>     identifier of the exchange where symbol is traded, comma separated, check https://docs.coinapi.io/#list-all-symbols
  --base=<string>     FX Spot base asset identifier, for derivatives it’s contact underlying (e.g. BTC for BTC/USD), comma separated, check https://docs.coinapi.io/#list-all-symbols
  --quote=<string>     FX Spot quote asset identifier, for derivatives it’s contract underlying (e.g. USD for BTC/USD), comma separated, check https://docs.coinapi.io/#list-all-symbols
  --type=<string>     Type of symbol (possible values are: SPOT, FUTURES or OPTION), comma separated
  --from=<date>     starting date.
  --source=<string>     the data to be downloaded (ohlcv, trades, quotes, order).

Options:
  -h --help     Show this screen.
  --path=<path>  a directory to save data to [default: out].
  --filetype=<string>  the saved data file type (json, csv) [default: csv].
  --to=<date>  ending date.
  --period=<string>  supported time periods available for requesting OHLCV timeseries data OR to convert data to, check https://docs.coinapi.io/#list-all-periods.
  --limit=<int>  Amount of items to return , minimum is 1, maximum is 100000 [default: 10000].
  --levels=<int>  Maximum amount of levels from each side of the book to include in response, max 20 [default: 20].
  --timeout=<int>  request timeout [default: 120].
  --generate_keys=<int>  generate N new coinapi keys.
  --find_n_proxy=<int>  number of proxies to find at a time [default: 100].
  --proxy_type=<string>  type of proxy (None, fresh, list, rotate) [default: None].
  --proxy_dnsbl  Check proxy in spam databases (DNSBL) [default: False].
  --proxy_strict  strict proxy search [default: False].
  --continue  continue the last run [default: False].

"""

import asyncio
import json
import os
import random
import re
import urllib
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
from json import JSONDecoder, JSONEncoder
from time import sleep

import dateutil.parser
import requests

try:
    from docopt import docopt
    from schema import Schema, And, Or, Use, SchemaError
    import names
    from guerrillamail import GuerrillaMailSession, GuerrillaMailException
    from fake_useragent import UserAgent
    from proxybroker import Broker
    from proxybroker.resolver import Resolver
    import pandas as pd
except ImportError:
    exit('One or more of the required libraries is missing\n'
         'Use the following commands to install them:\n'
         'pip install schema\n'
         'pip install docopt\n'
         'pip install names\n'
         'pip install python-guerrillamail\n'
         'pip install fake-useragent\n'
         'pip install proxybroker\n'
         'pip install pandas\n'
         '\n')

periods = ["1SEC", "2SEC", "3SEC", "4SEC", "5SEC", "6SEC", "10SEC", "15SEC", "20SEC", "30SEC", "1MIN", "2MIN", "3MIN",
           "4MIN", "5MIN", "6MIN", "10MIN", "15MIN", "20MIN", "30MIN", "1HRS", "2HRS", "3HRS", "4HRS", "6HRS", "8HRS",
           "12HRS", "1DAY", "2DAY", "3DAY", "5DAY", "7DAY", "10DAY", "1MTH", "2MTH", "3MTH", "4MTH", "6MTH", "1YRS",
           "2YRS", "3YRS", "4YRS", "5YRS"]
proxies_list = []
proxy_type = 'None'
PRODUCTION_URL = 'https://rest.coinapi.io/v1%s'
keys = []
proxy_types = ['None', 'fresh', 'list', 'rotate']
sources = ["ohlcv", "trades", "quotes", "order"]
filetypes = ["json", "csv"]
timeout = 120.0
args = {}


def generate_keys(num=1):
    print('generate_keys', end='\n' * 2)
    i = 0
    while i < num:
        try:
            session = GuerrillaMailSession()
            email_address = session.get_session_state()['email_address'].split('@')[0] + '@' + random.choice(
                ['sharklasers.com', 'guerrillamail.info', 'grr.la', 'guerrillamail.biz', 'guerrillamail.com',
                 'guerrillamail.de', 'guerrillamail.net', 'guerrillamail.org', 'guerrillamailblock.com', 'pokemail.net',
                 'spam4.me'])

            print("#" + str(i) + ", " + email_address)

            url = "https://rest.coinapi.io/www/freeplan"

            payload = {"email": email_address, "name": names.get_full_name(), "title": names.get_last_name(),
                       "company": random.choice(["1-10", "10-50", "50-250", "250-1000", "1000+"])}

            r = make_prequest("POST", url, json=payload)
            response = r.text

            if "OK" not in response:
                print(response)
                continue

            while True:
                try:
                    print('waiting for mail')
                    sleep(random.randint(5, 25))
                    email_list = session.get_email_list()
                    message = email_list[0].excerpt
                    matchObj = re.search(r'API Key: (.*)', message, re.M | re.I)
                    key = matchObj and matchObj.group(1)
                    if (key):
                        break
                except GuerrillaMailException as e:
                    print(e)
                    raise Exception(e)
                except Exception as e:
                    print(e)

            i += 1
            print(key)
            tmpKeys = readKeys()
            tmpKeys.append(key)
            keys.append(key)

            with open("keys.json", "w") as f:
                json.dump(tmpKeys, f)
        except  Exception as e:
            print(e)
            print('generate_keys_sleeping...')
            sleep(random.randint(10, 60))


def readKeys():
    try:
        with open("keys.json", "r") as f:
            return json.load(f)
    except Exception as e:
        print(e)
        return []


def parse_args():
    arguments = docopt(__doc__)
    schema = Schema({
        '--from': Or(None, Use(lambda i: datetime.strptime(i, '%Y-%m-%d')),
                     error='--from=date date should be in the format of YYYY-MM-DD '),
        '--to': Or(And(None, Use(lambda i: datetime.now())), Use(lambda i: datetime.strptime(i, '%Y-%m-%d')),
                   error='--to=date date should be in the format of YYYY-MM-DD '),
        '--period': Or(None, And(Use(str), lambda s: s in periods),
                       error='--period=string should be a string in ' + ', '.join(periods)),
        '--source': Or(None, And(Use(str), lambda s: s in sources),
                       error='--source=string should be a string in ' + ', '.join(sources)),
        '--filetype': Or(None, And(Use(str), lambda s: s in filetypes),
                         error='--filetype=string should be a string in ' + ', '.join(filetypes)),
        '--proxy_type': Or(None, And(Use(str), lambda s: s in proxy_types),
                           error='--proxy_type=string should be a string in ' + ', '.join(proxy_types)),
        '--limit': Or(None, And(Use(int), lambda n: 1 <= n <= 100000),
                      error='--limit=N should be integer 1 <= N <= 100000'),
        '--levels': Or(None, And(Use(int), lambda n: 1 <= n <= 20),
                       error='--limit=N should be integer 1 <= N <= 20'),
        '--timeout': Or(None, Use(int)),
        '--find_n_proxy': Or(None, Use(int)),
        '--generate_keys': Or(None, Use(int)),
        '--symbol': Or(None, Use(str)),
        '--exchange': Or(None, Use(str)),
        '--base': Or(None, Use(str)),
        '--quote': Or(None, Use(str)),
        '--type': Or(None, Use(str)),
        '--proxy_dnsbl': Or(None, Use(bool)),
        '--proxy_strict': Or(None, Use(bool)),
        '--continue': Or(None, Use(bool)),
        '--help': Or(None, Use(bool)),
        '--path': Or(None, And(Use(os.path.realpath),
                               lambda x: os.makedirs(x, exist_ok=True) or os.path.exists(x)),
                     error='--path=<path> PATH is incorrect')
    }, ignore_extra_keys=False)
    try:
        validate = schema.validate(arguments)
        validate['--symbol'] = validate['--symbol'] and validate['--symbol'].split(',') or []
        validate['--exchange'] = validate['--exchange'] and validate['--exchange'].split(',') or []
        validate['--base'] = validate['--base'] and validate['--base'].split(',') or []
        validate['--quote'] = validate['--quote'] and validate['--quote'].split(',') or []
        validate['--type'] = validate['--type'] and validate['--type'].split(',') or []
        return validate
    except SchemaError as e:
        exit(e)


def getSymbols():
    print('getSymbols', end='\n' * 2)
    symbol_ids = []
    symbols = try_keys(lambda api: api.metadata_list_symbols())

    with open(os.path.join(args['--path'], 'list_symbols.json'), "w") as f:
        json.dump(symbols, f)

    for symbol in symbols:
        if (len(args['--symbol']) == 0 or symbol['symbol_id'] in args['--symbol']) \
                and (len(args['--exchange']) == 0 or symbol['exchange_id'] in args['--exchange']) \
                and (len(args['--type']) == 0 or symbol['symbol_type'] in args['--type']) \
                and (len(args['--base']) == 0 or symbol['asset_id_base'] in args['--base']) \
                and (len(args['--quote']) == 0 or symbol['asset_id_quote'] in args['--quote']):
            symbol_ids.append(symbol['symbol_id'])

    with open(os.path.join(args['--path'], 'symbol_ids.json'), "w") as f:
        json.dump(symbol_ids, f)

    return symbol_ids


def getTrades(symbol):
    print('getTrades', end='\n' * 2)

    print(symbol)
    next_start = args['--from'].isoformat().split('.')[0]
    symbol_list = []
    while dateutil.parser.parse(next_start).date() < args['--to'].date():
        data = try_keys(lambda api: api.trades_historical_data(symbol, {'time_start': next_start,
                                                                        'time_end':
                                                                            args['--to'].isoformat().split('.')[0],
                                                                        'limit': args['--limit']}))
        if len(data) == 0:
            break
        next_start = data[-1]['time_coinapi'].split('.')[0]
        symbol_list.extend(data)

    data_frame = pd.DataFrame.from_dict(symbol_list)

    save_df(data_frame, symbol)

    return data_frame


def getOrder(symbol):
    print('getOrder', end='\n' * 2)

    print(symbol)
    next_start = args['--from'].isoformat().split('.')[0]
    symbol_list = []
    while dateutil.parser.parse(next_start).date() < args['--to'].date():
        data = try_keys(lambda api: api.orderbooks_historical_data(symbol, {'time_start': next_start,
                                                                            'time_end':
                                                                                args['--to'].isoformat().split('.')[
                                                                                    0],
                                                                            'limit': args['--limit'],
                                                                            'limit_levels': args['--levels']}))
        if len(data) == 0:
            break
        next_start = data[-1]['time_coinapi'].split('.')[0]
        symbol_list.extend(data)

    data_frame = pd.DataFrame.from_dict(symbol_list)
    save_df(data_frame, symbol)

    return data_frame


def getQuotes(symbol):
    print('getQuotes', end='\n' * 2)

    print(symbol)
    next_start = args['--from'].isoformat().split('.')[0]
    symbol_list = []
    while dateutil.parser.parse(next_start).date() < args['--to'].date():
        data = try_keys(lambda api: api.quotes_historical_data(symbol, {'time_start': next_start,
                                                                        'time_end':
                                                                            args['--to'].isoformat().split('.')[0],
                                                                        'limit': args['--limit']}))
        if len(data) == 0:
            break
        next_start = data[-1]['time_coinapi'].split('.')[0]
        symbol_list.extend(data)

    data_frame = pd.DataFrame.from_dict(symbol_list)
    save_df(data_frame, symbol)

    return data_frame


def getOhlcv(symbol):
    print('getOhlcv', end='\n' * 2)

    print(symbol)
    next_start = args['--from'].isoformat().split('.')[0]
    symbol_list = []
    while dateutil.parser.parse(next_start).date() < args['--to'].date():
        data = try_keys(lambda api: api.ohlcv_historical_data(symbol, {'time_start': next_start,
                                                                       'time_end':
                                                                           args['--to'].isoformat().split('.')[0],
                                                                       'limit': args['--limit'],
                                                                       'period_id': args['--period'] or '1MIN'}))
        if len(data) == 0:
            break
        next_start = data[-1]['time_period_end'].split('.')[0]
        symbol_list.extend(data)

    data_frame = pd.DataFrame.from_dict(symbol_list)

    if len(data_frame.index) > 0:
        save_df(data_frame, symbol,
                columns=['time_open', 'price_close', 'volume_traded', 'price_open', 'price_high', 'price_low',
                         'trades_count'],
                header=['Date', 'Close', 'Volume', 'Open', 'High', 'Low', 'Market Cap'])
    else:
        print('no data to save')

    return data_frame


def try_keys(call):
    print('try_keys')
    index = 0
    while True:
        try:
            if len(keys) == 0:
                generate_keys(args['--generate_keys'] or 5)

            index = random.randint(0, len(keys) - 1)
            api = CoinAPIv1(keys[index])
            response = call(api)
            results = json.loads(response.text)

            if type(results) is list:
                if response.headers.get('X-RateLimit-Remaining', None) == '0':
                    print("consumed key: " + keys.pop(index))
                    print("remaining keys: " + str(len(keys)))

                print("received records: ", len(results))
                return results
            else:
                print(results)
                if 'many requests'.lower() in response.text.lower() or 'Invalid API key'.lower() in response.text.lower() \
                        or response.headers.get('X-RateLimit-Remaining', None) == '0':
                    print("used key: " + keys.pop(index))
                    print("remaining keys: " + str(len(keys)))
        except Exception as e:
            print(e)
            print("used key: " + keys.pop(index))
            print("remaining keys: " + str(len(keys)))


def make_prequest(method='get',
                  url=None,
                  headers=dict(),
                  data=None,
                  params=None,
                  auth=None,
                  cookies=None,
                  proxies=None,
                  json=None):
    ua = UserAgent()
    headers.update({'User-Agent': ua.random})

    if proxy_type == 'None':
        while True:
            try:
                return requests.request(method=method, url=url, headers=headers, data=data, params=params, auth=auth,
                                        cookies=cookies, proxies=proxies, json=json, timeout=timeout)
            except Exception as e:
                print(e)
                print('make_prequest_sleeping...')
                sleep(random.randint(3, 15))

    index = 0

    while True:
        try:
            if len(proxies_list) == 0 or (type(proxies_list[0]) != str and len(proxies_list) <= 5):
                find_proxy(args['--find_n_proxy'])
                read_proxies()

            index = random.randint(0, len(proxies_list) - 1)
            if type(proxies_list[index]) == str:
                r = requests.request(method=method, url=proxies_list[index] + urllib.parse.quote_plus(url),
                                     headers=headers,
                                     data=data,
                                     params=params, auth=auth,
                                     cookies=cookies, json=json,
                                     timeout=(timeout if timeout and timeout >= 60 else 120))
                if r.status_code == 403 or r.status_code == 429:
                    print(r.status_code + ' ' + r.text)
                    print("used proxy: " + proxies_list.pop(index))
                    print("remaining proxies: " + str(len(proxies_list)))
                else:
                    return r

            else:
                r = requests.request(method=method, url=url, headers=headers, data=data, params=params, auth=auth,
                                     cookies=cookies, proxies=proxies_list[index], json=json, timeout=timeout)
                if r.status_code >= 400:
                    print(r.status_code + ' ' + r.text)
                    print("used proxy: " + proxies_list.pop(index)["http"])
                    print("remaining proxies: " + str(len(proxies_list)))
                return r
        except Exception as e:
            print(e)
            print("used proxy: " + str(proxies_list.pop(index)))
            print("remaining proxies: " + str(len(proxies_list)))


async def save_proxy(proxies):
    list = []
    while True:
        try:
            proxy = await proxies.get()
            if proxy is None:
                break
            list.append(
                {"http": ("http://%s:%d" % (proxy.host, proxy.port)),
                 "https": ("https://%s:%d" % (proxy.host, proxy.port))})
            print("#" + str(len(list)) + ", " + proxy.host)
        except  Exception as e:
            print(e)
            print('save_proxy_sleeping...')
            sleep(random.randint(3, 15))

    with open("proxies.json", "w") as f:
        json.dump(list, f)


def read_proxies():
    global proxies_list
    try:
        with open("proxies.json", "r") as f:
            proxies_list = json.load(f)
            return proxies_list
    except Exception as e:
        print(e)
        return []


def read_rproxies():
    global proxies_list
    try:
        with open("rproxy.json", "r") as f:
            proxies_list = json.load(f)
            return proxies_list
    except Exception as e:
        print(e)
        return []


def find_proxy(limit=1000):
    while True:
        try:
            print('find_proxy', end='\n' * 2)
            proxies = asyncio.Queue()
            broker = Broker(proxies)

            dnsbl = ['bl.spamcop.net', 'cbl.abuseat.org', 'dnsbl.sorbs.net',
                     'zen.spamhaus.org', 'bl.mcafee.com', 'spam.spamrats.com'] if args['--proxy_dnsbl'] else None

            tasks = asyncio.gather(
                broker.find(types=['HTTP', 'HTTPS'], limit=limit, strict=args['--proxy_strict'], dnsbl=dnsbl),
                save_proxy(proxies))
            loop = asyncio.get_event_loop()
            loop.run_until_complete(tasks)
            break
        except  Exception as e:
            print(e)
            print('find_proxy_sleeping...')
            Resolver._ip_hosts = [
                'https://wtfismyip.com/text',
                'http://api.ipify.org/',
                'http://ipinfo.io/ip',
                'http://ipv4.icanhazip.com/',
                'http://myexternalip.com/raw',
                'http://ipinfo.io/ip',
                'http://ifconfig.io/ip',
            ]
            sleep(random.randint(3, 15))


class HTTPClient:
    def __init__(self, endpoint, headers=dict(), params=dict()):
        self.url = PRODUCTION_URL % endpoint

        if headers.get('X-CoinAPI-Key', None):
            params.update({"apiKey": headers['X-CoinAPI-Key']})
            headers.pop('X-CoinAPI-Key')

        self.params = params
        self.headers = headers

    def perform(self):
        resource = self.url
        if self.params:
            query_string = urllib.parse.urlencode(self.params)
            resource = '%s?%s' % (self.url, query_string)

        return make_prequest(url=resource)


class MetadataListExchangesRequest:
    def endpoint(self):
        return '/exchanges'


class MetadataListAssetsRequest:
    def endpoint(self):
        return '/assets'


class MetadataListSymbolsRequest:
    def endpoint(self):
        return '/symbols'


class ExchangeRatesGetSpecificRateRequest:
    def __init__(self,
                 asset_id_base,
                 asset_id_quote,
                 query_parameters=dict()):
        self.asset_id_base = asset_id_base
        self.asset_id_quote = asset_id_quote
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/exchangerate/%s/%s' % (
            self.asset_id_base,
            self.asset_id_quote)


class ExchangeRatesGetAllCurrentRates:
    def __init__(self, asset_id_base):
        self.asset_id_base = asset_id_base

    def endpoint(self):
        return '/exchangerate/%s' % self.asset_id_base


class OHLCVListAllPeriodsRequest:
    def endpoint(self):
        return '/ohlcv/periods'


class OHLCVLatestDataRequest:
    def __init__(self, symbol_id, query_parameters=dict()):
        self.symbol_id = symbol_id
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/ohlcv/%s/latest' % self.symbol_id


class OHLCVHistoricalDataRequest:
    def __init__(self, symbol_id, query_parameters=dict()):
        self.symbol_id = symbol_id
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/ohlcv/%s/history' % self.symbol_id


class TradesLatestDataAllRequest:
    def __init__(self, query_parameters=dict()):
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/trades/latest'


class TradesLatestDataSymbolRequest:
    def __init__(self, symbol_id, query_parameters=dict()):
        self.symbol_id = symbol_id
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/trades/%s/latest' % self.symbol_id


class TradesHistoricalDataRequest:
    def __init__(self, symbol_id, query_parameters=dict()):
        self.symbol_id = symbol_id
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/trades/%s/history' % self.symbol_id


class QuotesCurrentDataAllRequest:
    def endpoint(self):
        return '/quotes/current'


class QuotesCurrentDataSymbolRequest:
    def __init__(self, symbol_id):
        self.symbol_id = symbol_id

    def endpoint(self):
        return '/quotes/%s/current' % self.symbol_id


class QuotesLatestDataAllRequest:
    def __init__(self, query_parameters=dict()):
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/quotes/latest'


class QuotesLatestDataSymbolRequest:
    def __init__(self, symbol_id, query_parameters=dict()):
        self.symbol_id = symbol_id
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/quotes/%s/latest' % self.symbol_id

    def limit(self, lim):
        params = self.__with_parameter('limit', lim)
        return QuotesLatestDataSymbolRequest(self.symbol_id, params)

    only = limit


class QuotesHistoricalData:
    def __init__(self, symbol_id, query_parameters=dict()):
        self.symbol_id = symbol_id
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/quotes/%s/history' % self.symbol_id


class OrderbooksCurrentDataAllRequest:
    def endpoint(self):
        return '/orderbooks/current'


class OrderbooksCurrentDataSymbolRequest:
    def __init__(self, symbol_id):
        self.symbol_id = symbol_id

    def endpoint(self):
        return '/orderbooks/%s/current' % self.symbol_id


class OrderbooksLatestDataRequest:
    def __init__(self, symbol_id, query_parameters=dict()):
        self.symbol_id = symbol_id
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/orderbooks/%s/latest' % self.symbol_id


class OrderbooksHistoricalDataRequest:
    def __init__(self, symbol_id, query_parameters=dict()):
        self.symbol_id = symbol_id
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/orderbooks/%s/history' % self.symbol_id


class CoinAPIv1:
    DEFAULT_HEADERS = {
        'Accept': 'application/json'
    }

    def __init__(self, api_key, headers=dict(), client_class=HTTPClient):
        self.api_key = api_key
        header_apikey = {'X-CoinAPI-Key': self.api_key}
        self.headers = {**self.DEFAULT_HEADERS, **headers, **header_apikey}
        self.client_class = client_class

    def with_header(self, header, value):
        old_headers = self.headers
        new_header = {header: value}
        return CoinAPIv1(self.api_key, {**old_headers, **new_header})

    def with_headers(self, additional_headers):
        old_headers = self.headers
        return CoinAPIv1(self.api_key, {**old_headers, **additional_headers})

    def metadata_list_exchanges(self):
        request = MetadataListExchangesRequest()
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def metadata_list_assets(self):
        request = MetadataListAssetsRequest()
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def metadata_list_symbols(self):
        request = MetadataListSymbolsRequest()
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def exchange_rates_get_specific_rate(self,
                                         asset_id_base,
                                         asset_id_quote,
                                         query_parameters=dict()):
        request = ExchangeRatesGetSpecificRateRequest(asset_id_base,
                                                      asset_id_quote,
                                                      query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def exchange_rates_get_all_current_rates(self,
                                             asset_id_base):
        request = ExchangeRatesGetAllCurrentRates(asset_id_base)
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def ohlcv_list_all_periods(self):
        request = OHLCVListAllPeriodsRequest()
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def ohlcv_latest_data(self,
                          symbol_id,
                          query_parameters=dict()):
        request = OHLCVLatestDataRequest(symbol_id,
                                         query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def ohlcv_historical_data(self,
                              symbol_id,
                              query_parameters):
        request = OHLCVHistoricalDataRequest(symbol_id, query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def trades_latest_data_all(self,
                               query_parameters=dict()):
        request = TradesLatestDataAllRequest(query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def trades_latest_data_symbol(self,
                                  symbol_id,
                                  query_parameters=dict()):
        request = TradesLatestDataSymbolRequest(symbol_id, query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def trades_historical_data(self,
                               symbol_id,
                               query_parameters=dict()):
        request = TradesHistoricalDataRequest(symbol_id, query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def quotes_current_data_all(self):
        request = QuotesCurrentDataAllRequest()
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def quotes_current_data_symbol(self,
                                   symbol_id):
        request = QuotesCurrentDataSymbolRequest(symbol_id)
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def quotes_latest_data_all(self,
                               query_parameters=dict()):
        request = QuotesLatestDataAllRequest(query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def quotes_latest_data_symbol(self,
                                  symbol_id,
                                  query_parameters=dict()):
        request = QuotesLatestDataSymbolRequest(symbol_id, query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def quotes_historical_data(self,
                               symbol_id,
                               query_parameters=dict()):
        request = QuotesHistoricalData(symbol_id, query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def orderbooks_current_data_all(self):
        request = OrderbooksCurrentDataAllRequest()
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def orderbooks_current_data_symbol(self,
                                       symbol_id):
        request = OrderbooksCurrentDataSymbolRequest(symbol_id)
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def orderbooks_latest_data(self,
                               symbol_id,
                               query_parameters=dict()):
        request = OrderbooksLatestDataRequest(symbol_id, query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def orderbooks_historical_data(self,
                                   symbol_id,
                                   query_parameters=dict()):
        request = OrderbooksHistoricalDataRequest(symbol_id, query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()


class DateTimeDecoder(json.JSONDecoder):

    def __init__(self, *args, **kargs):
        JSONDecoder.__init__(self, object_hook=self.dict_to_object,
                             *args, **kargs)

    def dict_to_object(self, d):
        if '__type__' not in d:
            return d

        type = d.pop('__type__')
        try:
            dateobj = datetime(**d)
            return dateobj
        except:
            d['__type__'] = type
            return d


class DateTimeEncoder(JSONEncoder):
    """ Instead of letting the default encoder convert datetime to string,
        convert datetime objects into a dict, which can be decoded by the
        DateTimeDecoder
    """

    def default(self, obj):
        if isinstance(obj, datetime):
            return {
                '__type__': 'datetime',
                'year': obj.year,
                'month': obj.month,
                'day': obj.day,
                'hour': obj.hour,
                'minute': obj.minute,
                'second': obj.second,
                'microsecond': obj.microsecond,
            }
        else:
            return JSONEncoder.default(self, obj)


def init_path():
    args['--path'] = os.path.join(args['--path'], args['--source'] + '_' + datetime.now().strftime("%Y%m%d-%H%M%S"))
    os.makedirs(args['--path'], exist_ok=True)
    with open(os.path.join(args['--path'], 'args.json'), "w") as f:
        json.dump(args, f, cls=DateTimeEncoder)


def save_df(df, filename, columns=None, header=True):
    file_path = os.path.join(args['--path'], filename + '.' + args['--filetype'])
    if args['--filetype'] == 'csv':
        df.to_csv(file_path, index=False,
                  columns=columns,
                  header=header)
    elif args['--filetype'] == 'json':
        df.to_json(file_path, orient='records')


def loop_symbols(symbols, call):
    while len(symbols) > 0:
        call(symbols[0])

        with open(os.path.join(args['--path'], "remaining_symbols.json"), "w") as f:
            symbols.pop(0)
            json.dump(symbols, f)


def convert_period(df):
    print('convert_period')
    if len(df.index) > 0:
        pass
    else:
        print('no data to save')
    return df


if __name__ == '__main__':
    start_exec = datetime.now()
    args = parse_args()
    print(args, end='\n' * 2)

    if args['--continue']:
        try:
            latest_subdir = max([os.path.join(args['--path'], d) for d in os.listdir(args['--path'])],
                                key=os.path.getmtime)
        except Exception as e:
            print(e)
            print('cant find the last run')
            exit()

        with open(os.path.join(args['--path'], latest_subdir, 'args.json'), "r") as f:
            args = json.load(f, cls=DateTimeDecoder)
            args['--continue'] = True

    keys = readKeys()
    timeout = args['--timeout'] if args['--timeout'] != 0 else None
    proxy_type = args['--proxy_type']

    if proxy_type == 'fresh':
        find_proxy(args['--find_n_proxy'])
        read_proxies()
    elif proxy_type == 'list':
        read_proxies()
    elif proxy_type == 'rotate':
        read_rproxies()

    if args['--generate_keys']:
        generate_keys(args['--generate_keys'])

    if args['--continue']:
        with open(os.path.join(args['--path'], "remaining_symbols.json"), "r") as f:
            symbols = json.load(f)
    else:
        init_path()
        symbols = getSymbols()

    print(symbols, end='\n' * 2)
    if len(symbols) == 0:
        print('No valid/remaining symbols found!')
        exit()

    if args['--source'] == 'ohlcv':
        loop_symbols(symbols, lambda symbol: getOhlcv(symbol))
    else:
        if args['--source'] == 'trades':
            loop_symbols(symbols, lambda symbol: convert_period(getTrades(symbol)))
        elif args['--source'] == 'quotes':
            loop_symbols(symbols, lambda symbol: convert_period(getQuotes(symbol)))
        elif args['--source'] == 'order':
            loop_symbols(symbols, lambda symbol: convert_period(getOrder(symbol)))

    print('DONE, Took: ', timedelta(seconds=(datetime.now() - start_exec).total_seconds()))
