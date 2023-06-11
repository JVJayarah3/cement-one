import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import numpy as np

df = st.session_state['df']
total_slurry_needed = st.session_state['total_slurry_need'] 
pump_out = st.session_state['pump_out']
displacement_fluid = st.session_state['displacement_fluid']
displacing_mud = st.session_state['displacing_mud']
old_mud = st.session_state['old_mud']
toc = st.session_state['toc']
tvd = st.session_state['tvd']
fc = st.session_state['fc']
od = st.session_state['od']
csd = st.session_state['csd']
excess_cement = st.session_state['excess_cement']
client = st.session_state['client']
well_name = st.session_state['well_name']
date = st.session_state['date']
dead_vol = st.session_state['dead_vol']
bump_p = st.session_state['bump_p']
cement_den = st.session_state['cement_den']
cement_sk = st.session_state['cement_sk']
preflush = st.session_state['preflush']
woc = st.session_state['woc']
md = st.session_state['md']
df = st.session_state['df']


st.dataframe(df)
