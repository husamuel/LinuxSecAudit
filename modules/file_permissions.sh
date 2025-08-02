DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$DIR")"

echo "=== File Permissions Audit ==="

echo "[+] World-writable files:"
find / -type f -perm -002 -exec ls -l {} \; 2>/dev/null > "$PROJECT_DIR/tmp/world_writable_files.txt"

echo "[+] SUID files:"
find / -perm -4000 -type f 2>/dev/null > "$PROJECT_DIR/tmp/suid_files.txt"

echo "[+] SGID files:"
find / -perm -2000 -type f 2>/dev/null > "$PROJECT_DIR/tmp/sgid_files.txt"
