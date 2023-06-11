import streamlit as st
import pandas as pd

st.text("Test")
with st.container():
  st.title("CASING - DETAILS")
  od = st.number_input("ENTER THE OD OF CASING",)
  id = st.number_input("ENTER THE ID OF CASING",)
  casing_cap = ((id**2)/1029.4)
button1  = st.button("SUBMIT")
shoetrack = casing_cap*(csd-fc)
if button1:
  st.write("CEMENT VOLUME IN SHOE TRACK"+str(shoetrack)+"bbls")
  
 
