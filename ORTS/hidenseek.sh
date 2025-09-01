#!/bin/bash

cat << "EOF"

 _     _     _       ___                  _
| |__ (_) __| | ___ ( _ )   ___  ___  ___| | __
| '_ \| |/ _` |/ _ \/ _ \/\/ __|/ _ \/ _ \ |/ /
| | | | | (_| |  __/ (_>  <\__ \  __/  __/   <
|_| |_|_|\__,_|\___|\___/\/|___/\___|\___|_|\_\

EOF

echo "Enumerating Hosts"
echo

hosts_files=($(find / -type f -name "hosts" 2>/dev/null))

for file in "${hosts_files[@]}"; do
    echo "Contents of $file:"
    cat "$file"
    echo
done

echo "Would you like to port scan IPs found in /etc/hosts? (Y/N): "

read answer

if [[ "$answer" == "Y" || "$answer" == "y" ]]; then
    for file in "${hosts_files[@]}"; do
        echo "Scanning IPs found in $file..."
        awk '/^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/ {print $1}' "$file" | xargs -r nmap
    done
else
    echo "Moving on..."
fi
