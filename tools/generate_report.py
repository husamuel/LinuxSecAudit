import os

def read_file(filepath):
    if not os.path.exists(filepath):
        return "File not found."
    with open(filepath, "r") as f:
        return f.read()

def generate_markdown_report():
    md_content = "# SecureAuditPlus Report\n\n"

    # Incluir resumo das vulnerabilidades no topo (gerado pelo outro script)
    summary = read_file("tmp/vulnerabilities_summary.txt")
    md_content += "## Vulnerability Summary\n\n"
    md_content += summary + "\n\n"

    # Todas as seções que devem ser incluídas no relatório
    sections = {
        "World-writable Files": "tmp/world_writable_files.txt",
        "SUID Files": "tmp/suid_files.txt",
        "SGID Files": "tmp/sgid_files.txt",
        "Rootkit Scan": "tmp/rootkit_scan.txt",
        "SSH Config Audit": "tmp/ssh_config.txt",
        "UID 0 Users Check": "tmp/uid0_users.txt",
        "Sensitive Files Permissions": "tmp/sensitive_files_permissions.txt",
        "Firewall Status": "tmp/firewall_status.txt"
    }

    for title, path in sections.items():
        md_content += f"## {title}\n\n"
        md_content += "```\n"
        md_content += read_file(path)
        md_content += "\n```\n\n"

    # Salvar o relatório final
    with open("report/report.md", "w") as f:
        f.write(md_content)

def main():
    generate_markdown_report()
    print("[*] Markdown report generated at report/report.md")

if __name__ == "__main__":
    main()
