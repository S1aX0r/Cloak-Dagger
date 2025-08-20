#!/bin/bash

logo='
BBBB    A    SSSS  H   H W   W  RRRR    A   PPPP
B   B  A A   S     H   H W   W  R   R  A A  P   P
BBBB  AAAAA  SSSS  HHHHH W W W  RRRR  AAAAA PPPP
B   B A   A     S  H   H W W W  R R   A   A P
BBBB  A   A  SSSS  H   H W   W  R  RR A   A P
'
echo "$logo"

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <payload_script>"
    exit 1
fi

PAYLOAD_SCRIPT=$1

if [ ! -f "$PAYLOAD_SCRIPT" ]; then
    echo "[!] Error: Payload script '$PAYLOAD_SCRIPT' not found."
    exit 1
fi

sleep_time=$((RANDOM % 5 + 1))
echo "Sleeping for '$sleep_time' to avoid detection..."
sleep $sleep_time

echo "[+] Executing payload..."

bash "$PAYLOAD_SCRIPT" > /dev/null 2>&1 &

echo "Payload executed in the background. Bye!"