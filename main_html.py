import streamlit as st

#st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

def css_html():
    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: rgb(210, 80, 49)
        ;color:white
        ;font-size:20px
        ;height:1.8em
        ;width:15em
        ;border-radius:10px 10px 10px 10px;
    }
    
    div.stDownloadButton:nth-child(2) {
        background-color: rgb(255, 255, 255);
        color: rgb(38, 10, 48);
        padding: 0.25em 0.38em;
        position: middle;
        text-decoration: none;
        border-radius: 4px;
        border-width: 10px;
        border-style: solid;
        border-color: rgb(230, 234, 241);
        border-image: initial;
    
    }
    div.stDownloadButton :hover {
        border-color: rgb(246, 10, 102);
        color: rgb(246, 51, 102);
    }
    div.stDownloadButton:active {
        box-shadow: none;
        background-color: rgb(246, 51, 102);
        color: white;
        }


    </style>
    
    """, unsafe_allow_html=True)
    return m