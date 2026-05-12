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
col1, col2 = st.columns([3, 1])
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


def load_data(nrows):
        data=pd.read_csv(DATA_URL, nrows=nrows)
        lowercase=lambda x:str(x).lower()
        data.rename(lowercase, axis="columns", inplace=True)
        data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
        return data

data_load_state=st.text("loading Data ...")
data=load_data(10000)
data_load_state.text("Loading data done")

col1.subheader("Raw Data")
col1.write(data)


col1.subheader("Num Pickups per hour")
hist_values=np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
col1.bar_chart(hist_values)




col2.subheader("map of pickups")
col2.map(data)


hour_to_filter=col2.slider("hour", 0,23,17)
filtered_data=data[data[DATE_COLUMN].dt.hour==hour_to_filter]
col2.subheader(f"Map of all Pickups at {hour_to_filter}:00")
col2.map(filtered_data)

number = st.slider("Pick a number", 0, 100)

color = st.color_picker("Pick a color")

