Import-Module posh-git
Import-Module oh-my-posh
Import-Module PSWriteColor
Set-PoshPrompt -Theme mussweg

Write-Color -Text ""
Write-Color -Text  " __        __        _" -Color Yellow
Write-Color -Text  " \ \      / /  ___  | |   ___    ___    _ __ ___     ___"-Color Yellow
Write-Color -Text  "  \ \ /\ / /  / _ \ | |  / __|  / _ \  | '_ ` _  \   / _ \"-Color Yellow
Write-Color -Text  "   \ V  V /  |  __/ | | | (__  | (_) | | | | | | | |  __/"-Color Yellow
Write-Color -Text  "    \_/\_/    \___| |_|  \___|  \___/  |_| |_| |_|  \___|"-Color Yellow

Write-Color -Text  "     _"-Color Yellow
Write-Color -Text  "    | |      _   _    ___    __ _"-Color Yellow
Write-Color -Text  "    | |     | | | |  / __|  / _`  |"-Color Yellow
Write-Color -Text  "    | |___  | |_| | | (__  | (_| |"-Color Yellow
Write-Color -Text  "    |_____|  \__,_|  \___|  \__,_|"-Color Yellow
Write-Color -Text " "
Write-Color -Text " "

$env:VIRTUAL_ENV_DISABLE_PROMPT = 1

$ScriptDirectory = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent
try {
    . ("$ScriptDirectory\powershell_alias.ps1")
    . ("$ScriptDirectory\themes\dracula.ps1")
}
catch {
    Write-Host "Error while loading supporting PowerShell Scripts" 
}
#endregion


