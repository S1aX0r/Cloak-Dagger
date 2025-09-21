#!/bin/bash

cat << "EOF"

 ____       ____      _   _
|  _ \ ___ |  _ \ ___| \ | |
| |_) / _ \| |_) / _ \  \| |
|  __/ (_) |  __/  __/ |\  |
|_|   \___/|_|   \___|_| \_|

EOF

PORT=12345

# Start listening for incoming connections
echo "Server listening on port $PORT..."
while true; do
    # Use netcat to listen for incoming connections
    nc -lvnp $PORT | while read line; do
        echo "Received: $line"
    done
done

