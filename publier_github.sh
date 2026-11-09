#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
if [ ! -d .git ]; then git init -b main; fi
git add -A
git commit -m "Publier les cours RAG M2 : cours 1-2, TP et infographies"
if ! git remote | grep -qx origin; then git remote add origin https://github.com/benlahmar/RAG_Cours_Ateliers.git; fi
git branch -M main
git push -u origin main
echo "Publié sur : https://github.com/benlahmar/RAG_Cours_Ateliers"
