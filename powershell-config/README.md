# Powershell-Config
 
## Installation
1. Install WindowsTerminal
&nbsp;
2. Install the following font
[Hack Regular Nerd Font Complete Mono Windows Compatible.ttf](https://github.com/ryanoasis/nerd-fonts)
Install it by opening the file and press the install button on the top left corner.
&nbsp;

3. WindowsTerminal theme
[copy the code from here](https://github.com/LucaKuechler/Powershell-Config/blob/master/Config/settings.json)
&nbsp;

4. Allow executing scripts in Powershell
* Open Powershell as administrator
```
Set-ExecutionPolicy RemoteSigned
```

5. Install Powershell modules
* Open Powershell as administrator
```
Install-Module posh-git -Scope CurrentUser
Install-Module oh-my-posh -Scope CurrentUser
Install-Module -Name PSWriteColor
```

6. Install my custom oh-my-posh theme
* Use the non admin shell
```
cd ~\OneDrive\Documents\WindowsPowerShell\Modules\oh-my-posh
cd 3.132.0  #Remind that this folders name changes based on the version you have installed.
cd themes
New-Item -ItemType file mussweg.omp.json
notepad mussweg.omp.json
```
or if your Documents are not saved to Onedrive then use this command
```
cd ~\Documents\WindowsPowerShell\Modules\oh-my-posh
cd 3.132.0  #Remind that this folders name changes based on the version you have installed.
cd themes
New-Item -ItemType file mussweg.omp.json
notepad mussweg.omp.json
```
[copy the code from here into the mussweg.omp.json file](https://github.com/LucaKuechler/Powershell-Config/blob/master/Config/mussweg.omp.json)
&nbsp;

7. Create a Powershell $PROFILE
```
notepad $PROFILE
```
[copy this code in your Powershell profile](https://github.com/LucaKuechler/Powershell-Config/blob/master/Config/Microsoft.PowerShell_profile.ps1)


8. Import my custom aliases
```
cd ~\OneDrive\Dokumente\WindowsPowerShell
New-Item -ItemType file powershell_alias.ps1
```

or if your Documents are not saved to Onedrive then use this command

```
cd ~\Dokumente\WindowsPowerShell
New-Item -ItemType file powershell_alias.ps1
```

[copy the code from here into the powershell_alias.ps1 file](https://github.com/LucaKuechler/Powershell-Config/blob/master/Config/powershell_alias.ps1)

9. Enjoy