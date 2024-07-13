import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv("Fuel_Resource Capacity.csv")
st.title("Installed Capacity by Fuel/Resource in Bangladesh")

# Plot pie chart using Plotly
fig = px.pie(df, names='Fuel/Resource', values='Installed Capacity', title='Installed Capacity by Fuel/Resource')

# Display the chart
st.plotly_chart(fig)

# Display the DataFrame
st.write(df)