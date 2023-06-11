import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
st.text("Test")
for key in st.session_state.keys():
  del st.session_state[key]
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

with st.container():
  st.title("CASING - DETAILS")
  od = st.number_input("ENTER THE OD OF CASING",)
  id = st.number_input("ENTER THE ID OF CASING",)
  pump_out = st.number_input("PUMP OUTPUT (BBLS/STK)",)
casing_cap = ((id**2)/1029.4)
shoetrack = casing_cap*(csd-fc)
rathole = ((od**2)/1029.4)*(md-csd)
annulus_vol = (((holesize**2)-(od**2))/1029.4)*((md-toc)-(md-csd))
total_slurry_needed = shoetrack+rathole+annulus_vol
sub1 = st.button("SUBMIT")
if sub1:
  st.write("total_slurry_needed"+str(total_slurry_needed))
  if 'total_slurry_need' not in st.session_state:
      st.session_state['total_slurry_need'] = total_slurry_needed
  if 'pump_out' not in st.session_state:
      st.session_state['pump_out'] = pump_out
  switch_page("receipe")
st.write("----------------------------------------------------")
 
