# Les carnets du RAG — parcours complet M2 (9 h)

Support étudiant pour les masters **Industry 4.0** et **Systèmes informatiques pour le génie de la logistique industrielle et des services**.

Le parcours comporte **3 séances × (1 h de cours + 2 h de TP)**. Chaque chapitre propose un volet vertical « Cours » et un volet vertical « TP · Atelier » ; le contenu s'ouvre horizontalement et l'interface est adaptée aux mobiles.

## Fichiers

- `index.html` — accueil et navigation entre les trois chapitres.
- `cours1.html` — tokens, embeddings, attention, Transformers, encodeurs/décodeurs, LLM, principes du RAG.
- `cours2.html` — ingestion, nettoyage, chunking (5 stratégies), indexation, FAISS / Chroma / Qdrant / pgvector, récupération, augmentation, génération, citations.
- `cours3.html` — **évaluation et optimisation** : gold set, Precision@k, Recall@k, Hit@k, MRR, fidélité, recherche hybride BM25 + RRF, reranking, coût / latence et sécurité. Quatre interactions pédagogiques.
- `tp/TP1_recherche_semantique_Industrie_Logistique.ipynb` — indexation et recherche sémantique.
- `tp/TP2_RAG_complet_Industrie_Logistique.ipynb` — assistant RAG avec véritable génération via modèle ouvert Qwen2.5-0.5B-Instruct.
- `tp/TP3_Evaluer_Optimiser_RAG_Industrie_Logistique.ipynb` — évaluation réelle de quatre configurations sur le corpus du module ; pas de clé API requise.
- `data/corpus_industrie_logistique.json` — **12 documents fictifs** et **12 questions annotées** réutilisées dans les TP. Le TP3 contient en plus deux questions multisources et deux cas sans preuve.
- `assets/architecture-rag.webp` — architecture complète du RAG.
- `assets/strategies-chunking.webp` — comparatif des stratégies de chunking.
- `assets/embeddings-bases-vectorielles.webp` — indexation et bases vectorielles.

Les trois images sont des ressources locales incluses dans l'archive ; les schémas complémentaires du Cours 3 sont intégrés au HTML.

## Déploiement statique : cPanel / GitHub Pages

Copier **tous les fichiers et sous-dossiers** sans modifier la structure. Ouvrir `index.html`. Sur cPanel, le placer par exemple dans `public_html/rag/`. Pour GitHub Pages, activer **Settings → Pages → Deploy from a branch → main → /(root)**.

Il n'y a ni backend ni base de données nécessaires pour le site. Les quatre simulations du Cours 3 fonctionnent hors ligne et leurs nombres fictifs sont explicitement identifiés.

## Notebooks Colab

Les notebooks sont téléchargeables depuis les panneaux TP. Après publication sur GitHub, les liens d'ouverture directe attendus sont :

- TP1 : `https://colab.research.google.com/github/benlahmar/RAG_Cours_Ateliers/blob/main/tp/TP1_recherche_semantique_Industrie_Logistique.ipynb`
- TP2 : `https://colab.research.google.com/github/benlahmar/RAG_Cours_Ateliers/blob/main/tp/TP2_RAG_complet_Industrie_Logistique.ipynb`
- TP3 : `https://colab.research.google.com/github/benlahmar/RAG_Cours_Ateliers/blob/main/tp/TP3_Evaluer_Optimiser_RAG_Industrie_Logistique.ipynb`

**Attention :** tant que le TP3 n'est pas poussé sur GitHub, son URL Colab directe ne peut pas être utilisée. Vous pouvez télécharger le fichier `.ipynb` et l'importer manuellement dans Colab.

Les TP exigent une connexion pour installer les bibliothèques et télécharger le modèle d'embeddings. L'exécution du TP2 télécharge également un LLM. Le TP3 n'exige pas de LLM pour ses mesures de retrieval ; son audit de fidélité est basé sur des affirmations annotées. Le rendu de résultats du TP3 dépend du modèle et de l'environnement d'exécution. Les performances réelles n'ont pas été pré-calculées dans cette archive.

## Précautions et limites

Les procédures industrielles, valeurs, équipements et documents sont **fictifs**. Ne jamais les utiliser pour décider d'une opération de sécurité sur une installation réelle. Les metrics de retrieval et la fidélité de la génération sont deux objets distincts. Un jeu de 14 questions positives est **pédagogique** : il ne suffit pas pour une validation industrielle ou une démonstration statistique de supériorité.

## Publier la mise à jour sur un dépôt Git déjà cloné

Copier les fichiers de l'archive dans le dossier local du dépôt, puis :

```bash
git add .
git commit -m "Ajout cours 03 et TP 03 : évaluation et optimisation RAG"
git push origin main
```

Ne pas exécuter `git init` dans un clone existant ; les scripts de publication fournis avec les archives précédentes visent le cas d'un dossier non encore initialisé.
