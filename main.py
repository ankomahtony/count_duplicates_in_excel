import streamlit as st
import pandas as pd
import numpy as np

st.title('Count Duplicates')

@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')


uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_excel(uploaded_file)
     
     
     option = st.selectbox(
     'Which column do you want to be checked with ?',
        list(dataframe.columns.values))
     
     count = dataframe[option].value_counts()
     
     st.table(count);
     csv = convert_df(count)
     st.download_button(
        "Press to Download Count Data",
        csv,
        option+"_duplicates.csv",
        "text/csv",
        key='download-csv'
    )
     
     
     agree = st.checkbox('Show Original Data')
     if agree:
        st.write(dataframe)
        
       
        