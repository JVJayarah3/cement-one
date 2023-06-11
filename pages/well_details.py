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
   if 'tvd' not in st.session_state:
      st.session_state['tvd'] = tvd
   if 'md' not in st.session_state:
      st.session_state['tvd'] = md
   if 'csd' not in st.session_state:
      st.session_state['tvd'] = csd
   if 'fc' not in st.session_state:
      st.session_state['tvd'] = fc
   if 'toc' not in st.session_state:
      st.session_state['tvd'] = toc
   if 'excess_cement' not in st.session_state:
      st.session_state['tvd'] = excess_cement
   if 'holesize' not in st.session_state:
      st.session_state['tvd'] = holesize
 
   switch_page("casing_details")

