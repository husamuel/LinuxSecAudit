echo "=== Linux Security Audit ==="

mkdir -p tmp
mkdir -p report

# Executa os módulos bash silenciosamente
for module in modules/*.sh; do
    bash "$module"
done

# Executa a análise Python para permissões que gera os arquivos em tmp
python3 tools/permission_check.py

# Gera o resumo das vulnerabilidades
python3 tools/vulnerabilities_summary.py

# Gera o relatório markdown completo com o resumo incluído
python3 tools/generate_report.py

echo
echo "=== Summary of File Permissions Audit ==="

WW_COUNT=$(wc -l < tmp/world_writable_files.txt)
echo "[+] World-writable files count: $WW_COUNT"

SUID_COUNT=$(wc -l < tmp/suid_files.txt)
echo "[+] SUID files count: $SUID_COUNT"

SGID_COUNT=$(wc -l < tmp/sgid_files.txt)
echo "[+] SGID files count: $SGID_COUNT"

echo

if [ "$WW_COUNT" -eq 0 ] && [ "$SUID_COUNT" -eq 0 ] && [ "$SGID_COUNT" -eq 0 ]; then
    echo ">>> System appears secure regarding critical permissions."
else
    echo ">>> Warning: potentially insecure permissioned files found."
fi

echo
echo "Tests performed:"
echo "- World-writable files check"
echo "- SUID files check"
echo "- SGID files check"
