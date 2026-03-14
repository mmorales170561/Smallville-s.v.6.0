
import nmap
import json

def run_nmap(target):
    """
    Performs a standard port scan and returns structured data.
    """
    scanner = nmap.PortScanner()
    print(f"[*] Scanning {target}...")
    
    # Run a basic TCP connect scan on common ports
    # Arguments: -sV for version detection, -T4 for speed
    scanner.scan(target, '22,80,443,3389', arguments='-sV -T4')
    
    # Check if target responded
    if target not in scanner.all_hosts():
        return {"error": "Host down or unreachable"}
    
    results = {
        "target": target,
        "status": scanner[target].state(),
        "open_ports": []
    }
    
    # Parse open ports and services
    for proto in scanner[target].all_protocols():
        ports = scanner[target][proto].keys()
        for port in ports:
            port_info = scanner[target][proto][port]
            results["open_ports"].append({
                "port": port,
                "state": port_info['state'],
                "name": port_info['name'],
                "product": port_info.get('product', 'unknown')
            })
            
    return results

# Example of how the Decision Engine will use this:
# recon_data = run_nmap("127.0.0.1")
# print(json.dumps(recon_data, indent=2))
