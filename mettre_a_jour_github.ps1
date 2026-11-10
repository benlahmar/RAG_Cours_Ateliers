# Exécuter dans la copie locale du dépôt GitHub, APRÈS extraction de la mise à jour.
# Ne remplace pas une sauvegarde de vos modifications non publiées.
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot
if (-not (Test-Path '.git')) { throw 'Ce dossier n’est pas un clone Git. Clonez d’abord https://github.com/benlahmar/RAG_Cours_Ateliers.git puis copiez-y la mise à jour.' }
$changes = git status --short
Write-Host 'Fichiers modifiés :'
Write-Host $changes
# Un dépôt à jour est nécessaire pour éviter les conflits de push.
git add cours2.html README.md tp/TP2B_Qdrant_Ollama_Industrie_Logistique.ipynb tp/atelier-b-local/README.md tp/atelier-b-local/compose.yaml
git diff --cached --quiet
if ($LASTEXITCODE -eq 1) {
    git commit -m 'Ajouter atelier B Qdrant Ollama adapte aux deux masters M2'
    git push origin main
    Write-Host 'Atelier B publié sur main.'
} elseif ($LASTEXITCODE -eq 0) {
    Write-Host 'Aucun changement à publier.'
} else {
    throw 'Échec de la vérification des changements Git.'
}
