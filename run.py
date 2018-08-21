""" Coinapi key generator and data downloader

Example, try:


Usage:
  run.py (--symbol=<string>... | --exchange=<string>... [--base=<string>...] [--quote=<string>...] [--type=<string>...]) --source=<string> --from=<date> [--to=<date>] [--period=<string>]  [--limit=<int>]  [--levels=<int>]  [--path=<path>] [--filetype=<string>]
  run.py (-h | --help)

Arguments:
  --symbol=<string>     Symbol id for requested timeseries, it can be one or more space separated, check https://docs.coinapi.io/#list-all-symbols
  --exchange=<string>     identifier of the exchange where symbol is traded, it can be one or more space separated, check https://docs.coinapi.io/#list-all-symbols
  --base=<string>     FX Spot base asset identifier, for derivatives it’s contact underlying (e.g. BTC for BTC/USD), it can be one or more space separated, check https://docs.coinapi.io/#list-all-symbols
  --quote=<string>     FX Spot quote asset identifier, for derivatives it’s contract underlying (e.g. USD for BTC/USD), it can be one or more space separated, check https://docs.coinapi.io/#list-all-symbols [default: USD]
  --type=<string>     Type of symbol (possible values are: SPOT, FUTURES or OPTION), it can be one or more space separated
  --from=<date>     starting date.
  --source=<string>     the data to be downloaded (ohlcv, trades, quotes, order).

Options:
  -h --help     Show this screen.
  --path=<path>  a directory to save data to [default: out].
  --filetype=<string>  the saved data file type (json, csv, xml) [default: csv].
  --to=<date>  ending date.
  --period=<string>  supported time periods available for requesting OHLCV timeseries data OR to convert data to, check https://docs.coinapi.io/#list-all-periods.
  --limit=<int>  Amount of items to return , minimum is 1, maximum is 100000 [default: 100000].
  --levels=<int>  Maximum amount of levels from each side of the book to include in response, max 20 [default: 20].

"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import math
import os
import csv
from datetime import datetime
import json
from time import sleep
import re

import requests

from pprint import pprint
from inspect import getmembers

from coinapi_v1 import CoinAPIv1

try:
    from docopt import docopt
    from schema import Schema, And, Or, Use, SchemaError, Optional
    from guerrillamail import GuerrillaMailSession
    from proxy_requests.proxy_requests import ProxyRequests
    import names
    import random
    from fake_useragent import UserAgent
except ImportError:
    exit('One or more of the required libraries is missing\n'
         'Use the following commands to install them:\n'
         'pip install schema\n'
         'pip install docopt\n'
         'pip install numpy\n'
         'pip install matplotlib\n'
         'pip install mpl_finance\n'
         'pip install python-guerrillamail\n'
         'pip install proxy-requests\n'
         'pip install names\n'
         'pip install fake-useragent\n'
         '\n')

periods = ["1SEC", "2SEC", "3SEC", "4SEC", "5SEC", "6SEC", "10SEC", "15SEC", "20SEC", "30SEC", "1MIN", "2MIN", "3MIN",
           "4MIN", "5MIN", "6MIN", "10MIN", "15MIN", "20MIN", "30MIN", "1HRS", "2HRS", "3HRS", "4HRS", "6HRS", "8HRS",
           "12HRS", "1DAY", "2DAY", "3DAY", "5DAY", "7DAY", "10DAY", "1MTH", "2MTH", "3MTH", "4MTH", "6MTH", "1YRS",
           "2YRS", "3YRS", "4YRS", "5YRS"]


def generate_keys(num=1, use_proxy=False):
    ua = UserAgent()
    keys = readKeys() or []
    i = 0
    while i < num:
        session = GuerrillaMailSession()
        email_address = session.get_session_state()['email_address']
        print('_' * 10)
        print(email_address)

        url = "https://rest.coinapi.io/www/freeplan"

        payload = {"email": email_address, "name": names.get_full_name(), "title": names.get_last_name(),
                   "company": random.choice(["1-10", "10-50", "50-250", "250-1000", "1000+"])}
        headers = {'User-Agent': ua.random}

        if (use_proxy):
            pr = ProxyRequests(url)
            pr.set_headers(headers)
            pr.post_with_headers(payload)
            response = pr.request
            print(pr.proxy_used)
        else:
            r = requests.request("POST", url, json=payload, headers=headers)
            response = r.text

        if "OK" not in response:
            print(response)
            continue

        while True:
            sleep(5)
            email_list = session.get_email_list()
            message = email_list[0].excerpt
            matchObj = re.search(r'API Key: (.*)', message, re.M | re.I)
            key = matchObj and matchObj.group(1)
            if (key):
                break
            print('waiting for mail')

        i += 1
        print(key)
        keys.append(key)

        with open("keys.json", "w") as f:
            json.dump(keys, f)

    print(keys)
    return key


def readKeys():
    with open("keys.json", "r") as f:
        keys = json.load(f)
    return keys


def run():
    print(generate_keys(10))


def getData():
    ua = UserAgent()
    api = CoinAPIv1("569B4671-0AEE-4153-84E4-69A4FE7D25A6", headers={'User-Agent': ua.random}, use_proxy=False)
    exchanges = api.metadata_list_exchanges()
    print('Exchanges')
    for exchange in exchanges:
        print('Exchange ID: %s' % exchange['exchange_id'])
        print('Exchange website: %s' % exchange['website'])
        print('Exchange name: %s' % exchange['name'])
    assets = api.metadata_list_assets()
    print('Assets')
    for asset in assets:
        print('Asset ID: %s' % asset['asset_id'])
        print('Asset name: %s' % asset['name'])
        print('Asset type (crypto?): %s' % asset['type_is_crypto'])
    symbols = api.metadata_list_symbols()
    print('Symbols')
    for symbol in symbols:
        print('Symbol ID: %s' % symbol['symbol_id'])
        print('Exchange ID: %s' % symbol['exchange_id'])
        print('Symbol type: %s' % symbol['symbol_type'])
        print('Asset ID base: %s' % symbol['asset_id_base'])
        print('Asset ID quote: %s' % symbol['asset_id_quote'])

        if (symbol['symbol_type'] == 'FUTURES'):
            print('Future delivery time: %s' % symbol['future_delivery_time'])

        if (symbol['symbol_type'] == 'OPTION'):
            print('Option type is call: %s' % symbol['option_type_is_call'])
            print('Option strike price: %s' % symbol['option_strike_price'])
            print('Option contract unit: %s' % symbol['option_contract_unit'])
            print('Option exercise style: %s' % symbol['option_exercise_style'])
            print('Option expiration time: %s' % symbol['option_expiration_time'])
    exchange_rate = api.exchange_rates_get_specific_rate('BTC', 'USD')
    print('Time: %s' % exchange_rate['time'])
    print('Base: %s' % exchange_rate['asset_id_base'])
    print('Quote: %s' % exchange_rate['asset_id_quote'])
    print('Rate: %s' % exchange_rate['rate'])
    last_week = datetime.date(2017, 5, 16).isoformat()
    exchange_rate_last_week = api.exchange_rates_get_specific_rate('BTC', 'USD', {'time': last_week})
    print('Time: %s' % exchange_rate_last_week['time'])
    print('Base: %s' % exchange_rate_last_week['asset_id_base'])
    print('Quote: %s' % exchange_rate_last_week['asset_id_quote'])
    print('Rate: %s' % exchange_rate_last_week['rate'])
    current_rates = api.exchange_rates_get_all_current_rates('BTC')
    print("Asset ID Base: %s" % current_rates['asset_id_base'])
    for rate in current_rates['rates']:
        print('Time: %s' % rate['time'])
        print('Quote: %s' % rate['asset_id_quote'])
        print('Rate: %s' % rate['rate'])
    periods = api.ohlcv_list_all_periods()
    for period in periods:
        print('ID: %s' % period['period_id'])
        print('Seconds: %s' % period['length_seconds'])
        print('Months: %s' % period['length_months'])
        print('Unit count: %s' % period['unit_count'])
        print('Unit name: %s' % period['unit_name'])
        print('Display name: %s' % period['display_name'])
    ohlcv_latest = api.ohlcv_latest_data('BITSTAMP_SPOT_BTC_USD', {'period_id': '1MIN'})
    for period in ohlcv_latest:
        print('Period start: %s' % period['time_period_start'])
        print('Period end: %s' % period['time_period_end'])
        print('Time open: %s' % period['time_open'])
        print('Time close: %s' % period['time_close'])
        print('Price open: %s' % period['price_open'])
        print('Price close: %s' % period['price_close'])
        print('Price low: %s' % period['price_low'])
        print('Price high: %s' % period['price_high'])
        print('Volume traded: %s' % period['volume_traded'])
        print('Trades count: %s' % period['trades_count'])
    start_of_2016 = datetime.date(2016, 1, 1).isoformat()
    ohlcv_historical = api.ohlcv_historical_data('BITSTAMP_SPOT_BTC_USD',
                                                 {'period_id': '1MIN', 'time_start': start_of_2016})
    for period in ohlcv_historical:
        print('Period start: %s' % period['time_period_start'])
        print('Period end: %s' % period['time_period_end'])
        print('Time open: %s' % period['time_open'])
        print('Time close: %s' % period['time_close'])
        print('Price open: %s' % period['price_open'])
        print('Price close: %s' % period['price_close'])
        print('Price low: %s' % period['price_low'])
        print('Price high: %s' % period['price_high'])
        print('Volume traded: %s' % period['volume_traded'])
        print('Trades count: %s' % period['trades_count'])
    latest_trades = api.trades_latest_data_all()
    for data in latest_trades:
        print('Symbol ID: %s' % data['symbol_id'])
        print('Time Exchange: %s' % data['time_exchange'])
        print('Time CoinAPI: %s' % data['time_coinapi'])
        print('UUID: %s' % data['uuid'])
        print('Price: %s' % data['price'])
        print('Size: %s' % data['size'])
        print('Taker Side: %s' % data['taker_side'])
    latest_trades_doge = api.trades_latest_data_symbol('BITSTAMP_SPOT_BTC_USD')
    for data in latest_trades_doge:
        print('Symbol ID: %s' % data['symbol_id'])
        print('Time Exchange: %s' % data['time_exchange'])
        print('Time CoinAPI: %s' % data['time_coinapi'])
        print('UUID: %s' % data['uuid'])
        print('Price: %s' % data['price'])
        print('Size: %s' % data['size'])
        print('Taker Side: %s' % data['taker_side'])
    historical_trades_btc = api.trades_historical_data('BITSTAMP_SPOT_BTC_USD', {'time_start': start_of_2016})
    for data in historical_trades_btc:
        print('Symbol ID: %s' % data['symbol_id'])
        print('Time Exchange: %s' % data['time_exchange'])
        print('Time CoinAPI: %s' % data['time_coinapi'])
        print('UUID: %s' % data['uuid'])
        print('Price: %s' % data['price'])
        print('Size: %s' % data['size'])
        print('Taker Side: %s' % data['taker_side'])
    current_quotes = api.quotes_current_data_all()
    print(current_quotes)
    for quote in current_quotes:
        print('Symbol ID: %s' % quote['symbol_id'])
        print('Time Exchange: %s' % quote['time_exchange'])
        print('Time CoinAPI: %s' % quote['time_coinapi'])
        print('Ask Price: %s' % quote['ask_price'])
        print('Ask Size: %s' % quote['ask_size'])
        print('Bid Price: %s' % quote['bid_price'])
        print('Bid Size: %s' % quote['bid_size'])
        if 'last_trade' in quote:
            print('Last Trade: %s' % quote['last_trade'])
    current_quote_btc_usd = api.quotes_current_data_symbol('BITSTAMP_SPOT_BTC_USD')
    print('Symbol ID: %s' % current_quote_btc_usd['symbol_id'])
    print('Time Exchange: %s' % current_quote_btc_usd['time_exchange'])
    print('Time CoinAPI: %s' % current_quote_btc_usd['time_coinapi'])
    print('Ask Price: %s' % current_quote_btc_usd['ask_price'])
    print('Ask Size: %s' % current_quote_btc_usd['ask_size'])
    print('Bid Price: %s' % current_quote_btc_usd['bid_price'])
    print('Bid Size: %s' % current_quote_btc_usd['bid_size'])
    if 'last_trade' in current_quote_btc_usd:
        last_trade = current_quote_btc_usd['last_trade']
        print('Last Trade:')
        print('- Taker Side: %s' % last_trade['taker_side'])
        print('- UUID: %s' % last_trade['uuid'])
        print('- Time Exchange: %s' % last_trade['time_exchange'])
        print('- Price: %s' % last_trade['price'])
        print('- Size: %s' % last_trade['size'])
        print('- Time CoinAPI: %s' % last_trade['time_coinapi'])
    quotes_latest_data = api.quotes_latest_data_all()
    for quote in quotes_latest_data:
        print('Symbol ID: %s' % quote['symbol_id'])
        print('Time Exchange: %s' % quote['time_exchange'])
        print('Time CoinAPI: %s' % quote['time_coinapi'])
        print('Ask Price: %s' % quote['ask_price'])
        print('Ask Size: %s' % quote['ask_size'])
        print('Bid Price: %s' % quote['bid_price'])
        print('Bid Size: %s' % quote['bid_size'])
    quotes_latest_data_btc_usd = api.quotes_latest_data_symbol('BITSTAMP_SPOT_BTC_USD')
    for quote in quotes_latest_data_btc_usd:
        print('Symbol ID: %s' % quote['symbol_id'])
        print('Time Exchange: %s' % quote['time_exchange'])
        print('Time CoinAPI: %s' % quote['time_coinapi'])
        print('Ask Price: %s' % quote['ask_price'])
        print('Ask Size: %s' % quote['ask_size'])
        print('Bid Price: %s' % quote['bid_price'])
        print('Bid Size: %s' % quote['bid_size'])
    quotes_historical_data_btc_usd = api.quotes_historical_data('BITSTAMP_SPOT_BTC_USD', {'time_start': start_of_2016})
    for quote in quotes_historical_data_btc_usd:
        print('Symbol ID: %s' % quote['symbol_id'])
        print('Time Exchange: %s' % quote['time_exchange'])
        print('Time CoinAPI: %s' % quote['time_coinapi'])
        print('Ask Price: %s' % quote['ask_price'])
        print('Ask Size: %s' % quote['ask_size'])
        print('Bid Price: %s' % quote['bid_price'])
        print('Bid Size: %s' % quote['bid_size'])
    orderbooks_current_data = api.orderbooks_current_data_all()
    for data in orderbooks_current_data:
        print('Symbol ID: %s' % data['symbol_id'])
        print('Time Exchange: %s' % data['time_exchange'])
        print('Time CoinAPI: %s' % data['time_coinapi'])
        print('Asks:')
        for ask in data['asks']:
            print('- Price: %s' % ask['price'])
            print('- Size: %s' % ask['size'])
        print('Bids:')
        for bid in data['bids']:
            print('- Price: %s' % bid['price'])
            print('- Size: %s' % bid['size'])
    orderbooks_current_data_btc_usd = api.orderbooks_current_data_symbol('BITSTAMP_SPOT_BTC_USD')
    print('Symbol ID: %s' % orderbooks_current_data_btc_usd['symbol_id'])
    print('Time Exchange: %s' % orderbooks_current_data_btc_usd['time_exchange'])
    print('Time CoinAPI: %s' % orderbooks_current_data_btc_usd['time_coinapi'])
    print('Asks:')
    for ask in orderbooks_current_data_btc_usd['asks']:
        print('- Price: %s' % ask['price'])
        print('- Size: %s' % ask['size'])
    print('Bids:')
    for bid in orderbooks_current_data_btc_usd['bids']:
        print('- Price: %s' % bid['price'])
        print('- Size: %s' % bid['size'])
    orderbooks_latest_data_btc_usd = api.orderbooks_latest_data('BITSTAMP_SPOT_BTC_USD')
    for data in orderbooks_latest_data_btc_usd:
        print('Symbol ID: %s' % data['symbol_id'])
        print('Time Exchange: %s' % data['time_exchange'])
        print('Time CoinAPI: %s' % data['time_coinapi'])
        print('Asks:')
        for ask in data['asks']:
            print('- Price: %s' % ask['price'])
            print('- Size: %s' % ask['size'])
        print('Bids:')
        for bid in data['bids']:
            print('- Price: %s' % bid['price'])
            print('- Size: %s' % bid['size'])
    orderbooks_historical_data_btc_usd = api.orderbooks_historical_data('BITSTAMP_SPOT_BTC_USD',
                                                                        {'time_start': start_of_2016})
    for data in orderbooks_historical_data_btc_usd:
        print('Symbol ID: %s' % data['symbol_id'])
        print('Time Exchange: %s' % data['time_exchange'])
        print('Time CoinAPI: %s' % data['time_coinapi'])
        print('Asks:')
        for ask in data['asks']:
            print('- Price: %s' % ask['price'])
            print('- Size: %s' % ask['size'])
        print('Bids:')
        for bid in data['bids']:
            print('- Price: %s' % bid['price'])
            print('- Size: %s' % bid['size'])


sources = ["ohlcv", "trades", "quotes", "order"]
filetypes = ["json", "csv", "xml"]


def parse_args():
    arguments = docopt(__doc__)
    schema = Schema({
        '--from': Or(None, Use(lambda i: datetime.strptime(i, '%Y-%m-%d')),
                     error='--from=date date should be in the format of YYYY-MM-DD '),
        '--to': Or(None, Use(lambda i: datetime.strptime(i, '%Y-%m-%d')),
                   error='--to=date date should be in the format of YYYY-MM-DD '),
        '--period': Or(None, And(Use(str), lambda s: s in periods),
                       error='--period=string should be a string in ' + ', '.join(periods)),
        '--source': Or(None, And(Use(str), lambda s: s in sources),
                       error='--source=string should be a string in ' + ', '.join(sources)),
        '--filetype': Or(None, And(Use(str), lambda s: s in filetypes),
                         error='--filetype=string should be a string in ' + ', '.join(filetypes)),
        '--limit': Or(None, And(Use(int), lambda n: 1 <= n <= 100000),
                      error='--limit=N should be integer 1 <= N <= 100000'),
        '--levels': Or(None, And(Use(int), lambda n: 1 <= n <= 20),
                       error='--limit=N should be integer 1 <= N <= 20'),
        '--symbol': Or(None, Use(str)),
        '--exchange': Or(None, Use(str)),
        '--base': Or(None, Use(str)),
        '--quote': Or(None, Use(str)),
        '--type': Or(None, Use(str)),
        '--help': Or(None, Use(bool)),
        '--path': Or(None, And(Use(os.path.realpath), os.path.exists), error='--path=<path> PATH should exist')
    }, ignore_extra_keys=False)
    try:
        return schema.validate(arguments)
    except SchemaError as e:
        exit(e)


if __name__ == '__main__':
    args = parse_args()
    print(args, end='\n' * 5)
# run()
# getData()
