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


y_cols = ['Close'] 
Y = df_lagged[y_cols]
X = df_lagged[df_lagged.columns.difference(y_cols)]
print(df_lagged)
X = X
Y = Y
#X = df_lagged[:,0:4]
#Y = df_lagged[:,4]
#print(X, Y)


seed = 7
test_size = 0.33
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
params = {
        'eta': 1,
        'objective': 'binary:logistic',
        'gamma': 0.01,
        'max_depth': 8,
    }
xgbtrain = xgb.DMatrix(X_train, Y_train)
#bst = xgb.train(dtrain=xgbtrain, params=params)

#print(X, Y)
#model = XGBRegressor()
reg = XGBRegressor(n_estimators=500, learning_rate=0.01)
reg.fit(X_train, 
        Y_train,
        eval_set=[(X_train, Y_train), (X_test, Y_test)])

predictions = reg.predict(X_test)

Y_test['Result'] = predictions
#print(predictions)
print(Y_test)

#model = XGBClassifier()
#model.fit(X_train, y_train)
#
#https://www.youtube.com/watch?v=Wsfz3i1AXzY

#print(bst)
# make predictions for test data
#y_pred = model.predict(X_test)
#predictions = [round(value) for value in y_pred]

#print(y_pred)

#accuracy = accuracy_score(y_test, predictions)
#print("Accuracy: %.2f%%" % (accuracy * 100.0))

