import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "palmerpenguins.png")
DATA_PATH = os.path.join(dir_of_interest, "data", "penguins.csv")

st.title("Dashboard - Palmer Penguins")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

species = st.selectbox("Select the Species:", df['species'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['species'] == species], x="body_mass_g")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['species'] == species], y="body_mass_g")
col2.plotly_chart(fig_2, use_container_width=True)

col3, col4 = st.columns(2)

fig_3 = px.histogram(df[df['species'] == species], x="flipper_length_mm")
col3.plotly_chart(fig_3, use_container_width=True)

fig_4 = px.box(df[df['species'] == species], y="flipper_length_mm")
col4.plotly_chart(fig_4, use_container_width=True)