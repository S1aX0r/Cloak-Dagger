function Print-Logo {
    $logo = @"

██╗    ██╗██╗███╗   ██╗ ██████╗ ██████╗ ██████╗ ███████╗
██║    ██║██║████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝
██║ █╗ ██║██║██╔██╗ ██║██║     ██║   ██║██║  ██║█████╗  
██║███╗██║██║██║╚██╗██║██║     ██║   ██║██║  ██║██╔══╝  
╚███╔███╔╝██║██║ ╚████║╚██████╗╚██████╔╝██████╔╝███████╗
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝

"@

Write-Output $logo
}


function Create-Payload {
    param (
        [string]$Command
    )
    
    $payload = @"
Invoke-Expression "$Command"
"@
    
    return $payload
}

function Obfuscate-Payload {
    param (
        [string]$Payload
    )
    
    $bytes = [System.Text.Encoding]::Unicode.GetBytes($Payload)
    
    $encodedPayload = [Convert]::ToBase64String($bytes)
    
    return $encodedPayload
}

Print-Logo

$commandToExecute = Read-Host "Enter the command you want to include in the payload"

$payload = Create-Payload -Command $commandToExecute
Write-Output "Generated Payload:"
Write-Output $payload

$obfuscatedPayload = Obfuscate-Payload -Payload $payload
Write-Output "Obfuscated Payload (Base64):"
Write-Output $obfuscatedPayload
