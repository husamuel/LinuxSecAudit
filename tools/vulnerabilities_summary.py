import os

def read_file(filepath):
    if not os.path.exists(filepath):
        return ""
    with open(filepath, "r") as f:
        return f.read()

def count_lines(filepath):
    if not os.path.exists(filepath):
        return 0
    with open(filepath, "r") as f:
        return sum(1 for _ in f)

def generate_summary():
    ww_count = count_lines("tmp/world_writable_files.txt")
    suid_count = count_lines("tmp/suid_files.txt")
    sgid_count = count_lines("tmp/sgid_files.txt")
    rootkit_report = read_file("tmp/rootkit_scan.txt")
    ssh_config_report = read_file("tmp/ssh_config.txt")
    uid0_users_report = read_file("tmp/uid0_users.txt")
    sensitive_files_report = read_file("tmp/sensitive_files_permissions.txt")
    firewall_status = read_file("tmp/firewall_status.txt")

    summary = []

    # World-writable files
    summary.append(
        f"- ⚠️ World-writable files found: {ww_count}"
        if ww_count > 0 else "- ✅ No world-writable files found"
    )

    # SUID files
    summary.append(
        f"- ⚠️ SUID files found: {suid_count}"
        if suid_count > 0 else "- ✅ No SUID files found"
    )

    # SGID files
    summary.append(
        f"- ⚠️ SGID files found: {sgid_count}"
        if sgid_count > 0 else "- ✅ No SGID files found"
    )

    # Rootkit detection
    summary.append(
        "- ⚠️ Rootkit scan indicates potential infections!"
        if "INFECTED" in rootkit_report.upper()
        else "- ✅ Rootkit scan found no issues"
    )

    # SSH Configuration
    insecure_ssh_settings = any(
        line.startswith(param) and "no" not in line.lower()
        for param in ["PermitRootLogin", "PasswordAuthentication", "X11Forwarding", "AllowTcpForwarding"]
        for line in ssh_config_report.splitlines()
    )
    summary.append(
        "- ⚠️ SSH config has potentially insecure settings"
        if insecure_ssh_settings else "- ✅ SSH config settings are secure"
    )

    # UID 0 users
    uid0_count = len([line for line in uid0_users_report.splitlines() if line.strip()])
    summary.append(
        f"- ⚠️ {uid0_count} user(s) with UID 0 found (should be only root)"
        if uid0_count > 1 else "- ✅ Only root user has UID 0"
    )

    # Sensitive files permissions
    if "INSECURE" in sensitive_files_report.upper():
        summary.append("- ⚠️ Sensitive file permissions may be insecure")
    else:
        summary.append("- ✅ Sensitive file permissions are correct")

    # Firewall status
    if "inactive" in firewall_status.lower():
        summary.append("- ⚠️ Firewall (ufw) is inactive")
    else:
        summary.append("- ✅ Firewall is active")

    return "\n".join(summary)

def save_summary():
    summary_text = generate_summary()
    with open("tmp/vulnerabilities_summary.txt", "w") as f:
        f.write(summary_text)

if __name__ == "__main__":
    save_summary()
    print("[*] Vulnerabilities summary saved to tmp/vulnerabilities_summary.txt")
