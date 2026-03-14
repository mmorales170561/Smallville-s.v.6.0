
# app.py
from agents import run_nmap, run_orchestrator

# Now your UI code is clean and focused on the dashboard
target = "127.0.0.1"
results = run_nmap(target)
run_orchestrator(results)
