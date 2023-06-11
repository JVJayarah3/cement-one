import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
st.text("Test")
butn = st.button("SUBMIT")
if butn:
  switch_page("well_details")

 
