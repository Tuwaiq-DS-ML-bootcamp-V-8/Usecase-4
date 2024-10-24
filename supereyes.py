import streamlit as st
import pandas as pd
import plotly.express as px

# Load your Toyota dataset
data = pd.read_csv('df_car_Toyota.csv')  # Adjust with your dataset path

# Title and Introduction
st.title("Toyota Car Finder Dashboard")
st.markdown("I understand the struggle of looking for a new car, so I did the heavy lifting for you.")
st.markdown("For starters, let's see what types we have from Toyota.")

# User Input for Car Type
car_types = data['Type'].unique()
selected_car = st.selectbox('What Type of Toyota are you interested in?', car_types)

# Filter based on the selected car type
filtered_data = data[data['Type'] == selected_car]

# Display the top 10 Toyota types
st.markdown("### 1. Top 10 Toyota Car Types")

# Count the occurrences of each car type
top_10_types = data['Type'].value_counts().head(10)
chart_data = pd.DataFrame({
    'Type': top_10_types.index,
    'Count': top_10_types.values
})

# Visualize with Plotly
fig1 = px.bar(chart_data, x='Type', y='Count', title='Top 10 Toyota Car Types')
st.plotly_chart(fig1)

# Display price ranges for the selected car type
st.markdown("### 2. Price Range for Selected Toyota Car Type")

# Creating bins for price ranges
price_bins = pd.cut(filtered_data['Price'], bins=10)  # Adjust bins as needed
price_range_counts = price_bins.value_counts().sort_index()

price_data = pd.DataFrame({
    'Price Range': price_range_counts.index.astype(str),
    'Count': price_range_counts.values
})

# Visualize price ranges with Plotly
fig2 = px.bar(price_data, x='Price Range', y='Count', title='Price Range for Selected Toyota Car Type')
st.plotly_chart(fig2)

# Display regions where the selected car type is available
st.markdown("### 3. Regions Where the Car is Available")

# Count the occurrences of each region
region_counts = filtered_data['Region'].value_counts()
region_data = pd.DataFrame({
    'Region': region_counts.index,
    'Count': region_counts.values
})

# Visualize regions with Plotly
fig3 = px.pie(region_data, names='Region', values='Count', title='Regions Where the Car is Available')
st.plotly_chart(fig3)