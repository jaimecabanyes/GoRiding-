import streamlit as st 
import pandas as pd
from PIL import Image
import src.support as sp

def app():

    st.write('''
        # Knowing About Global Ski Resorts
        ''')
    st.plotly_chart(sp.primer_gráfico_co())
    st.plotly_chart(sp.segundo_grafico_co())
    st.plotly_chart(sp.tercer_grafico_co())