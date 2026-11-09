# Publication vers le dépôt GitHub RAG_Cours_Ateliers
# Prérequis : Git installé et accès en écriture au dépôt.
$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot
if (-not (Test-Path .git)) { git init -b main }
git add -A
git commit -m "Publier les cours RAG M2 : cours 1-2, TP et infographies"
if ((git remote) -notcontains "origin") { git remote add origin https://github.com/benlahmar/RAG_Cours_Ateliers.git }
git branch -M main
git push -u origin main
Write-Host "Publication terminée : https://github.com/benlahmar/RAG_Cours_Ateliers"
