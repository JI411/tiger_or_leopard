from src.app import app
import streamlit as st
from src.download import load_data, load_weights

if 'downloaded' not in st.session_state:
    load_data()
    load_weights()
    st.session_state['downloaded'] = True

app()
