import streamlit as st
import plotly.express as px
form backend import get_data


st.title('Weather forcast for Next Days')
place = st.text_input('Place: ')
days = st.slider('Forcast Days', min_value=1, max_value=5, help='select the number of forcasted days')
option = st.selectbox('Select data to view',
                      ('Temperature', 'Sky'))

st.subheader(f"{option} for the next {days} days in {place}")

d, t = get_data(place, days, option)

figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperature (C)"})
st.plotly_chart(figure)
