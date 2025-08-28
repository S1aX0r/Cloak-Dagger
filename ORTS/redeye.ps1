function Print-logo {
    $logo = @'

 ██▀███  ▓█████ ▓█████▄ ▓█████▓██   ██▓▓█████ 
▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▓█   ▀ ▒██  ██▒▓█   ▀ 
▓██ ░▄█ ▒▒███   ░██   █▌▒███    ▒██ ██░▒███   
▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒▓█  ▄  ░ ▐██▓░▒▓█  ▄ 
░██▓ ▒██▒░▒████▒░▒████▓ ░▒████▒ ░ ██▒▓░░▒████▒
░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░░ ▒░ ░  ██▒▒▒ ░░ ▒░ ░
  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒  ░ ░  ░▓██ ░▒░  ░ ░  ░
  ░░   ░    ░    ░ ░  ░    ░   ▒ ▒ ░░     ░   
   ░        ░  ░   ░       ░  ░░ ░        ░  ░
                 ░             ░ ░            
'@

Write-Output $logo
}

function Get-FilesByExtension {
    param (
        [string]$Directory,
        [string]$Extension
    )

    if (Test-Path -Path $Directory) {
        $files = Get-ChildItem -Path $Directory -Recurse -Filter "*.$Extension" | 
                 Select-Object Name, FullName, Length

        if ($files.Count -eq 0) {
            Write-Host "No files found with the extension .$Extension in $Directory."
            return
        }

        Write-Host "Found the following files:"
        $files | ForEach-Object { Write-Host "$($_.Name) - Size: $($_.Length) bytes" }

        $openFile = Read-Host "Do you want to open a file? (yes/no)"
        if ($openFile -eq "yes") {
            $fileToOpen = Read-Host "Enter the name of the file to open (include extension)"
            $selectedFile = $files | Where-Object { $_.Name -eq $fileToOpen }

            if ($selectedFile) {
                Start-Process $selectedFile.FullName
            } else {
                Write-Host "File not found. Please check the name and try again."
            }
        }
    } else {
        Write-Host "The specified directory does not exist."
    }
}

$directoryInput = Read-Host "Enter the directory path"
$extensionInput = Read-Host "Enter the file extension (without the dot, e.g., 'txt')"

Print-logo
Get-FilesByExtension -Directory $directoryInput -Extension $extensionInput
