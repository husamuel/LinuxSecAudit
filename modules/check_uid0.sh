echo "=== UID 0 Users Check ==="

awk -F: '($3 == 0) {print $1}' /etc/passwd > tmp/uid0_users.txt

if [ -s tmp/uid0_users.txt ]; then
    echo "Users with UID 0 found:" >> tmp/uid0_users.txt
else
    echo "No users with UID 0 found besides root." > tmp/uid0_users.txt
fi
