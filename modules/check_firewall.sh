echo "=== Firewall Status Check ==="

> tmp/firewall_status.txt

if command -v ufw >/dev/null 2>&1; then
    echo "UFW status:" >> tmp/firewall_status.txt
    sudo ufw status verbose >> tmp/firewall_status.txt
else
    echo "UFW not installed." >> tmp/firewall_status.txt
fi

if command -v firewall-cmd >/dev/null 2>&1; then
    echo "" >> tmp/firewall_status.txt
    echo "firewalld status:" >> tmp/firewall_status.txt
    sudo firewall-cmd --state >> tmp/firewall_status.txt 2>&1
else
    echo "firewalld not installed." >> tmp/firewall_status.txt
fi
