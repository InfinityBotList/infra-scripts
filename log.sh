# Ensure $1 is set
if [ -z "$1" ]; then
    echo "Usage: log <service>"
    exit 1
fi

journalctl -u $1 -n 300 -f
