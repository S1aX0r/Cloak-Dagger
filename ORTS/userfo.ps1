function Print-logo {

    $logo = @'

     █    ██   ██████ ▓█████  ██▀███    █████▒▒█████  
 ██  ▓██▒▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒▓██   ▒▒██▒  ██▒
▓██  ▒██░░ ▓██▄   ▒███   ▓██ ░▄█ ▒▒████ ░▒██░  ██▒
▓▓█  ░██░  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄  ░▓█▒  ░▒██   ██░
▒▒█████▓ ▒██████▒▒░▒████▒░██▓ ▒██▒░▒█░   ░ ████▓▒░
░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░ ▒ ░   ░ ▒░▒░▒░ 
░░▒░ ░ ░ ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░ ░       ░ ▒ ▒░ 
 ░░░ ░ ░ ░  ░  ░     ░     ░░   ░  ░ ░   ░ ░ ░ ▒  
   ░           ░     ░  ░   ░                ░ ░  
                                                
'@

}

$users = Get-LocalUser

$userInfo = @()

foreach ($user in $users) {
    $groups = Get-LocalGroup | Where-Object { (Get-LocalGroupMember $_.Name).Name -contains $user.Name } | Select-Object -ExpandProperty Name

    $userDetails = [PSCustomObject]@{
        Name        = $user.Name
        Enabled     = $user.Enabled
        Description = $user.Description
        Groups      = -join $groups
    }

    $userInfo += $userDetails
}

$userInfo | Format-Table -AutoSize
