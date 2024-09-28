from the_keys import *
import requests as re
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest

url = "https://paper-api.alpaca.markets"
for_acct_url = ""
keys = {"APCA-API-KEY-ID": api_key, "APCA-API-SECRET-KEY": secret_api_key}

def accout_information():
    account = re.get("{}/v2/account".format(url), headers=keys)
    print(account.content)

def main_menu():
    ...

if __name__ == "__main__":
    main_menu()