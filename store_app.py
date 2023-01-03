import streamlit as st
import pandas as pd
import numpy as np

st.title('Store Data')

data = pd.read_csv('supermarket.csv')

st.subheader('Top 5 Sellers')

data_top_5_sellers = data.sort_values('store_sales', ascending=False)

st.bar_chart(data_top_5_sellers.store_sales.head())

st.subheader('Top 5 Daily Customer Count')

data_top_5_daily_customer_count = data.sort_values('daily_customer_count', ascending=False)

st.bar_chart(data_top_5_daily_customer_count.daily_customer_count.head())

st.subheader('Top 5 by Sales Per customer')

data['spc'] = data.store_sales / data.daily_customer_count

data_top_5_sales_per_customer = data.sort_values('spc', ascending=False)

st.bar_chart(data_top_5_sales_per_customer.spc.head())