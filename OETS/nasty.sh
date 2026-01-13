#!/bin/bash

cat << "EOF"

                     __       
   ____  ____ ______/ /___  __
  / __ \/ __ `/ ___/ __/ / / /
 / / / / /_/ (__  ) /_/ /_/ / 
/_/ /_/\__,_/____/\__/\__, /  
                     /____/   
                            

EOF


show_help() {
    echo "Usage: ./nasty.sh [options]"
    echo "Options:"
    echo "  -t, --target    Target IP or hostname"
    echo "  -p, --ports     Comma-separated list of ports to scan (default: 22,80,443)"
    echo "  -h, --help      Show this help message"
}

TARGET=""
PORTS="22,80,443,445,21,5985,3389"
SWEEP=false

while [[ "$#" -gt 0 ]]; do
    case $1 in
        -t|--target) TARGET="$2"; shift ;;
        -p|--ports)  PORTS="$2"; shift ;;
        -h|--help)   show_help; exit 0 ;;
        *)           echo "Unknown parameter: $1"; show_help; exit 1 ;;
    esac
    shift
done

if [[ -z "$TARGET" ]]; then
    echo "Error: Target is required."
    show_help
    exit 1
fi

echo "[*] Scan started on target: $TARGET"

check_ports() {
    IFS=',' read -ra ADDR <<< "$PORTS"
    echo "[*] Scanning ports: ${PORTS}"
    for port in "${ADDR[@]}"; do
        {
            (echo > /dev/tcp/$TARGET/$port) >/dev/null 2>&1 && echo "Port $port is open" || echo "Port $port is closed"
        } &
    done
    wait
}

check_ports

echo "[*] Scan complete."
