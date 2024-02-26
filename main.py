import streamlit as st
import functions as f
import numpy as np



st.title("Uber pickups in NYC")

data_load_state = st.text("Loading data...")
data = f.load_data(1000)
data_load_state.text("Loading data... done! (using cache!)")

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data)

st.subheader("Number of pickups by hour")
hist_values = np.histogram(data[f.date_column].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
col1, col2 = st.columns(2)
st.subheader("Pickups map")

with col1:
    st.write("This map shows all pickup locations. You can filter by hour in the other map. Use the slider and watch the map update in real time.")
    st.map(data)

with col2:
    hour_to_filter = st.slider("hour", 0, 23, 11)
    filtered_data = data[data[f.date_column].dt.hour == hour_to_filter]
    # st.subheader(f'Map of all pickups at {hour_to_filter}:00')
    st.map(filtered_data)