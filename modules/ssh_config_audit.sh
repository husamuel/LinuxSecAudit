SSHD_CONF="/etc/ssh/sshd_config"

if [ ! -f "$SSHD_CONF" ]; then
    echo "SSH config file not found at $SSHD_CONF" > tmp/ssh_config.txt
    exit 1
fi

grep -E '^(PermitRootLogin|PasswordAuthentication|X11Forwarding|AllowTcpForwarding)' "$SSHD_CONF" > tmp/ssh_config.txt

{
    echo ""
    echo "[*] Recommended settings:"
    echo "PermitRootLogin no"
    echo "PasswordAuthentication no"
    echo "X11Forwarding no"
    echo "AllowTcpForwarding no"
} >> tmp/ssh_config.txt
