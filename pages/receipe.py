import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
st.text("Test")

total_slurry_needed = st.session_state['total_slurry_need'] 
with st.container():
  st.title("TOTAL VOLUME OF SLURRY NEEDED - ")
  
