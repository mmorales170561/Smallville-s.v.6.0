import requests
from urllib.parse import urljoin

class WebAuditEngine:
    def __init__(self, target_url):
        self.target_url = target_url
        self.findings = []
        self.session = requests.Session()

    def check_security_headers(self):
        """Analyze HTTP headers for security gaps."""
        try:
            response = self.session.get(self.target_url, timeout=10)
            headers = response.headers
            
            # Example check: Content-Security-Policy
            if 'Content-Security-Policy' not in headers:
                self.findings.append({"type": "Security Header", "issue": "Missing CSP"})
        except Exception as e:
            self.findings.append({"type": "Error", "issue": str(e)})

    def check_directory_listing(self, paths=["/admin", "/config", "/backup"]):
        """Check for common sensitive directories."""
        for path in paths:
            url = urljoin(self.target_url, path)
            try:
                response = self.session.get(url, timeout=5)
                if response.status_code == 200:
                    self.findings.append({"type": "Sensitive Path", "issue": f"Path found: {url}"})
            except:
                continue

    def run_all(self):
        """Execute all audit checks."""
        self.check_security_headers()
        self.check_directory_listing()
        return self.findings

def run_web_scanner(target_url):
    """Wrapper function called by the Orchestrator."""
    engine = WebAuditEngine(target_url)
    return engine.run_all()
