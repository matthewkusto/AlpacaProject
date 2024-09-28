from the_keys import *
import requests as re


url = "https://paper-api.alpaca.markets"
keys = {"APCA-API-KEY-ID": api_key, "APCA-API-SECRET-KEY": secret_api_key}

def accout_information():
    account = re.get("{}/v2/account".format(url), headers=keys)
    print(account.content)

def get_asset(_symbol:str): # Allow for user input
    assets = re.get("{url}/v2/assets/{}".format(_symbol.upper()), headers=keys)
    print(assets.content)

def place_order(_symbol:str, _qty:int, _side:str, _type:str, _time_in_force:str, ):
    order = {
        'symbol':_symbol.upper(),
        'qty':_qty,
        'side':_side,
        'type':_type,
        'time_in_force':_time_in_force
    }
    order_placed = re.post("{}/v2/orders".format(url), json=order, headers=keys)
    return order_placed.content
    
def main_menu():
    ...


place_order('aapl', 10, 'buy', 'market', 'day')