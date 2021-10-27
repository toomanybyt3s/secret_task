from fastapi import FastAPI
import uvicorn
from pycoingecko import CoinGeckoAPI

app = FastAPI()
cg = CoinGeckoAPI()


@app.get("/")
def root():
    return {"Hello": "World",
        "/price/`coin`}":"Returns current 'coin' price",
        "/market/'coin'":"Returns all the information about hence 'coin'"
    }


@app.get("/price/{coin}")
def get_price(coin: str):
    price = cg.get_price(ids=coin, vs_currencies='eur', include_market_cap=True)
    if price != {}:
        return price
    else:
        return {"error":"Please type in a valid full coin name eg `Bitcoin`"}
    

@app.get("/market/{coin}")
def get_market(coin: str):
    market = cg.get_coins_markets(ids=coin, vs_currency='eur')
    if market != {}:
        return market
    else:
        return {"error":"Please type in a valid full coin name eg `Bitcoin`"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000)