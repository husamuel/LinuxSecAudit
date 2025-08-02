echo "=== Sensitive Files Permission Check ==="

FILES=(
    "/etc/shadow"
    "/etc/sudoers"
    "/etc/passwd"
)

> tmp/sensitive_files_permissions.txt

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        ls -l "$file" >> tmp/sensitive_files_permissions.txt
    else
        echo "$file not found." >> tmp/sensitive_files_permissions.txt
    fi
done
