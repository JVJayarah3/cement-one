import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
st.text("Test")

total_slurry_needed = 52
#total_slurry_needed = st.session_state['total_slurry_need'] 

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
    bowc1 = st.number_input("BWOC PERCENTAGE - ",key=1)
    bowc2 = st.number_input("BWOC PERCENTAGE - ",key=2)
    bowc3 = st.number_input("BWOC PERCENTAGE - ",key=3)
    bowc4 = st.number_input("BWOC PERCENTAGE - ",key=4)
    bowc5 = st.number_input("BWOC PERCENTAGE - ",key=5)
         
  with col3:
    galsk1 = st.number_input("GAL/SACK - ",key=1)
    galsk2 = st.number_input("GAL/SACK - ",key=2)
    galsk3 = st.number_input("GAL/SACK - ",key=3)
    galsk4 = st.number_input("GAL/SACK - ",key=4)
    galsk5 = st.number_input("GAL/SACK - ",key=5)

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
            
            
            
