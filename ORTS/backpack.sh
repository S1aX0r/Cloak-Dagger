#!/bin/bash

cat << 'EOF'

 _                _                     _    
| |__   __ _  ___| | ___ __   __ _  ___| | __
| '_ \ / _` |/ __| |/ / '_ \ / _` |/ __| |/ /
| |_) | (_| | (__|   <| |_) | (_| | (__|   < 
|_.__/ \__,_|\___|_|\_\ .__/ \__,_|\___|_|\_\
                      |_|                    

EOF

echo "Enumerating tools of interest..."
echo

echo "OSINT TOOLS"
echo "----------------"

which nmap         
which spiderfoot
which rustcan
which masscan
which amass
which recon-ng
which fierce
which maltego
which dirb
which gobuster
which ffuf
which wfuzz
echo
echo "EXPLOITATION TOOLS"
echo "----------------"
which msfconsole
which commix
which sqlmap
which zaproxy
which burpsuite
echo
echo "SNIFFERS"
echo "----------------"
which tcpdump
which ettercap
which wireshark
which tshark
which scapy
which netsniff-ng
which dnsiff
echo
echo "TOOLS DUMPED, Enjoy ;)"