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


#st.bar_chart(df, x="category", y="sales")

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


def load_data(nrows):
        data=pd.read_csv(DATA_URL, nrows=nrows)
        lowercase=lambda x:str(x).lower()
        data.rename(lowercase, axis="columns", inplace=True)
        data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
        return data

number = st.slider("Pick a number", 0, 100)

color = st.color_picker("Pick a color")


d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write("Your birthday is:", d)