from the_keys import *
import requests as re


url = "https://paper-api.alpaca.markets"
keys = {"APCA-API-KEY-ID": api_key, "APCA-API-SECRET-KEY": secret_api_key}


def Main_Menu():
    print("=========================")
    print("========Main_Menu========")
    print("| 1. Account Information |")
    print("| 2. Find Asset          |")
    print("| 3. Place Order         |")
    print("| 4. Cancel Order        |")
    print("==========================")
    

def accout_information():
    account = re.get("{}/v2/account".format(url), headers=keys)
    return account.content


def get_asset(_symbol:str): # Allow for user input
    assets = re.get("{url}/v2/assets/{}".format(_symbol.upper()), headers=keys)
    return assets.content


# def create_order(object:list) -> list:
#     ...
# This should be able to in multiple orders, then place them


# Turn into async function for multi-order queue
def place_order(_symbol:str, _qty:int, _buy_or_sell:str, _order_type:str, _time_in_force:str):
    order = {
        
            'symbol':_symbol.upper(),
            'qty':_qty,
            'side':_buy_or_sell,
            'type':_order_type,
            'time_in_force':_time_in_force
        }
    
    order_placed = re.post("{}/v2/orders".format(url), json=order, headers=keys)
    return order_placed.content
   
    
# Single cancel orders ... Eventually turn into multi-cancel queue 
def cancel_order(_symbol:str) -> str:
    order_canceled = re.delete("{}/v2/positions/{}".format(url, _symbol.upper()), headers=keys)
    print(order_canceled.content, 'True')


if __name__ == "__main__":
    # Test
    loo = 2
    for i in range(loo):
        symbol:str = input("Symbol: ").upper()
        qty:int = input("Quantity: ")
        side:str  = input("Buy or Sell: ")
        order_type = input("Type: ")
        time_for_order:str  = input("Time: ")
        place_order(symbol, qty, side, order_type, time_for_order)
        print("================")
    # cancel_order('aapl')