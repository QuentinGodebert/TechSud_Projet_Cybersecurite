print("=== Audit TechSud ===")
import subprocess, json, csv, socket
from datetime import datetime
from pathlib import Path
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return {
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
        "returncode": result.returncode
    }
def get_hostname():
    return socket.gethostname()

    
def get_ssh_status():
    result = run_command("systemctl is-active ssh")
    if result["returncode"] == 0:
        return result["stdout"]
    return "inconnu"