import streamlit as st
import valkey
import pandas as pd
import plotly.express as px

r = valkey.Valkey(host='localhost', port=6379, decode_responses=True)

st.title("📊 Global Reserve Composition (1999-2021)")

years = [str(y) for y in range(1999, 2022, 2)] # Get data points we have

# Construct the data frame
data = []
for y in years:
    big4 = float(r.get(f"big4:{y}") or 0)
    non = float(r.get(f"non:{y}") or 0)
    data.append([y, big4, non])

df = pd.DataFrame(data, columns=['Year', 'Big Four (%)', 'Nontraditional (%)'])

# Dual-axis visualization logic
fig = px.line(df, x='Year', y=['Big Four (%)', 'Nontraditional (%)'],
              title='Big Four vs. Nontraditional Reserve Shares',
              markers=True, template="plotly_dark")

st.plotly_chart(fig, use_container_width=True)
st.dataframe(df)