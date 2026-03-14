import streamlit as st
from agents.decision_engine import run_orchestrator
from agents.data_manager import DataManager

# 1. Page Configuration
st.set_page_config(page_title="Smallville S.V.6.0", layout="wide")
st.title("🛡️ Smallville S.V.6.0 C2 Dashboard")

# 2. Sidebar Navigation
st.sidebar.header("Operator Controls")
target = st.sidebar.text_input("Target IP/Domain", placeholder="192.168.1.1")
run_btn = st.sidebar.button("Execute Workflow")

# 3. Main Dashboard Logic
if run_btn and target:
    # Use a spinner to handle the delay during agent execution
    with st.spinner(f"Smallville agents are working on {target}..."):
        # The Orchestrator handles the sequential calls to recon/exploit modules
        results = run_orchestrator(target)
        
        # Display the results
        st.success("Workflow Complete.")
        st.json(results)
elif run_btn and not target:
    st.error("Please enter a target to initiate the Smallville workflow.")

# 4. View Historic Data
st.subheader("Mission Archive")
dm = DataManager()
# Display a list of processed reports
# (Logic to read from data/processed/ and list filenames as buttons)
st.write("Recent scan logs will appear here.")
