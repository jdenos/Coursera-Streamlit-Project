import datetime as dt

import pandas as pd
import pydeck as pdk
import streamlit as st
from plotly import graph_objs as go

import numpy as np

data_file = "./Motor_Vehicle_Collisions_-_Crashes.csv"

st.title = "Motor Vehicle Collisions in NYC"
st.markdown('''
# Motor Vehicle Collisions in NYC
## Context 
This dashboard was created for the guided project 
[Build a Data Science Web App with Streamlit and Python]
(https://www.coursera.org/projects/data-science-streamlit-python)
on coursera! 
## Goals
The purpose of this dashboard is to visualise vehicle collision 🚗 in New York City 🗽
''')


@st.cache(persist=True)
def get_data(nrows=None):
    data = pd.read_csv('https://data.cityofnewyork.us/resource/hhsa-x92p.csv', nrows=nrows,
                       parse_dates=[['CRASH DATE', 'CRASH TIME']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    data.rename(lambda x: str(x).lower(), axis='columns', inplace=True)
    data.rename(columns={'crash date_crash time': 'date_time'}, inplace=True)
    # data['time'] = data['date_time'].dt.time
    data.reset_index(inplace=True, drop=True)
    return data


df = get_data()

if st.checkbox('Raw Data', False):
    st.subheader('Raw Data')
    # st.write(df)
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[df[i] for i in df.columns],
                   fill_color='lavender',
                   align='left'))
    ])
    fig.update_layout(autosize=False,
                      width=10000,
                      height=500)
    st.plotly_chart(fig, use_container_width=False)

# Filters
st.sidebar.header("Filters")
injured_people = st.sidebar.slider("Number of people injured in the accident (or more)", 0,
                                   int(df['number of persons injured'].max()),
                                   value=2)
time = st.sidebar.slider("What time period do you want to check", min_value=dt.time(00, 00), max_value=dt.time(23, 59),
                         value=[dt.time(12, 00), dt.time(20, 00)], step=dt.timedelta(minutes=15))
date = st.sidebar.slider("which dates do you want to check", min_value=df['date_time'].dt.date.min(),
                         max_value=df['date_time'].dt.date.max(),
                         value=[df['date_time'].dt.date.min(), df['date_time'].dt.date.max()])

# Filtered data
df_filtred = df[
    (df['date_time'].dt.time >= time[0])
    & (df['date_time'].dt.time <= time[1])
    & (df['date_time'].dt.date >= date[0])
    & (df['date_time'].dt.date <= date[1])] \
    .query('`number of persons injured` >= @injured_people')

# 2D map
st.header('Location of accidents:')
st.map(df_filtred[['latitude', 'longitude']]
       .dropna(how='any'))
st.write(len(df))

# Deckgl map
st.header('3D map')
midpoint = (np.nanmean(df['latitude']), np.nanmean(df['longitude']))
st.write(
    pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state={
            'latitude': midpoint[0],
            "longitude": midpoint[1],
            "zoom": 11,
            "pitch": 50
        },
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=df_filtred[['date_time','latitude', 'longitude']],
                get_position=['longitude','latitude'],
                radius=100,
                extruded=True,
                pickable=True,
                elevation_scale=4,
                elevation_range=[0,1000]
            )
        ]
    )
)
