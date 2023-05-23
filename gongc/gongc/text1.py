import streamlit as st
import numpy as np
import pandas as pd
import time
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
df = pd.read_csv('sc.csv')
data = pd.read_csv('111.csv')
label_t = df['label']
#创建file_uploader组件
uploaded_file = st.file_uploader("Choose a file", type={"csv", "txt"})
if uploaded_file is not None:
     # To read file as bytes:
     spectra = pd.read_csv(uploaded_file )
     label_p = spectra['label']
     sc = sum(label_t==label_p)/len(label_t)
     name=uploaded_file.name.split('.')[0]
     st.write(name)     
     st.write(sc)
     data = data.append({'name':name,'score':sc,'s_time':now},ignore_index=True)
     st.write(data)
     data = data.sort_values(by=['score', 's_time'], ascending=[False,True])
     data.to_csv('111.csv',index=False)
     


