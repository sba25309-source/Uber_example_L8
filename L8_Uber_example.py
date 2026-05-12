#
#
import streamlit as st
import pandas as pd
import numpy as np
import datetime



st.title("Uber Pickups in New York")

st.write("""
# My first app
Hello *world!*
""")


st.bar_chart(df, x="category", y="sales")


number = st.slider("Pick a number", 0, 100)

color = st.color_picker("Pick a color")


d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write("Your birthday is:", d)