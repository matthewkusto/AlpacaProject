from the_keys import *
import requests as re
import json

url = "https://paper-api.alpaca.markets"
keys = {"APCA-API-KEY-ID": api_key, "APCA-API-SECRET-KEY": secret_api_key}


def Main_Menu():
    print("=========================")
    print("========Main_Menu========")
    print("| 1. Account Information |")
    print("| 2. Find Asset          |")
    print("| 3. Place Order         |")
    print("| 4. Cancel Order        |")
    print("| x. Exit                |")
    print("==========================")
    choice = input("Enter Selection: ")
    while choice != "x":
        match choice:
            case "1":
                print(accout_information())
            case "2":
                symbol_ = input("Enter ticker symbol: ")
                print((get_asset(symbol_)))
            case "3":
                # have two functions here. 1 or multiple
                sym = input("Enter Ticker: ")
                qty = int(input("Enter QTY: "))
                buy_or_sell = input("Buy or Sell: ")
                order_type = input("Market: ")
                time_in_force = input("Trade type: ")
                print((place_order(sym, qty, buy_or_sell, order_type, time_in_force)))
            case "4":
                cancel_order()
            case "x":
                break
            case _:
                print("Please make selection")
        choice = input("Enter Selection: ")


def accout_information() -> str:
    acct_info = re.get("{}/v2/account".format(url), headers=keys).content
    # many ways to turn bytes to dict (an obj in JSON). The data.decode('utf-8'), str(data, 'utf-8'), bytearray(data)
    info = json.loads(acct_info.decode("utf-8"))  # This is now a dict (JSON obj)

    selected_items = {
        "buying_power": info.get("buying_power"),
        "equity": info.get("equity"),
        "portfolio_value": info.get("portfolio_value"),
    }
    
    return "\n".join(
        f"{key.capitalize()}: ${int(value):,}" for key, value in selected_items.items()
    )


def get_asset(_symbol: str):  # Allow for user input
    assets = re.get(
        "{}/v2/assets/{}".format(url, _symbol.upper()), headers=keys
    ).content
    asset_info = json.loads(assets.decode("utf-8"))
    selected_items = {
        "name": asset_info.get("name"),
        "symbol": asset_info.get("symbol"),
        "exchange": asset_info.get("exchange"),
    }

    return "\n".join(
        f"{key.capitalize()}: {value}" for key, value in selected_items.items()
    )  # return exchange, symbol, name


# def create_order(object:list) -> list:
#     ...
# This should be able to in multiple orders, then place them


# Turn into async function for multi-order queue
# Should return an order id
def place_order(
    _symbol: str, _qty: int, _buy_or_sell: str, _order_type: str, _time_in_force: str
):
    order = {
        "symbol": _symbol.upper(),
        "qty": _qty,
        "side": _buy_or_sell,
        "type": _order_type,
        "time_in_force": _time_in_force,
    }

    order_placed = re.post("{}/v2/orders".format(url), json=order, headers=keys).content
    order_info = json.loads(order_placed.decode('utf-8'))
    
    return f'Order-ID: {order_info.get('id')}'


# Single cancel orders ... Eventually turn into multi-cancel queue
def cancel_order(_symbol: str) -> str:
    order_canceled = re.delete(
        "{}/v2/positions/{}".format(url, _symbol.upper()), headers=keys
    )
    print(order_canceled.content, "True")


if __name__ == "__main__":
    # Test
    Main_Menu()
    # loo = 2
    # for i in range(loo):
    #     symbol:str = input("Symbol: ").upper()
    #     qty:int = input("Quantity: ")
    #     side:str  = input("Buy or Sell: ")
    #     order_type = input("Type: ")
    #     time_for_order:str  = input("Time: ")
    #     place_order(symbol, qty, side, order_type, time_for_order)
    #     print("================")
    # cancel_order('aapl')
