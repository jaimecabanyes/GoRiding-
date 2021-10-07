import streamlit as st
import pandas as pd
import src.support as sp
from PIL import Image
from mulitpage import MultiPage
from streamlitpages import distribucionglob
from streamlitpages import esp
from streamlitpages import europa



st.title ("""
GoRiding!!
""")

app = MultiPage()

app.add_page('GLOBAL', distribucionglob.app)

app.add_page('SPAIN', esp.app)

app.add_page('EUROPE', europa.app)

app.run()
