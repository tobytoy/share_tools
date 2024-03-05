import streamlit as st
import threading
import subprocess
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

    st.button("Reset", type="primary")
    if st.button('Say hello'):
        st.write('Why hello there')
    else:
        st.write('Goodbye')



st.title('Uber pickups in NYC')
st.text(str(add_selectbox))


tab1, tab2, tab3 = st.tabs(["Installer", "Terminal", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


expander = st.expander("See explanation")
expander.write("""
    The chart above shows some numbers I picked for you.
    I rolled actual dice for these, so they're *guaranteed* to
    be random.
""")
expander.image("https://static.streamlit.io/examples/dice.jpg")

