; -- 64Bit.iss --
; Instalador para un programa llamado Hercules con estructura de carpetas personalizada.

[Setup]
AppName=Hercules
AppVersion=1.0.0
WizardStyle=modern
DefaultDirName=C:\Programs\Hercules
DefaultGroupName=Hercules
UninstallDisplayIcon={pf}\hercules-v1.0.0.exe
Compression=lzma2
SolidCompression=yes
OutputDir=userdocs:Inno Setup Examples Output
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
OutputBaseFilename=hercules-v1.0.0-win64

[Files]
; Crear la carpeta principal y colocar el ejecutable en Hercules //CORREGIR EL NOMBRE DE menu.exe
Source: "C:\Users\Axell\Documents\Github\Hercules\dist\hercules-v1.1.0.exe"; DestDir: "{pf}/Hercules"; DestName: "hercules-v1.1.0.exe"
Source: "C:\Users\Axell\Documents\Github\Hercules\assets\hercules.ico"; DestDir: "{pf}\Hercules\assets"; Flags: ignoreversion

[Dirs]
; Crear la carpeta vacía "assets" en Hercules
Name: "{pf}\Hercules\assets"
Name: "{userappdata}\Hercules"


[Icons]
; Crear un acceso directo del ejecutable en el escritorio
Name: "{commondesktop}\Hercules"; Filename: "{pf}\Hercules\hercules-v1.1.0.exe"

; Crear un acceso directo del programa en el menú de inicio
Name: "{group}\Hercules"; Filename: "{pf}\Hercules\hercules-v1.1.0.exe"

[Run]
; Crear un archivo vacío mymusic.json en la carpeta appdata
Filename: "cmd"; Parameters: "/c echo. > ""{userappdata}\Roaming\Hercules\mymusic.json"""; Flags: runhidden

; Establecer permisos de escritura para mymusic.json (opcional)
Filename: "icacls"; Parameters: """{userappdata}\Roaming\Hercules\mymusic.json"" /grant Everyone:(W)"; Flags: runhidden

; Opcional: Ejecutar el programa después de la instalación
Filename: "{pf}\Hercules\hercules-v1.1.0.exe"; Flags: nowait postinstall skipifsilent
