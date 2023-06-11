import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.title("Test")
with st.container():
  st.title("WELL-DETAILS")
  tvd = st.number_input("ENTER THE TVD (ft)",)
  md = st.number_input("ENTER THE MD  (ft)",)
  csd = st.number_input("ENTER THE SHOE DEPTH  (ft)",)
  fc = st.number_input("ENTER THE F/C DEPTH  (ft)",)
  toc = st.number_input("ENTER THE TOC  (ft)",)
  excess_cement = st.number_input("Excess Volume Pecentage (normally 20%)",)
  holesize = st.number_input("ENTER THE AVERAGE HOLE SIZE (IN)",)
st.write("----------------------------------------------------")
submit1 = st.button("SUBMIT")
if submit1:
    switch_page("casing_details")

