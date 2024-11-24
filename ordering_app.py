import streamlit as st
import pandas as pd
from datetime import time
import time as sleepTime

st.title("🍟HKUST McDonald's Decision Maker")

df = pd.read_csv("menu_items.csv")
orderedMeals = []

orderTime = st.slider("Order time", min_value = time(7, 00), max_value=time(23, 59), value = time(12, 00))
priceRange = st.slider("Budget", value = (0, 60), max_value = 60)

df = df[(df['meal'] >= priceRange[0]) & (df['meal'] <= priceRange[1])]


currentMenu = 0

if orderTime < time(11, 00):
    st.warning("Serving Breakfast Menu")
    currentMenu = df[(df['ordtime'] == 'Breakfast')]
else:
    st.info("Serving Regular Menu")
    currentMenu = df[(df['ordtime'] == 'Regular')]

st.dataframe(currentMenu[['menuitem','meal']], height=35*(currentMenu['menuitem'].shape[0]+1) + 3)

# Forum thread on optimal df height: https://discuss.streamlit.io/t/st-dataframe-controlling-the-height-threshold-for-scolling/31769/5


with st.container(border=True):
    st.write("Please choose:")
    addToCart = st.multiselect("Select Product", currentMenu['menuitem'])
    if addToCart:
        myItem = addToCart[0]

    prices = [currentMenu[currentMenu.menuitem==fooditem].meal.item() for fooditem in addToCart]
    st.write(f"##### Total Price: ${sum(prices)}")
    orderButton = st.button("Place order")

if orderButton:
    st.write("#### Ordered meals:")
    for meal in addToCart:
        st.write(meal)

