
import streamlit as st
from StereamLit_timeseries_forecast import *
from streamlit import *
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(layout = 'wide')

st.markdown("# Home 🧮")
st.sidebar.markdown("# Home 🧮")

av_instruments_names = ['S&P 500 ETF', 'CD PROJECT RED', 'TEN SQUARE GAMES', 'APPLE', 'OTHER']
av_instruments = ['SPY', 'CDR.WA', 'TEN.WA', 'AAPL', 'TYPE IN YOUR INSTRUMENT ALIAS']
start_date = '2017-01-01'
end_date = '2022-05-01'

def get_ticker_from_name(name_list, chosen_name, ticker_list):
    n=0
    for element in name_list:
        if element == chosen_name:
            break
        n +=1
    return n

def plot_chart_of_data(plot_data):
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(x=plot_data.index, y=plot_data['Volume'], name="yaxis2 data"),secondary_y=True,)
    fig.add_trace(go.Scatter(x=plot_data.index, y=plot_data['Close'], name="yaxis data"),secondary_y=False,)
    fig.update_layout(title_text="Double Y Axis Example")
    # Set x-axis title
    fig.update_xaxes(title_text="xaxis title")
    # Set y-axes titles
    fig.update_yaxes(title_text="<b>primary</b> yaxis title", secondary_y=False)
    fig.update_yaxes(title_text="<b>secondary</b> yaxis title", secondary_y=True)
    fig.update_layout(width=1000, height=550)

    chart = st.write(fig)

instrument_name = st.sidebar.selectbox('Select one of the folling financial instruments',av_instruments_names)
ticker_num = get_ticker_from_name(av_instruments_names, instrument_name, av_instruments)

def present_data(ticker, start_date = start_date, end_date = end_date):
    df_raw = get_data(str(ticker), start_date, end_date)
    st.dataframe(df_raw)
    plot_data = plot_chart_of_data(df_raw)

if instrument_name == 'OTHER':
    instrument_ticker = st.sidebar.text_input(label = 'Type in your ticker')
    
    if instrument_ticker == '':
        a = ''
    else:
        present_data(instrument_ticker)
else:
    instrument_ticker = av_instruments[ticker_num]
    instrument_ticker_info = st.sidebar.write("You've chosen " +str(instrument_ticker))
    present_data(instrument_ticker)



class StreamlitApp:
    def init():
        main = '__main__'    