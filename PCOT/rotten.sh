#!/bin/bash

logo='
RRRR    OOO  TTTTT TTTTT EEEE  N   N
R   R  O   O   T     T   E     NN  N
RRRR   O   O   T     T   EEEE  N N N
R  R   O   O   T     T   E     N  NN
R   R   OOO    T     T   EEEE  N   N
'
echo "$logo"

echo "Enter command or message to obfuscate: "
read user_command

encoded_command=$(echo "$user_command" | tr 'A-Za-z' 'N-ZA-Mn-za-m')

echo "obfuscated command: $encoded_command"

echo "$encoded_command" | tr 'A-Za-z' 'N-ZA-Mn-za-m' | bash