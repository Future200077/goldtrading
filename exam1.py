
import requests
from datetime import datetime, timedelta 
from dotenv import load_dotenv
import os
load_dotenv()
CONFIG = {
    'SYMBOLS': ['GC=F', 'XAUUSD=X', 'BTC-USD', 'ETH-USD'],
    'MAX_TRADE_AMOUNT': 1000000,
    'RISK_THRESHOLD': 0.85,
    'DATA_REFRESH_INTERVAL': 300,
    'MAX_POSITION_SIZE': 0.1,
    'IBKR_HOST': '127.0.0.1',
    'IBKR_PORT': 7497,
    'COINGECKO_SYMBOL_MAP': {
        'BTC-USD': 'bitcoin',
        'ETH-USD': 'ethereum',
        'GC=F': 'gold',
        'XAUUSD=X': 'gold'
    }
}
original_symbol='XAUUSD=X'
symbol_variant = 'XAUUSD=X'
COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")
print(COINGECKO_API_KEY)

cg_symbol = CONFIG['COINGECKO_SYMBOL_MAP'].get(original_symbol)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(cg_symbol)
if 'USD' in symbol_variant and not 'XAU' in symbol_variant and COINGECKO_API_KEY:
    if cg_symbol:
        url = f"https://api.coingecko.com/api/v3/simple/price"
        params = {'ids': cg_symbol, 'vs_currencies': 'usd'}
        response = requests.get(url, params=params).json()
        print("price")
        print(response[cg_symbol]['usd'])
        print('timestamp')
        print(datetime.now())
        # return {
        #     'price': response[cg_symbol]['usd'],
        #     'timestamp': datetime.now()
        # }