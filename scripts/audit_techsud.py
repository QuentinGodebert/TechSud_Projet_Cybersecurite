# subprocess = commandes système | export JSON/CSV | socket = infos réseau
import subprocess, json, csv, socket

from datetime import datetime
from pathlib import Path


# Exécute une commande système et récupère le résultat
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return {
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
        "returncode": result.returncode,
    }


# Récupère le nom de la machine
def get_hostname():
    return socket.gethostname()


# Vérifie si SSH est actif
def get_ssh_status():
    result = run_command("systemctl is-active ssh")
    if result["returncode"] == 0:
        return result["stdout"]
    return "inconnu"


# Vérifie si fail2ban est actif
def get_fail2ban_status():
    result = run_command("systemctl is-active fail2ban")
    if result["returncode"] == 0:
        return result["stdout"]
    return "inconnu"


# Vérifie si fail2ban est actif pour le service sshd
def get_fail2ban_sshd_status():
    result = run_command("fail2ban-client status sshd")
    return result["returncode"] == 0


# Vérifie si fail2ban est installé
def get_fail2ban_installed():
    result = run_command("dpkg -l | grep fail2ban")
    return result["returncode"] == 0 and result["stdout"] != ""


# Vérifie si UFW est actif
def get_ufw_status():
    result = run_command("ufw status")
    if "Status: active" in result["stdout"]:
        return "actif"
    return "inactif"


# Lit la configuration SSH
def get_ssh_config():
    port = "22"
    root_login = "inconnu"
    password_authentication = "inconnu"

    try:
        with open("/etc/ssh/sshd_config", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                if line.startswith("Port "):
                    port = line.split()[1]

                if line.startswith("PermitRootLogin "):
                    root_login = line.split()[1]

                if line.startswith("PasswordAuthentication "):
                    password_authentication = line.split()[1]

    except:
        pass

    return {
        "port": port,
        "root_login": root_login,
        "password_authentication": password_authentication,
    }


# Récupère la liste des ports ouverts
def get_open_ports():
    result = run_command("ss -tuln")
    ports = []

    for line in result["stdout"].splitlines():
        line = line.strip()

        if not line or line.startswith("Netid"):
            continue

        parts = line.split()

        if len(parts) >= 5:
            local_address = parts[4]

            if ":" in local_address:
                port = local_address.rsplit(":", 1)[-1]

                if port.isdigit() and port not in ports:
                    ports.append(port)

    return sorted(ports, key=int)


# Récupère la liste des services actifs
def get_active_services():
    result = run_command(
        "systemctl list-units --type=service --state=running --no-pager --no-legend"
    )
    services = []

    for line in result["stdout"].splitlines():
        line = line.strip()

        if not line:
            continue

        services.append(line.split()[0])

    return services


# Récupère les utilisateurs ayant un shell interactif
def get_shell_users():
    users = []

    try:
        with open("/etc/passwd", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(":")

                if len(parts) >= 7:
                    username = parts[0]
                    shell = parts[-1]

                    if shell.endswith("/bash") or shell.endswith("/sh"):
                        users.append(username)

    except:
        pass

    return users


# Vérifie quelques points simples de conformité
def build_compliance(
    ssh_status,
    ssh_config,
    ufw_status,
    fail2ban_installed,
    fail2ban_status,
    fail2ban_sshd_active,
    open_ports,
):
    ssh_port = ssh_config["port"]

    return {
        "ssh_active": ssh_status == "active",
        "ssh_custom_port": ssh_port != "22",
        "ssh_port_listening": ssh_port in open_ports,
        "root_login_disabled": ssh_config["root_login"].lower() == "no",
        "ufw_active": ufw_status == "actif",
        "fail2ban_installed": fail2ban_installed,
        "fail2ban_active": fail2ban_status == "active",
        "fail2ban_sshd_active": fail2ban_sshd_active,
        "password_auth_disabled": ssh_config["password_authentication"].lower() == "no",
    }


# Construit le rapport complet
def build_report():
    hostname = get_hostname()
    ssh_status = get_ssh_status()
    ssh_config = get_ssh_config()
    ufw_status = get_ufw_status()
    fail2ban_installed = get_fail2ban_installed()
    fail2ban_status = get_fail2ban_status()
    fail2ban_sshd_active = get_fail2ban_sshd_status()
    open_ports = get_open_ports()
    active_services = get_active_services()
    shell_users = get_shell_users()

    compliance = build_compliance(
        ssh_status,
        ssh_config,
        ufw_status,
        fail2ban_installed,
        fail2ban_status,
        fail2ban_sshd_active,
        open_ports,
    )

    compliance_ok = sum(1 for value in compliance.values() if value)
    compliance_total = len(compliance)

    return {
        "audit_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hostname": hostname,
        "ssh": {
            "service_status": ssh_status,
            "configured_port": ssh_config["port"],
            "permit_root_login": ssh_config["root_login"],
            "password_authentication": ssh_config["password_authentication"],
        },
        "security_tools": {
            "ufw_status": ufw_status,
            "fail2ban_installed": fail2ban_installed,
            "fail2ban_status": fail2ban_status,
        },
        "system": {
            "open_ports": open_ports,
            "active_services": active_services,
            "interactive_shell_users": shell_users,
        },
        "compliance": compliance,
        "summary": {
            "validated_checks": compliance_ok,
            "total_checks": compliance_total,
        },
    }


# Affiche un résumé lisible dans le terminal
def print_summary(report):
    print("=== Audit TechSud ===\n")
    print("Date :", report["audit_date"])
    print("Machine :", report["hostname"])

    print("\n--- SSH ---")
    print("Statut :", report["ssh"]["service_status"])
    print("Port configuré :", report["ssh"]["configured_port"])
    print("PermitRootLogin :", report["ssh"]["permit_root_login"])
    print("PasswordAuthentication :", report["ssh"]["password_authentication"])

    print("\n--- Outils de sécurité ---")
    print("UFW :", report["security_tools"]["ufw_status"])
    print("fail2ban installé :", report["security_tools"]["fail2ban_installed"])
    print("fail2ban statut :", report["security_tools"]["fail2ban_status"])

    print("\n--- Ports ouverts ---")
    if report["system"]["open_ports"]:
        print(", ".join(report["system"]["open_ports"]))
    else:
        print("Aucun")

    print("\n--- Services actifs ---")
    if report["system"]["active_services"]:
        for service in report["system"]["active_services"]:
            print("-", service)
    else:
        print("Aucun")

    print("\n--- Utilisateurs avec shell interactif ---")
    if report["system"]["interactive_shell_users"]:
        print(", ".join(report["system"]["interactive_shell_users"]))
    else:
        print("Aucun")

    print("\n--- Contrôles de conformité ---")
    for key, value in report["compliance"].items():
        print(f"{key} :", "OK" if value else "NON CONFORME")

    print(
        f"\nRésumé : {report['summary']['validated_checks']} / "
        f"{report['summary']['total_checks']} contrôles validés"
    )


# Exporte le rapport en JSON
def export_json(report, output_dir):
    output_path = output_dir / "audit_result.json"

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)


# Exporte le rapport en CSV
def export_csv(report, output_dir):
    output_path = output_dir / "audit_result.csv"

    rows = [
        ["audit_date", report["audit_date"]],
        ["hostname", report["hostname"]],
        ["ssh_service_status", report["ssh"]["service_status"]],
        ["ssh_configured_port", report["ssh"]["configured_port"]],
        ["ssh_permit_root_login", report["ssh"]["permit_root_login"]],
        ["ufw_status", report["security_tools"]["ufw_status"]],
        ["fail2ban_installed", report["security_tools"]["fail2ban_installed"]],
        ["fail2ban_status", report["security_tools"]["fail2ban_status"]],
        ["open_ports", ", ".join(report["system"]["open_ports"])],
        ["active_services", ", ".join(report["system"]["active_services"])],
        [
            "interactive_shell_users",
            ", ".join(report["system"]["interactive_shell_users"]),
        ],
        ["validated_checks", report["summary"]["validated_checks"]],
        ["total_checks", report["summary"]["total_checks"]],
    ]

    for key, value in report["compliance"].items():
        rows.append([f"compliance_{key}", value])

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["key", "value"])
        writer.writerows(rows)


# Fonction principale
def main():
    base_dir = Path(__file__).resolve().parent
    output_dir = base_dir / "results"
    output_dir.mkdir(exist_ok=True)

    report = build_report()
    print_summary(report)
    export_json(report, output_dir)
    export_csv(report, output_dir)


# Lance le script
if __name__ == "__main__":
    main()
    # python3 script/audit_techsud.py
