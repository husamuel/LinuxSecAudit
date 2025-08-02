# 🔐 SecureAudit

**SecureAudit** is a lightweight and extensible Linux security auditing tool designed to help assess key security configurations and file permissions on Unix-based systems.

It is ideal for system administrators, DevOps engineers, or security-focused developers who want a quick and readable audit of core vulnerabilities.

---

## 📋 Features

- ✅ **World-writable files detection**
- ✅ **SUID and SGID binary enumeration**
- ✅ **SSH configuration security audit**
- ✅ **Rootkit detection using `chkrootkit`**
- ✅ **Markdown report generation**
- ✅ **Summary of findings in natural language**
- ✅ **CI/CD integration with GitHub Actions**
- ✅ **Optional email delivery of report**

---

## 🧪 What Does It Check?

The tool performs the following checks:

| Check                            | Description                                                  |
|----------------------------------|--------------------------------------------------------------|
| World-writable files             | Detects files that can be written by any user               |
| SUID files                       | Finds binaries with the SUID bit (privilege escalation risk)|
| SGID files                       | Identifies SGID files that may expose group-level access     |
| Rootkit scan                     | Runs `chkrootkit` to detect signs of rootkits                |
| SSH hardening                    | Audits key sshd_config parameters like `PermitRootLogin`     |

---

# LinuxSecAudit
