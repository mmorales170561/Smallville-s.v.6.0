
import json
import os
from .recon import run_nmap
from .web_audit import run_web_scanner
from .exploit import run_exploit_module

def run_orchestrator(target):
    """
    The central intelligence unit for Smallville S.V.6.0.
    Evaluates scan results and dispatches tasks to specific agents.
    """
    print(f"[*] Starting Intelligence Routine for target: {target}")
    
    # 1. Primary Recon Stage
    nmap_data = run_nmap(target)
    
    # 2. Logic Gate (The deterministic decision process)
    tasks = []
    
    # Analyze ports found in nmap_data
    if "80/tcp" in nmap_data or "443/tcp" in nmap_data:
        tasks.append("web_audit")
    
    if "22/tcp" in nmap_data:
        tasks.append("ssh_enumeration")
        
    # 3. Execution Phase
    for task in tasks:
        if task == "web_audit":
            print("[+] Routing to Web Audit Agent...")
            run_web_scanner(target)
        elif task == "ssh_enumeration":
            print("[+] Routing to SSH Enumeration Agent...")
            # run_ssh_agent(target)
            
    return {"status": "Complete", "dispatched_tasks": tasks}

# Helper to save results to disk for the UI to read
def save_findings(data):
    with open("data/results.json", "w") as f:
        json.dump(data, f, indent=4)
