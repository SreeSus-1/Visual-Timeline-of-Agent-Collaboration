import streamlit as st
import json
import pandas as pd
import plotly.express as px
from orchestrator import run_agents

LOG_FILE = "logs/agent_logs.json"

st.title("AI Agent Collaboration Timeline")

topic = st.text_input("Enter Topic")

if st.button("Run Agents"):

    run_agents(topic)
    st.success("Agents completed!")

try:
    with open(LOG_FILE) as f:
        data = json.load(f)
except:
    data = []

if data:
    df = pd.DataFrame(data)

    st.subheader("Agent Timeline")

    fig = px.scatter(
        df,
        x="timestamp",
        y="agent",
        color="agent",
        hover_data=["topic"]
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Agent Outputs")

    for row in data[::-1]:
        with st.container():
            st.markdown(f"### {row['agent']}")
            st.write(f"**Topic:** {row['topic']}")
            st.write(f"**Time:** {row['timestamp']}")
            st.write(f"**Output:** {row['output']}")
            st.markdown("---")