from pandas_datareader import data as pdr
from xgboost.sklearn import XGBRegressor
import yfinance as yf
import xgboost as xgb
import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
import streamlit


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
    def __init__(self, data):
        self.data = data
        self.data_lagged = self.lag_prepare_data(data)
        self.X_train, self.X_test, self.Y_train, self.Y_test = self.x_y(self.data_lagged)
        self.y_result, self.results, self.r_sq = self.xgboost_regresson_applience(self.X_train, self.X_test, self.Y_train, self.Y_test)
        #self.y_result, self.results, self.r_sq = self.linear_regression_applience(self.X_train, self.X_test, self.Y_train, self.Y_test)


    def lag_prepare_data(self, df, trailing_window_size = 1):
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

    def x_y(self, df_lagged, test_size = 0.3, seed = 7):
        #df_lagged = self.lag_prepare_data(df_raw)

        y_cols = ['Close'] 
        Y = df_lagged[y_cols]
        X = df_lagged[df_lagged.columns.difference(y_cols)]
        #print(X, Y)
        X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
        
        return X_train, X_test, Y_train, Y_test

    def linear_regression_applience(self, X_train, X_test, Y_train, Y_test):
        model = LinearRegression()
        model.fit(X_train, Y_train)
        predictions = model.predict(X_test)
        r_sq = model.score(X_test, Y_test)
        Y_test['Result'] = predictions
        return predictions, Y_test, r_sq
        

    def xgboost_regresson_applience(self, X_train, X_test, Y_train, Y_test):
        params = {
                'eta': 1,
                'objective': 'binary:logistic',
                'gamma': 0.01,
                'max_depth': 8,
            }
        #xgbtrain = xgb.DMatrix(X_train, Y_train)
        reg = XGBRegressor(n_estimators=500, learning_rate=0.01)
        #print(X_train, Y_train)
        reg.fit(X_train, Y_train) #, eval_set=[(X_train, Y_train), (X_test, Y_test)])

        predictions = reg.predict(X_test)
        r_sq = reg.score(X_test, Y_test)
        Y_test['Result'] = predictions
        #predictions = 1
        #Y_test =1 
        return predictions, Y_test, r_sq



df_raw = get_data(av_instruments[0], start_date, end_date)
#sample_prediction = TimeSeries(df_raw)

#print(sample_prediction.r_sq)



