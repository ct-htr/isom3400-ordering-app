import streamlit as st
from datetime import time
orderTime = st.slider("Order time", min_value = time(00, 00), max_value=time(23, 59), value = time(12, 00))

if orderTime < time(7, 00):
    st.error("McDonald's is not open yet!")
elif orderTime < time(11, 00):
    st.warning("Breakfast Menu")
else:
    st.info("Regular Menu")