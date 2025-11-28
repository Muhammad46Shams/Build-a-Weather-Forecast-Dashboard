import streamlit as st
import plotly.express as px

st.title('Weather forcast for Next Days')
place = st.text_input('Place: ')
days = st.slider('Forcast Days', min_value=1, max_value=5, help='select the number of forcasted days')
option = st.selectbox('Select data to view',
                      ('Temperature', 'Sky'))

st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
	dates = ['2025-28-11', '2025-29-11', '2025-30-11']
	temperatures = [10, 11, 15]
	temperatures = [days * i for i in temperatures]
	return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperature (C)"})
st.plotly_chart(figure)
