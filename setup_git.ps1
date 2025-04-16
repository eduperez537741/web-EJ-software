# Script para configurar Git en Windows
Write-Host "Configurando Git..." -ForegroundColor Green

# Verificar si Git está instalado
$gitPath = "C:\Program Files\Git\bin\git.exe"
if (Test-Path $gitPath) {
    Write-Host "Git encontrado en: $gitPath" -ForegroundColor Green
    
    # Agregar Git al PATH
    $currentPath = [Environment]::GetEnvironmentVariable("Path", "Machine")
    if (-not $currentPath.Contains("Git\bin")) {
        $newPath = $currentPath + ";C:\Program Files\Git\bin"
        [Environment]::SetEnvironmentVariable("Path", $newPath, "Machine")
        Write-Host "Git agregado al PATH del sistema" -ForegroundColor Green
    }
    else {
        Write-Host "Git ya está en el PATH" -ForegroundColor Yellow
    }
    
    # Verificar la versión de Git
    & $gitPath --version
}
else {
    Write-Host "Git no encontrado. Por favor, instala Git desde https://git-scm.com/download/win" -ForegroundColor Red
}

Write-Host "`nPor favor, cierra y vuelve a abrir la terminal para que los cambios surtan efecto." -ForegroundColor Yellow 