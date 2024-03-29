﻿
import streamlit as st
from StereamLit_timeseries_forecast import *
from streamlit import *
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from main_html import *
import datetime

    

class StreamlitApp:
    def __init__(self, title):
        self.main = '__main__'
        self.page_config = st.set_page_config(layout = 'wide')
        self.github = st.write('Check out [GITHUB](https://github.com/emptynonsens/timeseries_forecast) for this project', unsafe_allow_html=True)
        self.tile = st.markdown(title) 
        self.sidebar_title = st.sidebar.markdown(title)
        self.av_instruments_names = ['S&P 500 ETF', 'CD PROJECT RED', 'TEN SQUARE GAMES', 'APPLE', 'OTHER']
        self.av_tickers = ['SPY', 'CDR.WA', 'TEN.WA', 'AAPL', 'TYPE IN YOUR INSTRUMENT ALIAS']
        self.start_date = st.sidebar.date_input("Timeseries start date",datetime.date(2021, 1, 1))
        self.end_date = st.sidebar.date_input("Timeseries end date",datetime.date(2022, 1, 1))
        self.ticker = self.get_ticker(self.av_instruments_names, self.av_tickers)
        self.present_data = self.present_data(self.ticker, self.start_date, self.end_date)
        self.custom_html = css_html()

    def get_ticker(self, av_instruments_names, av_tickers):
        def get_ticker_num(av_instruments_names, chosen_name):
            n=0
            for element in av_instruments_names:
                if element == chosen_name:
                    break
                n +=1
            return n
        
        instrument_name = st.sidebar.selectbox('Select one of the folling financial instruments',av_instruments_names)
        ticker_num = get_ticker_num(av_instruments_names, instrument_name)

        if instrument_name == 'OTHER':
            instrument_ticker = st.sidebar.text_input(label = 'Type in your ticker')
            if instrument_ticker == '':
                return ''
            else:
                return instrument_ticker
        else:
            instrument_ticker = av_tickers[ticker_num]
            instrument_ticker_info = st.sidebar.write("You've chosen " +str(instrument_ticker))
            #present_data(instrument_ticker)
        return instrument_ticker

    def plot_chart_of_data(self, plot_data):
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Bar(x=plot_data.index, y=plot_data['Volume'], name="Volume"),secondary_y=True,)
        fig.add_trace(go.Scatter(x=plot_data.index, y=plot_data['Close'], name="Close price"),secondary_y=False,)
        fig.update_layout(title_text="Closing and volume over time")
        # Set x-axis title
        #fig.update_xaxes(title_text="xaxis title")
        # Set y-axes titles
        fig.update_yaxes(title_text="<b>Closing</b> price", secondary_y=False)
        fig.update_yaxes(title_text="<b>Volume</b> of ticker", secondary_y=True)
        fig.update_layout(width=1000, height=550)

        chart = st.write(fig)

    def present_data(self, ticker, start_date, end_date):
        if ticker == '':
            st.markdown('waiting for ticker')
        else:
            df_raw = get_data(str(ticker), start_date, end_date)
            st.dataframe(df_raw)
            plot_data = self.plot_chart_of_data(df_raw)
            button = st.download_button(label="Download data as CSV",data=df_raw.to_csv().encode('utf-8'),file_name='timeseries.csv',mime='text/csv',)

        

title = "# Home 🧮"
main_page = StreamlitApp(title)







