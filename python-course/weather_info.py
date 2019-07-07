#!/usr/bin/env python3.6

import requests
import sys
import os
from argparse import ArgumentParser

parser = ArgumentParser(description='Get the current weater info.')
parser.add_argument('zip', help='zip/postal code to get the weather for')
parser.add_argument('--country', default='us',
                    help='country zip/postal belongs to, default is "us"')
args = parser.parse_args()
api_key = os.getenv('API_KEY')
if not api_key:
    print('no api_key supplied. set env var and retry.')
    sys.exit(1)

url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"
response = requests.get(url)
if response.status_code != 200:
    print(f"error while getting weater:{response.status_code}")
    sys.exit(1)
print(response.json())
