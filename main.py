import streamlit as st
import functions as f



st.title("Uber pickups in NYC")

data_load_state = st.text("Loading data...")
data = f.load_data(1000)
data_load_state.text("Loading data... done! (using cache!)")

st.subheader("Raw data")
st.write(data)

