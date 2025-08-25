function Print-Logo {
    $logo = @"

██████╗  ██████╗ ██╗    ██╗███████╗██████╗  ██████╗ ██████╗ ██████╗ ███████╗
██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝
██████╔╝██║   ██║██║ █╗ ██║█████╗  ██████╔╝██║     ██║   ██║██║  ██║█████╗  
██╔═══╝ ██║   ██║██║███╗██║██╔══╝  ██╔══██╗██║     ██║   ██║██║  ██║██╔══╝  
██║     ╚██████╔╝╚███╔███╔╝███████╗██║  ██║╚██████╗╚██████╔╝██████╔╝███████╗
╚═╝      ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
                                                                        
"@
    Write-Output $logo
}

function Encode-Command {
    param (
        [string]$Command
    )
    
    $bytes = [System.Text.Encoding]::Unicode.GetBytes($Command)
    
    $encodedCommand = [Convert]::ToBase64String($bytes)
    
    return $encodedCommand
}

Print-Logo

$commandToEncode = Read-Host "Enter the command you want to encode"
$encoded = Encode-Command -Command $commandToEncode
Write-Output "Encoded Command: $encoded"