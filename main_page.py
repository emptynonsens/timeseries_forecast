
import streamlit as st

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

av_instruments_names = ['S&P 500 ETF', 'CD PROJECT RED', 'TEN SQUARE GAMES', 'APPLE', 'OTHER']
av_instruments = ['SPY', 'CDR.WA', 'TEN.WA', 'AAPL', 'TYPE IN YOUR INSTRUMENT ALIAS']
start_date = '2017-01-01'
end_date = '2017-05-01'

def get_ticker_from_name(name_list, chosen_name, ticker_list):
    n=0
    for element in name_list:
        if element == chosen_name:
            break
        n +=1
    return n

instrument_name = st.sidebar.selectbox('Select one of the folling financial instruments',av_instruments_names)
ticker_num = get_ticker_from_name(av_instruments_names, instrument_name, av_instruments)
instrument_ticker = st.sidebar.write("You've chosen " + str(av_instruments[ticker_num]) )

#st.write(a)

class StreamlitApp:
    def init():
        main = '__main__'    