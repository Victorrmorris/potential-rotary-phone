import streamlit as st
import pandas as pd
import plotly.express as px

# ---- 🎨 Streamlit Page Configuration ----
st.set_page_config(page_title="Cost of Living Comparison", layout="wide")

# ---- 📊 Sample Cost of Living Data ----
data = {
    "City": ["New York", "San Francisco", "Los Angeles", "Berlin", "Munich", "Frankfurt", "Paris", "London", "Madrid", "Amsterdam"],
    "Country": ["USA", "USA", "USA", "Germany", "Germany", "Germany", "France", "UK", "Spain", "Netherlands"],
    "Cost of Living Index": [100, 95, 85, 70, 72, 68, 80, 90, 65, 78],  # Relative to New York (100 as baseline)
    "Rent (USD)": [3500, 3200, 2800, 1800, 2000, 1700, 2500, 2900, 1500, 2700],
    "Groceries (USD)": [600, 550, 500, 400, 420, 390, 480, 530, 350, 470],
    "Transport (USD)": [150, 140, 130, 90, 100, 95, 120, 130, 85, 110],
    "Total Monthly Cost (USD)": [4250, 3890, 3430, 2190, 2520, 2185, 3100, 3560, 1935, 3280]
}

df = pd.DataFrame(data)

# ---- 🎯 Sidebar: Filter by Region ----
st.sidebar.header("🔍 Filter Cities by Country")
selected_countries = st.sidebar.multiselect("Select Countries:", df["Country"].unique(), default=df["Country"].unique())
filtered_df = df[df["Country"].isin(selected_countries)]

# ---- 🏠 Main Section: Introduction ----
st.title("🌍 Cost of Living Comparison: U.S. vs. Europe")
st.markdown("""
💡 **Compare major expense categories across cities to make informed decisions.**  
🔹 **Bubble Chart:** Highlights the Cost of Living Index per city.  
🔹 **Treemap:** Breaks down Rent Costs across regions.
""")

# ---- 📊 Bubble Chart: Cost of Living Index ----
st.subheader("📈 Cost of Living Index by City")
fig_bubble = px.scatter(filtered_df, x="City", y="Cost of Living Index",
                        size="Total Monthly Cost (USD)", color="Country",
                        hover_name="City", size_max=60,
                        title="Cost of Living Index: U.S. vs. European Cities",
                        labels={"Cost of Living Index": "Cost Index (New York = 100)"})

st.plotly_chart(fig_bubble, use_container_width=True)

# ---- 🏠 Treemap: Rent Costs ----
st.subheader("🏡 Rent Costs Across Cities")
fig_treemap = px.treemap(filtered_df, path=["Country", "City"], values="Rent (USD)",
                         title="Rent Costs by Country & City",
                         color="Rent (USD)", color_continuous_scale="Blues")

st.plotly_chart(fig_treemap, use_container_width=True)

# ---- 📋 Show Data Table ----
st.subheader("📊 Detailed Cost Breakdown")
st.dataframe(filtered_df.style.format({"Rent (USD)": "${:,.0f}", "Groceries (USD)": "${:,.0f}", "Transport (USD)": "${:,.0f}", "Total Monthly Cost (USD)": "${:,.0f}"}))

# ---- ℹ️ Explanation Section ----
st.markdown("""
### 🔎 **How to Use This Dashboard**
- Use the **sidebar** to filter by **country**.
- Hover over **bubbles** to compare **cost of living levels**.
- Use the **Treemap** to see **rent prices by region**.
- View the **detailed table** for precise cost breakdowns.
""")
