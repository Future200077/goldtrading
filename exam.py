# import yfinance as yf
# data = yf.Ticker("XAUUSD=X")
# # Adjust to weekdays (gold trades from Sun 6PM ET - Fri 5PM ET)
# info = data.info
# print(info)  # Should print details about XAUUSD

# # hist = data.history(period="5d", interval="1h")  # Last 5 days, hourly data
# # print(hist)

# import requests
# POLYGON_API_KEY = '4LmcqdksDnc53KzDbEEbFwXBCNiJOT1T'
# polygon_symbol = 'C:XAUUSD'

# url = f"https://api.polygon.io/v2/aggs/ticker/{polygon_symbol}/prev"
# # url = f"https://api.polygon.io/v2/aggs/ticker/{polygon_symbol}/range/1/day/2025-03-01/2025-03-17"
# # url = f"https://api.polygon.io/v3/trades/C:GCM24?limit=5&apiKey=POLYGON_API_KEY"
# response = requests.get(url, params={'apiKey': POLYGON_API_KEY}).json()
# # response = requests.get(url).json()
# print(f"📡 Polygon.io Data for {polygon_symbol}:")
# print("(((((()))))(((((()))))))")
# print(response)
# print(response.get('results'))


import yfinance as yf
from pycoingecko import CoinGeckoAPI
from polygon.rest import RESTClient
import pandas as pd
import logging
from typing import Optional, Dict, Any, List
import os
from dotenv import load_dotenv
from datetime import datetime
import numpy as np
import scipy.stats as stats
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from statsmodels.tsa.arima.model import ARIMA
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from threading import Thread
import hashlib
import pytz
from openai import OpenAI
load_dotenv()
print(os.getenv('OPENAI_API_KEY'))

symbols = ['AAPL', 'BTC', 'XAU-USD']
symbol = 'BTC'
start_date = '2000-01-01'
end_date = datetime.today().strftime('%Y-%m-%d')
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

try:
    logger.info(f"Fetching data from Polygon.io for {symbol}...")
    POLYGON_API_KEY = os.getenv('POLYGON_API_KEY')
    if not POLYGON_API_KEY:
        raise ValueError("Polygon API key is missing.")
    client = RESTClient(POLYGON_API_KEY)

    if symbol == "GOLD":
        symbol = "XAU-USD"
    historical_data = client.get_aggs(symbol, 1, "day", start_date, end_date)
    if historical_data:
        df = pd.DataFrame(historical_data)
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
    else:
        raise ValueError(f"No data found for symbol: {symbol} in Polygon.")
    
    print(df)
except Exception as e:
    logger.error(f"Error fetching data for {symbol} from Polygon: {e}")