import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv('sc.csv')
data = pd.DateFrame(col
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


