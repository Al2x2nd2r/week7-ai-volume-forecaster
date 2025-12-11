import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error

# Configuration
DATA_PATH = 'data/historical_volumes.csv'
MA_WINDOW = 7
ALPHA = 0.3

# Load data
df = pd.read_csv(DATA_PATH)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Ensure 'volume' exists
if 'volume' not in df.columns:
    raise RuntimeError("'volume' column not found in data")

vol = df['volume']

# 1) Moving Average forecast (window=MA_WINDOW)
df[f'MA_{MA_WINDOW}'] = vol.rolling(window=MA_WINDOW).mean()
# Shift MA to represent forecast for next period
ma_preds = df[f'MA_{MA_WINDOW}'].shift(1).dropna()
ma_actual = vol.loc[ma_preds.index]
mae_ma = mean_absolute_error(ma_actual, ma_preds)

# 2) Exponential smoothing (matching class logic)
result = [vol.iloc[0]]
for i in range(1, len(vol)):
    forecast = ALPHA * vol.iloc[i-1] + (1 - ALPHA) * result[-1]
    result.append(forecast)
exp_series = pd.Series(result, index=vol.index)
# Shift to align forecasts for the next period
exp_preds = exp_series.shift(1).dropna()
exp_actual = vol.loc[exp_preds.index]
mae_exp = mean_absolute_error(exp_actual, exp_preds)

# Print results
print(f"Data points: {len(vol)}")
print(f"MA (window={MA_WINDOW}) MAE: {mae_ma:.4f}")
print(f"Exponential smoothing (alpha={ALPHA}) MAE: {mae_exp:.4f}")
