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
            pr.post(payload)
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

    print(keys)
    with open("keys.json", "w") as f:
        json.dump(keys, f)

    return key


def readKeys():
    with open("keys.json", "r") as f:
        keys = json.load(f)
    return keys


def run():
    print(generate_keys(2, True))
    # keys = readKeys()
    # print(keys)
    # url = 'https://rest.coinapi.io/v1/orderbooks/BITSTAMP_SPOT_BTC_USD/history?time_start=2016-01-01T00:00:00'
    # headers = {'X-CoinAPI-Key': keys[0]}
    # response = requests.get(url, headers=headers)
    # print(response.text)


if __name__ == '__main__':
    run()
