import streamlit as st
import numpy as np
import pandas as pd

st.title("Live data stream")

df = pd.read_csv('data.csv')
df.columns = ['id', 'time stamp', 'e1', 'e2', 'e3']

st.dataframe(df[['time stamp', 'e1', 'e2', 'e3']])
