# Atelier B — Qdrant serveur + Ollama (variante locale)

Cette variante est destinée à **Jupyter local ou une VM**, pas à Google Colab.

1. Installer Docker Engine/Compose et Ollama sur la machine cible.
2. Dans ce dossier : `docker compose up -d` ; vérifier `http://127.0.0.1:6333/collections`.
3. Dans un terminal local : `ollama pull qwen2.5:0.5b` puis `ollama list` ; Ollama doit être accessible à `http://127.0.0.1:11434`.
4. Ouvrir le notebook voisin `../TP2B_Qdrant_Ollama_Industrie_Logistique.ipynb` dans Jupyter sur **la même machine**.
5. Au début du notebook régler `QDRANT_BACKEND = 'server'`, `GENERATION_BACKEND = 'ollama'`, et garder les URL `127.0.0.1`.
6. Exécuter toutes les cellules. Les téléchargements de poids de l'encodeur demeurent nécessaires lors de la première exécution.

⚠️ Ne pas exposer les ports Qdrant et Ollama publiquement sans authentification, TLS et contrôles d'accès. Le fichier Compose lie 6333 à 127.0.0.1. Si Qdrant est réellement distant, configurez un accès sécurisé et adapté aux droits métiers. `client.delete_collection` réinitialise volontairement la collection **pédagogique** à chaque exécution : ne pas utiliser ce code pour une collection de production.

Le modèle `qwen2.5:0.5b` est léger mais ses réponses peuvent comporter des erreurs ; vérifier chaque citation. Les données du corpus sont fictives.
