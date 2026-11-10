# Les carnets du RAG — Masters M2 Industry 4.0 & Logistique/services

Parcours pédagogique sur le *Retrieval-Augmented Generation* : **trois séances** (1 h de cours + 2 h de TP chacune, soit 9 h) et un **mini-projet** appliqué aux pages publiques de l'Université de Pau et des Pays de l'Adour (UPPA).

Site : ouvrir `index.html` (aucun backend, aucune dépendance CSS/JS externe).

## Contenu du dépôt

### Pages

| Fichier | Contenu |
|---|---|
| `index.html` | Accueil, schéma animé du pipeline, accès aux cours et au mini-projet |
| `cours1.html` | Cours 1 — tokens, embeddings, attention, Transformers, LLM, principe du RAG |
| `cours2.html` | Cours 2 — les deux phases du RAG, chunking, bases vectorielles, prompt augmenté, citations |
| `cours3.html` | Cours 3 — métriques, fidélité, recherche hybride, reranking, compromis |
| `outils.html` | Atlas de 23 outils RAG (recherche, filtres, fiches, liens officiels) |
| `projet-uppa.html` | Consignes du mini-projet UPPA Smart Assistant (dix étapes, barème, livrables) |

### Ateliers des trois séances — corpus fictif commun

Les ateliers utilisent **12 fiches fictives** (6 Industrie 4.0, 6 logistique) recopiées dans chaque notebook pour qu'il reste autonome ; la référence est `data/corpus_industrie_logistique.json`.

| Notebook (`tp/`) | Séance | Sujet | Questions annotées |
|---|---|---|---|
| `TP1_recherche_semantique_Industrie_Logistique.ipynb` | 1 | Embeddings, FAISS, première mesure Hit@k | 12 |
| `TP2_RAG_complet_Industrie_Logistique.ipynb` | 2 (atelier A) | RAG complet : retrieval, prompt, génération Qwen, citations | 12 |
| `TP2B_Qdrant_Ollama_Industrie_Logistique.ipynb` | 2 (atelier B, facultatif) | Qdrant, payloads, filtres ; variante locale Docker + Ollama dans `tp/atelier-b-local/` | 12 |
| `TP3_Evaluer_Optimiser_RAG_Industrie_Logistique.ipynb` | 3 (atelier A) | Métriques, comparaison de 4 variantes, questions reformulées | 14 + 12 reformulées |
| `TP3B_Ameliorer_RAG_Industrie_Logistique.ipynb` | 3 (atelier B, facultatif) | BM25, RRF, cross-encoder | 20 |

**Pourquoi des questions reformulées ?** Les 12 questions d'origine reprennent les mots des fiches (`PR-17`, `VB-04`, `FEFO`) : une recherche BM25 seule retrouve la bonne fiche au rang 1 pour les 12, et les variantes comparées ne se départagent pas. Les 12 questions reformulées (`questions_reformulees` dans le fichier de données) visent les mêmes fiches sans leur vocabulaire ; BM25 seul n'en retrouve plus que 5 sur 12 dans les trois premiers résultats.

### Mini-projet UPPA Smart Assistant

Chaque notebook produit une archive lue par le suivant. Sans archive, chacun se rabat sur un petit corpus **explicitement fictif**, jamais présenté comme une source UPPA.

| Notebook (`tp/`) | Rôle | Entrée → sortie |
|---|---|---|
| `Notebook01_UPPA_Acquisition_Preparation.ipynb` | Collecte contrôlée (hôtes autorisés, `robots.txt`), Markdown, métadonnées, couverture | pages publiques → `UPPA_Notebook01_exports_*.zip` |
| `Notebook02_UPPA_Chunking_Embeddings_Qdrant.ipynb` | Chunking structurel, embeddings multilingues, Qdrant local — **index de référence V2** | NB01 → `UPPA_Notebook02_index_*.zip` |
| `Notebook02_V3_UPPA_Optimisation_Retrieval.ipynb` | Atelier 02+ : découpage contrôlé en tokens, stratégies A/B/C/D | NB01 + NB02 → `UPPA_Notebook02_V3_index_*.zip` |
| `Notebook03_UPPA_Recherche_Generation_RAG.ipynb` | Recherche filtrée, contexte `[S1]`, génération Qwen, audit des citations | index V2 ou V3 → `UPPA_Notebook03_reponses_*.zip` |
| `Notebook04_UPPA_Evaluation_Hybride_Reranking.ipynb` | Dense, BM25, hybride RRF, reranking ; métriques au niveau document ; grille de 45 questions | index V2 ou V3 (+ NB03) → `UPPA_Notebook04_evaluation_*.zip` |

`tp/exemples/UPPA_Notebook01_exports_synthetic_demo.zip` : petit jeu **fictif** pour tester l'enchaînement NB01 → NB02.

Points de méthode à connaître :

- **V2 et V3 coexistent volontairement.** Le Notebook 02 mesure et affiche la part de chunks tronqués par l'encodeur (limite en tokens) mais conserve son découpage : il sert de référence à l'Atelier 02+, qui corrige la troncature en regroupant des phrases entières et en répétant les en-têtes de tableau.
- **Aucun score sur le corpus réel sans annotations humaines.** Les Notebooks 02, 02 V3 et 04 refusent de calculer Recall/MRR tant que les références ne sont pas renseignées à la main.
- **Modèle de génération.** Le Notebook 03 charge Qwen2.5-1.5B-Instruct si un GPU est disponible, Qwen2.5-0.5B-Instruct sinon (`QWEN_MODEL = 'auto'`).

## Ouvrir un notebook dans Colab

Les boutons des pages ouvrent directement les notebooks de la branche `main` :

`https://colab.research.google.com/github/benlahmar/RAG_Cours_Ateliers/blob/main/tp/<fichier>.ipynb`

Autre possibilité : télécharger le `.ipynb`, puis l'importer depuis <https://colab.research.google.com/#upload>.

Les notebooks installent leurs dépendances et téléchargent leurs modèles à la première exécution : Internet est nécessaire, aucune clé d'API payante ne l'est. Un GPU Colab accélère la génération.

## Mise en ligne

- **GitHub Pages :** Settings → Pages → « Deploy from a branch », branche `main`, répertoire `/(root)`.
- **cPanel ou autre hébergement statique :** copier tous les fichiers en conservant `tp/`, `data/` et `assets/`, par exemple dans `public_html/rag/`, puis ouvrir `https://<votre-domaine>/rag/index.html`.

Pour mettre à jour le dépôt, travailler dans un clone à jour (`git pull`), puis `git add`, `git commit`, `git push`. Ne pas lancer `git init` dans un dossier vide pour pousser par-dessus `main`.

## Vérifier le dépôt

```bash
python scripts/verifier_depot.py
```

Le script contrôle, sans réseau : la validité et la syntaxe de chaque notebook, la concordance du corpus recopié dans les TP avec `data/`, et les liens locaux des pages HTML.

**État des tests.** La logique des notebooks UPPA 02, 02 V3, 03 (mode `inspect`) et 04, ainsi que celle du TP 3, a été exécutée hors ligne de bout en bout avec un **encodeur de substitution** et un vrai Qdrant local. Les modèles réels (encodeur multilingue, cross-encoder, Qwen) et la collecte du Notebook 01 n'ont pas été rejoués : une exécution complète dans Colab reste à faire avant chaque distribution aux étudiants.

## Précautions

- Les procédures industrielles et logistiques, noms de documents et valeurs des TP sont **fictifs** ; ils ne doivent guider aucune décision de sécurité ou de pilotage.
- Le mini-projet est un prototype pédagogique **indépendant de l'UPPA**. La collecte se limite aux pages publiques, sans espace authentifié ni donnée personnelle ; conserver la date de collecte et vérifier les conditions de réutilisation.
- Les informations d'admission changent d'une campagne à l'autre : une réponse de l'assistant est une aide documentaire, jamais une décision administrative.
- Une citation affichée ne prouve pas que le modèle a correctement interprété la source.
- Variante locale de l'atelier 2B : ne pas exposer les ports Qdrant et Ollama sans authentification.

## Illustrations

`assets/` contient les trois infographies du cours 2 en WebP (`architecture-rag`, `strategies-chunking`, `embeddings-bases-vectorielles`), hébergées localement.
