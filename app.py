import streamlit as st
import pandas as pd
import plotly.express as px
import balance, wins_bo1, wins_bo3
from PIL import Image

PAGES = {
    'Balance': balance,
    'Wins(BO1)': wins_bo1,
    'Wins(BO3)': wins_bo3
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]

# img = Image.open('./media/icon.png')
# st.sidebar.image(img)

page.app()
