# 🔐 SecureCheck Tool for Linux

<img width="813" height="695" alt="audit" src="https://github.com/user-attachments/assets/e1fcafb0-13ab-4e59-aeaf-7694c5965ff8" />


This project is a lightweight, extensible Linux security auditing tool that performs essential vulnerability checks and generates comprehensive Markdown reports. It leverages Bash scripts for efficient data gathering and Python scripts for parsing results and report generation.

Built to showcase skills in:

   - Shell scripting and automation

   - Python-based data processing and reporting

   - CI/CD pipeline integration and orchestration

   - Linux security hardening best practices


## 📋 Features

- ✅ Detects world-writable, SUID, and SGID files
- ✅ Audits SSH configuration and firewall status
- ✅ Checks sensitive files and UID 0 users
- ✅ Performs rootkit detection using `chkrootkit`
- ✅ Generates Markdown reports with summaries
- ✅ Provides a natural-language summary of findings
- ✅ Integrates with GitHub Actions for CI/CD automation
- ✅ Supports optional email delivery of reports


## 🧪 What Does It Check?

| Check                | Description                                                     |
| -------------------- | --------------------------------------------------------------- |
| World-writable files | Identifies files writable by any user                           |
| SUID files           | Detects binaries with SUID bit (potential escalation risks)     |
| SGID files           | Finds SGID files that may expose group-level access             |
| Rootkit scan         | Uses `chkrootkit` to detect signs of rootkits                   |
| SSH hardening        | Audits `sshd_config` for settings like `PermitRootLogin`        |
| Firewall status      | Checks firewall configuration and status to ensure proper rules |
| Sensitive files      | Verifies existence and permissions of critical sensitive files  |
| UID 0 users          | Lists all users with UID 0 (root privileges)                    |
| File permissions     | Audits key system files for secure permissions                  |

---

## 📁 Directory Structure

```

├── audit.sh                      # Main script that runs all modules and generates the report
├── modules/                     
│   ├── check_firewall.sh          # Checks the status and rules of the system firewall
│   ├── check_sensitive_files.sh   # Verifies existence and permissions of sensitive files
│   ├── check_uid0.sh              # Lists users with UID 0 (root privileges)
│   ├── file_permissions.sh        # Audits permissions of critical system files
│   ├── rootkit_scan.sh            # Performs rootkit scan using chkrootkit
│   └── ssh_config_audit.sh        # Audits SSH configuration for security best practices
├── README.md                     
├── report/                      
│   └── report.md                  # Markdown report generated after the audit
├── tmp/                         
└── tools/                      
    ├── generate_report.py         # Python script that compiles data and creates the final report
    └── vulnerabilities_summary.py # Generates a natural language summary of the findings


```

## 🔄 CI/CD Pipeline

The included GitHub Actions workflow:
- Runs the full audit on every push to the `main` branch
- Generates `report.md`
- Optionally emails the report via SMTP
- Uploads the report as a GitHub Actions artifact

To enable report emailing, configure these GitHub repository secrets:

| Secret Name      | Description                            |
|-------------------|----------------------------------------|
| `EMAIL_USERNAME` | Email address for sending reports      |
| `EMAIL_PASSWORD` | SMTP password or app-specific password |
| `EMAIL_TO`       | Recipient email address                |

## 🚀 Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/SecureAuditPlus.git
   cd SecureAuditPlus
   ```

2. **Make the audit script executable**:
   ```bash
   chmod +x audit.sh
   ```

3. **Run the full audit**:
   ```bash
   ./audit.sh
   ```

4. **View results**:
   - Detailed report: `report/report.md`
   - Summary: Printed to the terminal


## 💭 Final Thoughts

I created this project to improve my scripting skills in both Python and Bash. I wanted to apply my knowledge of Linux security hardening because I’ve always been concerned with system security.  

During development, I faced several challenges, especially debugging scripts to ensure the output was accurate and reliable. Troubleshooting permission issues and parsing complex system configurations required patience and iterative testing.  

Overall, this project helped me deepen my understanding of Linux security practices while sharpening my automation and scripting abilities.


## 📄 License

MIT License © 2025 Hugo Leonor
