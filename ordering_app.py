import streamlit as st
import pandas as pd
from datetime import time

df = pd.read_csv("menu_items.csv")

#st.write(df)


orderTime = st.slider("Order time", min_value = time(00, 00), max_value=time(23, 59), value = time(12, 00))
priceRange = st.slider("Budget", value = (0, 60), max_value = 60)

filtered_df = df[(df['alacarte'] >= priceRange[0]) & (df['alacarte'] <= priceRange[1])]

st.write(filtered_df)

if orderTime < time(7, 00):
    st.error("McDonald's is not open yet!")
elif orderTime < time(11, 00):
    st.warning("Serving Breakfast Menu")
    # st.write(df[(filtered_df['time'] == 'Breakfast')])
else:
    st.info("Serving Regular Menu")
    # st.write(df[(filtered_df['time'] == 'Regular')])

