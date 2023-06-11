import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import numpy as np
st.text("Test")

total_slurry_needed = 52
pump_out = 0.084
#total_slurry_needed = st.session_state['total_slurry_need'] 
#pump_out = st.session_state['pump_out']

with st.container():
  st.title("CEMENTING - DETAILS")
  st.header("TOTAL VOLUME OF SLURRY NEEDED - "+str(total_slurry_needed))
  cementyld = st.number_input("CEMENT YIELD (CF-SK) - ",min_value=0.1)  
  cement_sk = (total_slurry_needed/(cementyld*0.178))         
  st.header("CEMENT-RECEIPE")
  col1,col2,col3 = st.columns(3)
  with col1:
    name1 = st.text_input("RECEIPE NAME - ",key=1)
    name2 = st.text_input("RECEIPE NAME - ",key=2)
    name3 = st.text_input("RECEIPE NAME - ",key=3)
    name4 = st.text_input("RECEIPE NAME - ",key=4)
    name5 = st.text_input("RECEIPE NAME - ",key=5)
            
  with col2:
    bowc1 = st.number_input("BWOC PERCENTAGE - ",key=6)
    bowc2 = st.number_input("BWOC PERCENTAGE - ",key=7)
    bowc3 = st.number_input("BWOC PERCENTAGE - ",key=8)
    bowc4 = st.number_input("BWOC PERCENTAGE - ",key=9)
    bowc5 = st.number_input("BWOC PERCENTAGE - ",key=10)
         
  with col3:
    galsk1 = st.number_input("GAL/SACK - ",key=11)
    galsk2 = st.number_input("GAL/SACK - ",key=12)
    galsk3 = st.number_input("GAL/SACK - ",key=13)
    galsk4 = st.number_input("GAL/SACK - ",key=14)
    galsk5 = st.number_input("GAL/SACK - ",key=15)

df = pd.DataFrame()
df['receipe_name'] = [name1,name2,name3,name4,name5]
df['bwoc'] = [bowc1,bowc2,bowc3,bowc4,bowc5]
df['galsk'] = [galsk1,galsk2,galsk3,galsk4,galsk5]
try:           
  df['output-1'] = ((df['bwoc']/100)*94*cement_sk)
except:
  pass         
df['output-2'] = df['galsk']*cement_sk          
df['unit-1'] = np.where(df['output-1'] != 0 ,"Lbs","")     
df['unit-2'] = np.where(df['output-2'] != 0 ,"Gal","") 
df['output'] = df['output-1'] + df['output-2']           
df['unit'] =   df['unit-1'] + df['unit-2'] 
bt0 = st.button("SUBMIT")
if bt0:
  st.dataframe(df)          
            
            
            
