from pandas_datareader import data as pdr
import yfinance as yf
import xgboost as xgb
import pandas as pd



 # <== that's all it takes :-)

# download dataframe



av_instruments_names = ['S&P 500 ETF', 'CD PROJECT RED', 'TEN SQUARE GAMES', 'APPLE']
av_instruments = ['SPY', 'CDR.WA', 'TEN.WA', 'AAPL']
start_date = '2017-01-01'
end_date = '2017-05-01'

def get_data(fin_instrument, start, end):
    yf.pdr_override()
    raw_data = pdr.get_data_yahoo(fin_instrument, start, end)
    data = raw_data.loc[:, raw_data.columns != 'Adj Close']
    return data
 


class TimeSeries:
    def __init__(self, data, x, y):
        self.data = data
        self.x = x
        self.y = y
        # napisać funckje, które zrobią te rzeczy
    
    def x_of_data(data):
        pass

    def y_of_data(data):
        pass



df_raw = get_data(av_instruments[0], start_date, end_date)

def lag_prepare_data(df):
    trailing_window_size = 1
    df_lagged = df.copy()
    lag_exp = '_lag'
    exeption_cols = ['Open', 'High', 'Low']
    for window in range(1, trailing_window_size + 1):
        shifted = df.shift(window)
        shifted.columns = [x + lag_exp + str(window) for x in df.columns]
    
        df_lagged = pd.concat((df_lagged, shifted), axis=1)
    df_lagged = df_lagged.dropna()
    list_of_cols = df_lagged.columns.difference(exeption_cols)

    df_final = df_lagged[list_of_cols].copy()
    return df_final

df_lagged = lag_prepare_data(df_raw)

y_cols = ['Close','Volume']

y = df_lagged[y_cols]
x = df_lagged[df_lagged.columns.difference(y_cols)]

