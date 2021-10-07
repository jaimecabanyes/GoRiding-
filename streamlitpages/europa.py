import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
import plotly.express as px
import plotly.graph_objects as go
import folium
from geopy.geocoders import Nominatim 
import src.support as sp
import streamlit as st 

def app():
    st.plotly_chart(sp.primer_grafico_eu())
    st.plotly_chart(sp.segundo_grafico_eu())