import streamlit as st
import pandas as pd
import plotly.express as px

# Sample cost of living data for European cities vs. the U.S.
data = {
    "City": ["New York", "San Francisco", "Los Angeles", "Berlin", "Munich", "Frankfurt", "Paris", "London", "Madrid", "Amsterdam"],
    "Country": ["USA", "USA", "USA", "Germany", "Germany", "Germany", "France", "UK", "Spain", "Netherlands"],
    "Cost of Living Index": [100, 95, 85, 70, 72, 68, 80, 90, 65, 78],  # Relative to New York (100 as baseline)
    "Rent (USD)": [3500, 3200, 2800, 1800, 2000, 1700, 2500, 2900, 1500, 2700],
    "Groceries (USD)": [600, 550, 500, 400, 420, 390, 480, 530, 350, 470],
    "Transport (USD)": [150, 140, 130, 90, 100, 95, 120, 130, 85, 110]
}

# Convert data into a DataFrame
df = pd.DataFrame(data)

# Streamlit App Layout
st.title("🌍 Cost of Living Comparison: U.S. vs. Europe")
st.markdown("Compare major expense categories across major cities.")

# Show Data
st.dataframe(df)

# Create Bubble Chart for Cost of Living Comparison
st.subheader("📊 Cost of Living Index - Bubble Chart")
fig_bubble = px.scatter(df, x="City", y="Cost of Living Index",
                        size="Cost of Living Index", color="Country",
                        hover_name="City", size_max=60,
                        title="Cost of Living Comparison: U.S. vs. European Cities")
st.plotly_chart(fig_bubble)

# Create Treemap for Expense Breakdown by City
st.subheader("🏠 Rent Costs Across U.S. and European Cities")
fig_treemap = px.treemap(df, path=["Country", "City"], values="Rent (USD)",
                         title="Rent Costs Across U.S. and European Cities",
                         color="Rent (USD)", color_continuous_scale="Blues")
st.plotly_chart(fig_treemap)
