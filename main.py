import streamlit as st
import pandas as pd


titanic = pd.read_csv("titanic.csv")

st.title("Titanic, Supervivientes:")

st.table(data=titanic[["Age", "Sex"]])

"""
 Objetivo: Usando https://docs.streamlit.io/develop/api-reference crear 3 elementos para mostrar datos de Titanic.
 Los datos están en Pandas ->  
    Ejemplos - ayuda: 
        https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html
        https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html

""" 