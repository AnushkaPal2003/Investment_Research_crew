import os

import requests
import streamlit as st

API_URL = os.environ.get("API_URL", "http://localhost:8000")

st.set_page_config(page_title="Investment Research Crew", page_icon="📊")
st.title("📊 Investment Research Crew")
st.caption("Multi-agent company due-diligence brief, powered by CrewAI")

company = st.text_input("Company name", placeholder="e.g. Zomato")

if st.button("Run research", type="primary") and company:
    with st.spinner("Agents are researching, analyzing, and reviewing..."):
        response = requests.post(
    f"{API_URL}/research",
    json={"company": company},
    timeout=300,
)

    

    if response.status_code == 200:
        report = response.json()["report"]
        st.markdown(report)
    else:
        st.error("Backend failed")