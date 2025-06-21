import streamlit as st

st.set_page_config(page_title="Investment Dashboard", layout="wide")

st.title("📈 AI Investment Dashboard")
st.write("Welcome to your mobile-friendly stock tracking app!")

col1, col2, col3 = st.columns(3)
col1.metric("Top Stock", "AAPL", "+3.25%")
col2.metric("Portfolio Value", "$15,230", "+1.1%")
col3.metric("AI Signal Score", "82 / 100")
