from os import name
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
import plotly.express as px
px.set_mapbox_access_token('pk.eyJ1IjoiamFpbWVjYWJhbnllcyIsImEiOiJja3VmbGU0NnUwbm1yMnFudmNyZmJ3dmNmIn0.qOLos9ziMX3SVitpJlowvw')
import pandas as pd
import plotly.graph_objects as go
from geopy.geocoders import Nominatim
from streamlit.proto.PlotlyChart_pb2 import Figure 
import streamlit as st

def load_data():
    df = pd.read_csv('Data2/FINAL!!!!!.csv')
    df = df.drop(columns='Unnamed: 0')
    df.rename(columns={'Adults': 'Adult Price (€/$)'}, inplace=True)
    return df

def primer_gráfico_co():
    df = load_data()
    agrupado = df.groupby(['Continent']).agg({'Total_ski_routes': 'sum'})
    Number_Ski_Resorts = [176, 422]
    agrupado['Number_ski_Resorts'] = Number_Ski_Resorts
    agrupado.reset_index(inplace=True)
    fig = go.Figure([go.Bar(x=agrupado.Continent, y=agrupado.Total_ski_routes, text=agrupado.Number_ski_Resorts, textposition='outside',)])
    fig.update_xaxes(
        title_text = "Continent",
        title_font = {"size": 20},
        title_standoff = 25)
    fig.update_yaxes(
        title_text = "Total Ski Routes (km)",
        title_standoff = 25)

    return fig

def segundo_grafico_co():
    df = load_data()
    fig = px.scatter(df, x="Total_ski_routes", y="Adult Price (€/$)", color="Continent", trendline='ols')
    fig.update_xaxes(
        title_text = "Total Ski Routes (km)",
        title_font = {"size": 20},
        title_standoff = 25)
    fig.update_yaxes(
        title_text = "Adult Prices (€/$)",
        title_standoff = 25)
    return fig

def tercer_grafico_co():
    df = load_data()
    fig = px.box(df, x="Continent", y="Adult Price (€/$)")
    fig.update_xaxes(
        title_text = "Continent",
        title_font = {"size": 20},
        title_standoff = 25)
    fig.update_yaxes(
        title_text = "Adult Price (€/$)",
        title_standoff = 25)
    
    
    return fig



''''
ESPAÑAAAAAA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
def load_data_es():
    df = pd.read_csv('Data2/espfin')
    df = df.drop(columns='Unnamed: 0')
    return df


def esp_primer_graf():
    df = load_data_es()
    fig = px.scatter_mapbox(df,
                        lat=df.Lat,
                        lon=df.Lon,
                        hover_name="Name",
                        color = "CCAA",
                        mapbox_style= 'satellite-streets', 
                       center = {'lat':40.804246, 'lon':-4.004724},
                       zoom = 4.5)
    fig.update_layout(height=600,margin={"r":0,"t":30,"l":0,"b":0},title="Estaciones en España")

    return fig  


'''
EUROPA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

def load_data_eu():
    df = pd.read_csv('Data2/FINAL!!!!!.csv')
    df = df.drop(columns='Unnamed: 0')
    df.rename(columns={'Adults': 'Adult Price (€/$)'}, inplace=True)
    subset_europe = df[df["Continent"]== 'Europe']
    return subset_europe

def primer_grafico_eu(): 
    df = load_data_eu()
    subset_europe = df[df["Continent"]== 'Europe']
    a =subset_europe[["Country",  "Easy", "Intermediate", "Difficult"]]
    easy = a.groupby(["Country"])["Easy"].sum().reset_index()
    intermediate = a.groupby(["Country"])["Intermediate"].sum().reset_index()
    difficult = a.groupby(["Country"])["Difficult"].sum().reset_index()
    dfskiroutes = pd.concat((easy, intermediate.Intermediate, difficult.Difficult), axis=1)
    fig = go.Figure(data=[
        go.Bar(name='Easy', x=dfskiroutes.Country, y=dfskiroutes.Easy, marker_color="blue"),
        go.Bar(name='Intermediate', x=dfskiroutes.Country, y=dfskiroutes.Intermediate, marker_color="red"),
        go.Bar(name='Difficult', x=dfskiroutes.Country, y=dfskiroutes.Difficult, marker_color="black")
        ])
    fig.update_xaxes(
        tickangle = 90,
        title_text = "Country",
        title_font = {"size": 20},
        title_standoff = 25)
    fig.update_yaxes(
        title_text = "Total Ski Routes",
        title_standoff = 25)



        # Change the bar mode
    fig.update_layout(barmode='stack')

    return fig



def segundo_grafico_eu():
    df = load_data_eu()
    b = df[['Country', 'Min_Altitude','Max_Altitude']]
    minalt = b.groupby(["Country"])["Min_Altitude"].mean().reset_index()
    maxalt =  b.groupby(["Country"])["Max_Altitude"].mean().reset_index()
    minmax = pd.concat((minalt, maxalt.Max_Altitude), axis=1)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=minmax.Country, y=minmax.Min_Altitude, fill='tozeroy', name= 'Min Altitude')) # fill down to xaxis
    fig.add_trace(go.Scatter(x=minmax.Country, y=minmax.Max_Altitude, fill='tonexty', name= 'Max Altitude')) # fill to trace0 y
    fig.update_xaxes(
        tickangle = 90,
        title_text = "Country",
        title_font = {"size": 20},
        title_standoff = 25)
    fig.update_yaxes(
        title_text = "Min/Max Altitude (Average)",
        title_standoff = 25)
    
    return fig

'''
QUESTIONARIO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

def CC_AA():
    data = load_data()
    return list(data["CCAA"].unique())



#ccaa = CCAA()

def user_input_features():
    Total_ski_routes = st.sidebar.slider('Total_ski_routes', 1, 160, 20)
    Lifts = st.sidebar.slider('Lifts', 3, 29, 8)
    adult_price = st.sidebar.slider('Adult Price (€)', 22, 54, 34)
    CCAA = st.selectbox('CCAA', CC_AA())


    data = {
            'Total_ski_routes': Total_ski_routes,
            'Lifts': Lifts,
            'Adult Price (€)':adult_price,
            'CCAA': CCAA
            }

    return pd.DataFrame(data, index=[0])



def saca_tu_estacion(df, min_ski_r, lifts, ffprice):
        a = df[(df["Total_ski_routes"] >= min_ski_r) & (df["Lifts"] >= lifts) & (df["Adult Price (€)"] <= ffprice)]
        #b = a.fillna("Unknown")
        return a
