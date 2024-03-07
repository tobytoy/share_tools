import streamlit as st
import threading
import subprocess
import pandas as pd
import numpy as np
import configparser

st.set_page_config(layout="wide")

config = configparser.ConfigParser()
config.read('config.ini')

def config_write():
    with open('config.ini', 'w') as configfile:    # save
        config.write(configfile)


# Sider Part
st.sidebar.title("躲貓咪的家")
expander_cat = st.sidebar.expander("meow meow")
expander_cat.image("images/cat-1796834_1280.jpg")
add_selectbox = st.sidebar.selectbox(
    "咪咪管家幫你",
    ("Setting", "Threading", "Mobile phone")
)
with st.sidebar:
    if str(add_selectbox) == "Setting":
        config['set']['terminal'] = str(st.checkbox('terminal', config['set'].getboolean('terminal')))
        config_write()
    

    # add_radio = st.radio(
    #     "Choose a shipping method",
    #     ("Standard (5-15 days)", "Express (2-5 days)")
    # )
    # st.button("Reset", type="primary")
    # if st.button('Say hello'):
    #     st.write('Why hello there')
    # else:
    #     st.write('Goodbye')


# Main Part
st.title('你是傻貓貓')
st.text(str(add_selectbox))


tabs = st.tabs(["Installer", "Terminal", "Owl"])

with tabs[0]:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tabs[1]:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tabs[2]:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


# terminal
if config['set'].getboolean('terminal'):
    expander = st.expander("Terminal")
    expander.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
    expander.image("https://static.streamlit.io/examples/dice.jpg")

