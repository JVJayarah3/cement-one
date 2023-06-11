import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

csd = st.session_state['csd']
fc = st.session_state['fc']

with st.container():
  st.title("CASING - DETAILS")
  od = st.number_input("ENTER THE OD OF CASING",)
  id = st.number_input("ENTER THE ID OF CASING",)
  casing_cap = ((id**2)/1029.4)

shoetrack = casing_cap*(csd-fc)
button2  = st.button("SUBMIT")
if button2:
  switch_page("receipe")
