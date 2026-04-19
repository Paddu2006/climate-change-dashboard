# Climate Change Dashboard — India
# By Padma Shree
# Project 14 of 25

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(
    page_title="India Climate Dashboard",
    page_icon="🌍",
    layout="wide"
)

# Title
st.title("🌍 India Climate Change Dashboard")
st.markdown("Tracking temperature anomalies, rainfall patterns and extreme weather across India")

# Generate realistic climate data
np.random.seed(42)
years = list(range(1990, 2024))

# Temperature data
temp_anomaly = [-0.2, -0.1, 0.0, 0.1, 0.2, 0.1, 0.3, 0.4, 0.3, 0.5,
                0.4, 0.6, 0.5, 0.7, 0.6, 0.8, 0.7, 0.9, 0.8, 1.0,
                0.9, 1.1, 1.0, 1.2, 1.1, 1.3, 1.2, 1.4, 1.3, 1.5,
                1.4, 1.6, 1.5, 1.7]

# Rainfall data
rainfall = [850, 820, 880, 790, 860, 810, 840, 870, 800, 890,
            830, 780, 860, 820, 790, 850, 810, 870, 800, 840,
            780, 860, 830, 790, 850, 810, 870, 800, 840, 780,
            860, 830, 790, 850]

# Extreme weather events
extreme_events = [2, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10,
                  9, 11, 10, 12, 11, 13, 12, 14, 13, 15, 14, 16, 15, 17,
                  16, 18, 17, 19]

df = pd.DataFrame({
    "Year": years,
    "Temperature_Anomaly": temp_anomaly,
    "Rainfall_mm": rainfall,
    "Extreme_Events": extreme_events
})

# Key metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Temperature Rise", "+1.7°C", "+0.2°C since 2020")
with col2:
    st.metric("Avg Rainfall", "832mm", "-18mm since 1990")
with col3:
    st.metric("Extreme Events 2023", "19", "+17 since 1990")
with col4:
    st.metric("Years Analysed", "34", "1990-2023")

st.divider()

# Chart 1 - Temperature anomaly
st.subheader("Temperature Anomaly Over Time")
fig1 = px.line(df, x="Year", y="Temperature_Anomaly",
               title="India Temperature Anomaly (1990-2023)",
               color_discrete_sequence=["red"])
fig1.add_hline(y=0, line_dash="dash", line_color="gray")
st.plotly_chart(fig1, use_container_width=True)

# Chart 2 - Rainfall trend
st.subheader("Annual Rainfall Trend")
fig2 = px.bar(df, x="Year", y="Rainfall_mm",
              title="Annual Rainfall in India (1990-2023)",
              color="Rainfall_mm",
              color_continuous_scale="Blues")
st.plotly_chart(fig2, use_container_width=True)

# Chart 3 - Extreme weather events
st.subheader("Extreme Weather Events")
fig3 = px.area(df, x="Year", y="Extreme_Events",
               title="Extreme Weather Events per Year (1990-2023)",
               color_discrete_sequence=["orange"])
st.plotly_chart(fig3, use_container_width=True)

# State wise temperature
st.subheader("State-wise Temperature Risk")
states_data = {
    "State": ["Rajasthan", "Gujarat", "Maharashtra", "Delhi", "Punjab",
              "Kerala", "Karnataka", "Tamil Nadu", "West Bengal", "Assam"],
    "Avg_Temp": [32, 30, 28, 29, 26, 28, 27, 30, 28, 25],
    "Risk": ["High", "High", "Medium", "High", "Medium",
             "Low", "Low", "Medium", "Medium", "Low"]
}
df_states = pd.DataFrame(states_data)
fig4 = px.bar(df_states, x="State", y="Avg_Temp", color="Risk",
              color_discrete_map={"High": "red", "Medium": "orange", "Low": "green"},
              title="Average Temperature by State")
st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")
st.markdown("Built by **Padma Shree** | Data Science Journey | Project 14 of 25")