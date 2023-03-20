Set-PSReadlineOption -Color @{
    "Command" = [ConsoleColor]::Yellow
    "Parameter" = [ConsoleColor]::Gray
    "Operator" = [ConsoleColor]::Magenta
    "Variable" = [ConsoleColor]::Red
    "String" = [ConsoleColor]::White
    "Number" = [ConsoleColor]::Blue
    "Type" = [ConsoleColor]::Cyan
    "Comment" = [ConsoleColor]::DarkCyan

}