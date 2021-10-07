import streamlit as st 
import pandas as pd
from PIL import Image
import src.support as sp
import numpy as np



def app():
    st.plotly_chart(sp.esp_primer_graf())

    Total_ski_routes = st.slider('Minimum ski routes (km)', 1, 160, 20)
    Lifts = st.slider('Minimum lifts available?', 3, 29, 8)
    adult_price = st.slider('Maximum you will pay for a day?(€)', 22, 55, 34)


    if Total_ski_routes == 20 and Lifts == 8 and adult_price == 34:
        st.stop()

    df = sp.load_data_es()
    
    loqsea = sp.saca_tu_estacion(df,Total_ski_routes, Lifts,adult_price)
    
    st.dataframe(loqsea)

 
    pass

