echo "=== Rootkit Scan ==="

if ! command -v chkrootkit &> /dev/null; then
    echo "chkrootkit not installed. Please install it to run rootkit scan."
    exit 1
fi

chkrootkit > tmp/rootkit_scan.txt 2>&1
