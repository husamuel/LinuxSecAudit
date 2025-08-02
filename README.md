# 🔐 Linux Secure Tool

**Linux Secure Tool** is a lightweight, extensible Linux security auditing tool designed to assess critical security configurations and file permissions on Unix-based systems. Ideal for system administrators, DevOps engineers, and security-focused developers, it provides a quick and readable audit of core vulnerabilities.

## 📋 Features

- ✅ Detects world-writable files that pose security risks
- ✅ Enumerates SUID and SGID binaries for privilege escalation checks
- ✅ Audits SSH configuration for security best practices
- ✅ Performs rootkit detection using `chkrootkit`
- ✅ Generates detailed Markdown reports
- ✅ Provides a natural-language summary of findings
- ✅ Integrates with GitHub Actions for CI/CD automation
- ✅ Supports optional email delivery of reports

## 🧪 What Does It Check?

| Check                     | Description                                                  |
|---------------------------|--------------------------------------------------------------|
| World-writable files      | Identifies files writable by any user                        |
| SUID files                | Detects binaries with SUID bit (potential escalation risks)  |
| SGID files                | Finds SGID files that may expose group-level access          |
| Rootkit scan              | Uses `chkrootkit` to detect signs of rootkits                |
| SSH hardening             | Audits `sshd_config` for settings like `PermitRootLogin`     |

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

## 📁 Directory Structure

```
SecureAuditPlus/
├── modules/                   # Audit module scripts
│   ├── check_world_writable.sh
│   ├── check_suid.sh
│   ├── check_sgid.sh
│   ├── check_ssh_config.sh
│   └── run_chkrootkit.sh
├── tools/                     # Python scripts for processing and reporting
│   ├── permission_check.py
│   ├── generate_summary.py
│   └── report_generator.py
├── report/                    # Generated Markdown reports
├── tmp/                       # Temporary files during execution
├── audit.sh                   # Main script coordinating all modules
└── .github/workflows/         # GitHub Actions CI/CD configuration
```

## 🔄 CI/CD Pipeline

The included GitHub Actions workflow:
- Runs the full audit on every push to the `main` branch
- Generates `report.md`
- Optionally emails the report via SMTP
- Uploads the report as a GitHub Actions artifact

## 📧 Email Integration

To enable report emailing, configure these GitHub repository secrets:

| Secret Name      | Description                            |
|-------------------|----------------------------------------|
| `EMAIL_USERNAME` | Email address for sending reports      |
| `EMAIL_PASSWORD` | SMTP password or app-specific password |
| `EMAIL_TO`       | Recipient email address                |

## ⚠️ Disclaimers

- This tool is for auditing purposes only and does not automatically fix issues.
- Some findings (e.g., SUID/SGID binaries) may be legitimate depending on system configuration.
- Run with `sudo` for comprehensive results.

## 🛠️ Requirements

- Python 3.8+
- `chkrootkit` installed (e.g., via `apt`, `yum`)
- GitHub Actions (for CI/CD integration)

## 📄 License

MIT License © 2025 [Your Name or GitHub Handle]

## 🙋‍♂️ Why This Project?

SecureAuditPlus was developed as a technical exercise for a Linux Security Engineer position, showcasing:
- Shell scripting and automation
- Python-based parsing and reporting
- CI/CD pipeline orchestration
- Knowledge of Linux security hardening
