import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import numpy as np

df = st.session_state['df']
st.dataframe(df)
