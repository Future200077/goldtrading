import pandas as pd
import numpy as np

def moving_average(data, window=50):
    """
    Calculate the Simple Moving Average (SMA) for a given window.
    
    Args:
    - data: pd.DataFrame containing market data (e.g., close prices).
    - window: int, the period of the moving average.

    Returns:
    - pd.Series: SMA for the 'close' column.
    """
    if 'close' not in data.columns:
        raise ValueError("Data must contain a 'close' column.")
    return data['close'].rolling(window=window).mean()


def relative_strength_index(data, window=14):
    """
    Calculate the Relative Strength Index (RSI) for a given window.
    
    Args:
    - data: pd.DataFrame containing market data (e.g., close prices).
    - window: int, the period of the RSI.

    Returns:
    - pd.Series: RSI for the 'close' column.
    """
    if 'close' not in data.columns:
        raise ValueError("Data must contain a 'close' column.")

    delta = data['close'].diff(1)
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def macd(data, fast_period=12, slow_period=26, signal_period=9):
    """
    Calculate the Moving Average Convergence Divergence (MACD) and Signal Line.
    
    Args:
    - data: pd.DataFrame containing market data (e.g., close prices).
    - fast_period: int, period for the fast EMA.
    - slow_period: int, period for the slow EMA.
    - signal_period: int, period for the signal line.

    Returns:
    - tuple: (macd, signal_line)
    """
    if 'close' not in data.columns:
        raise ValueError("Data must contain a 'close' column.")
        
    fast_ema = data['close'].ewm(span=fast_period, adjust=False).mean()
    slow_ema = data['close'].ewm(span=slow_period, adjust=False).mean()

    macd = fast_ema - slow_ema
    signal_line = macd.ewm(span=signal_period, adjust=False).mean()

    return macd, signal_line


def exponential_moving_average(data, window=50):
    """
    Calculate the Exponential Moving Average (EMA) for a given window.
    
    Args:
    - data: pd.DataFrame containing market data (e.g., close prices).
    - window: int, the period of the EMA.

    Returns:
    - pd.Series: EMA for the 'close' column.
    """
    if 'close' not in data.columns:
        raise ValueError("Data must contain a 'close' column.")
    return data['close'].ewm(span=window, adjust=False).mean()


