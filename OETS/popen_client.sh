#!/bin/bash

read -p "Enter server IP to connect to: " server_ip
read -p "Enter port to connect to: " port


echo "Connecting to chat server @ $server_ip:$port"

while true; do
	read -p "You: " message
	echo "$message" | nc $server_ip $port
done
