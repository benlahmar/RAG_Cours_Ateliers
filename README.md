# Les carnets du RAG — Masters M2 Industry 4.0 & Logistique/services

Archive pédagogique contenant deux séances, chacune avec **1 h de cours et 2 h de TP**.

## Contenu

- `index.html` : page d'accueil du parcours et navigation vers les deux cours
- `cours1.html` : cours 1 avec accordéon vertical **Cours / TP** (pré-requis, tokens, embeddings, attention, Transformers, LLM, recherche)
- `cours2.html` : cours 2 enrichi avec les **deux phases du RAG**, acquisition, nettoyage, chunking (5 méthodes), embeddings et indexation, FAISS/Chroma/Qdrant/pgvector, retrieval, top-k, prompt augmenté, génération et citations
- `tp/TP1_recherche_semantique_Industrie_Logistique.ipynb` : recherche sémantique, embeddings, FAISS
- `tp/TP2_RAG_complet_Industrie_Logistique.ipynb` : véritable pipeline RAG complet, génération locale avec Qwen2.5-0.5B-Instruct (téléchargement des poids requis)
- `data/corpus_industrie_logistique.json` : corpus commun de **12 documents fictifs** et **12 questions annotées** pour les deux TP.

## Mise en ligne sur cPanel

Décompresser **tous les fichiers** en gardant les sous-dossiers `tp/` et `data/` dans un répertoire du domaine, par exemple `public_html/rag/`. Ouvrir `https://<votre-domaine>/rag/index.html`.

L'interface HTML fonctionne sans backend ni base de données ; il n'y a pas de dépendance CSS/JS externe. Les contenus des simulations sont pédagogiques et s'exécutent directement dans le navigateur.

## Colab

Dans chaque volet TP :

1. Télécharger le fichier `.ipynb` correspondant ;
2. Cliquer sur **Ouvrir dans Google Colab** ;
3. Dans Colab, importer/upload le notebook téléchargé.

Le lien du bouton Colab utilise **l'import**, et non un lien direct inexistant. Pour une ouverture directe après publication sur GitHub, renseigner `configuredColabNotebookUrl` dans le script HTML de la page concernée avec une URL vérifiée, par exemple `https://colab.research.google.com/github/<user>/<repo>/blob/<branch>/tp/<file>.ipynb`.

Le TP 2 requiert Internet pour installer ses dépendances et télécharger un modèle d'embeddings ainsi qu'un petit LLM ouvert. Un GPU Colab facilite l'exécution ; sur CPU, la génération est plus lente. Aucune clé d'API payante n'est requise.

## Précautions

Les procédures industrielles et logistiques, noms de documents, valeurs et exemples sont **fictifs**. Ils ne doivent pas guider des décisions de sécurité ou de pilotage de machines réelles. Une citation ne garantit pas que le LLM ait correctement interprété la source.

## Infographies originales du Cours 2

Les trois illustrations sont incluses localement dans `assets/` en **WebP optimisé** (lecture et agrandissement) :

- `architecture-rag.webp` — indexation / interrogation ;
- `strategies-chunking.webp` — cinq méthodes ;
- `embeddings-bases-vectorielles.webp` — corpus, vecteurs, top-k, moteurs vectoriels.

Cliquez sur une figure dans le cours pour l’ouvrir à sa taille complète. Aucun hébergeur d’images externe n’est nécessaire.

**Colab après push :** Les boutons des TP renvoient directement vers les notebooks de la branche `main`.

**Publication GitHub Pages (facultative) :** dans Settings > Pages, sélectionner « Deploy from a branch », puis la branche `main` et le répertoire `/(root)`.


## Cours 03 — Évaluer, optimiser et fiabiliser

- `cours3.html` : carnet interactif de 60 minutes, deux volets verticaux Cours / TP, 4 simulations (métriques, fidélité, RRF, compromis).
- `tp/TP3_Evaluer_Optimiser_RAG_Industrie_Logistique.ipynb` : atelier Colab autonome de 2 heures, comparaison A/B/C/D sur le corpus commun.
- Les chiffres des simulations HTML sont fictifs, les métriques du notebook sont recalculées sur le jeu de référence lors de l'exécution.
- La fidélité d'une réponse générée est évaluée séparément de la qualité de retrieval.

**Accès Colab direct** : `https://colab.research.google.com/github/benlahmar/RAG_Cours_Ateliers/blob/main/tp/TP3_Evaluer_Optimiser_RAG_Industrie_Logistique.ipynb` (après mise en ligne du notebook sur GitHub).


## Nouvel Atelier B — Module 2 : Qdrant + Ollama (deux masters)

- Dans `cours2.html`, ouvrez le **volet vertical TP**, puis choisissez **Atelier B — Qdrant + Ollama**. L'**Atelier A avec FAISS** reste intact et constitue le TP 2 obligatoire de 2 h.
- `tp/TP2B_Qdrant_Ollama_Industrie_Logistique.ipynb` : notebook Colab/Jupyter autonome sur le même corpus de 12 documents, avec chunking phrase-aware, encodeur multilingue, Qdrant local, payloads, filtres de domaine, retrieval, génération et audit des citations.
- **Colab (par défaut)** : Qdrant `:memory:` + Qwen2.5-0.5B-Instruct via Transformers, sans Docker ni clé API ; modèle téléchargé lors du premier lancement.
- **Local (optionnel)** : dossier `tp/atelier-b-local/` avec `compose.yaml` pour Qdrant serveur et instructions pour Ollama `qwen2.5:0.5b` ; modifier les deux variables `QDRANT_BACKEND` et `GENERATION_BACKEND` dans le notebook.
- Bouton Colab direct dans `cours2.html` : `https://colab.research.google.com/github/benlahmar/RAG_Cours_Ateliers/blob/main/tp/TP2B_Qdrant_Ollama_Industrie_Logistique.ipynb` une fois le notebook ajouté au dépôt.

**Enjeux des deux masters :** Industrie 4.0 (PR-17, VB-04, métrologie) et Logistique & services (FEFO, WMS, quais). Les données sont fictives et ne fournissent pas de mesures ni de stocks en temps réel. L'atelier B est un **prolongement recommandé de 60–90 min**, hors volume obligatoire de 9 heures.

### Mise à jour dans le dépôt GitHub existant

1. Utilisez un clone à jour de `https://github.com/benlahmar/RAG_Cours_Ateliers.git` (`git clone` si nécessaire).
2. Décompressez `RAG_M2_Mise_a_jour_Atelier_B_Qdrant_Ollama.zip` **dans la racine de ce clone**, en conservant les chemins.
3. Dans PowerShell, lancez `./mettre_a_jour_github.ps1` (si la politique d’exécution l’autorise) ou faites `git add .`, `git commit -m "Ajout Atelier B Qdrant"`, `git push origin main`.

Ne lancez pas `git init` dans un nouveau dossier vide pour pousser par-dessus la branche `main` existante.


## Nouveau — Atelier 3B : améliorer un RAG

Le volet **TP** du `cours3.html` contient désormais deux onglets : **A — Évaluer** et **B — Améliorer**.

Le nouveau notebook se trouve dans :

`tp/TP3B_Ameliorer_RAG_Industrie_Logistique.ipynb`

Il est autonome et utilise les 12 fiches communes, 20 questions annotées, BM25, recherche dense, RRF et un cross-encoder multilingue. Le notebook inclut deux parcours : Industry 4.0 et Logistique industrielle / services.

### Google Colab

Avant publication, téléchargez le notebook puis importez-le via https://colab.research.google.com/#upload.
Une fois cette mise à jour poussée sur la branche `main`, l'URL directe sera :

https://colab.research.google.com/github/benlahmar/RAG_Cours_Ateliers/blob/main/tp/TP3B_Ameliorer_RAG_Industrie_Logistique.ipynb

À ce moment-là, dans `cours3.html`, modifiez `const notebookPublie=false` en `true` pour activer le bouton direct (ou utilisez l'URL ci-dessus).

Cet atelier est **facultatif**, en complément des 9 heures obligatoires.


## Mini-projet UPPA Smart Assistant — Formations, Admissions et Recherche

- `projet-uppa.html` : consignes pédagogiques complètes du mini-projet M2, sans calendrier imposé, avec dix étapes de réalisation, architecture RAG interactive, recherche multi-domaines, cas d’usage, critères d’évaluation et livrables.
- `index.html` : nouveau lien visible **« Mini-projet UPPA »** et encart de présentation, à côté des trois cours.
- Sources officielles à explorer : https://formation.univ-pau.fr/fr/trouver-votre-formation.html ; https://formation.univ-pau.fr/fr/admission.html ; https://recherche.univ-pau.fr/fr/laboratoires.html .
- **Respect des sources** : collecte limitée aux documents publics, sans espace authentifié ni données personnelles ; vérifier les conditions de réutilisation et conserver la date de collecte. Le projet n’est pas un service officiel de l’UPPA.
- **Installation** : placer `projet-uppa.html` dans le même répertoire que `index.html`, sans modifier les dossiers existants. L’application et ses schémas fonctionnent sans serveur applicatif.


## Notebook 01 — Acquisition et préparation UPPA

- `tp/Notebook01_UPPA_Acquisition_Preparation.ipynb` : atelier Google Colab, 39 cellules (dont 22 cellules de code).
- Trois domaines : formations, admissions, recherche ; URL officielles contrôlées, robots.txt, extraction HTML, Markdown, tableaux, métadonnées et audit.
- Corpus fictif de secours explicitement distinct si le site ne peut pas être interrogé ; aucune donnée fictive ne doit être présentée comme source UPPA.
- Sorties Colab : `corpus_uppa.jsonl` (si collecte officielle autorisée) ou `corpus_synthetic_demo.jsonl`, `manifest_*.jsonl`, `dataset_info.json`, Markdown, CSV qualité et ZIP.
- `projet-uppa.html` contient un accès direct au notebook et un lien Colab (ce dernier après publication GitHub).


## Notebook 02 — Chunking, embeddings et Qdrant (UPPA)

- `tp/Notebook02_UPPA_Chunking_Embeddings_Qdrant.ipynb` : Colab guidé, import JSONL/ZIP issu du Notebook 01, chunking récursif et conscient des titres/tableaux, embeddings multilingues, Qdrant local persistant, recherche avec filtres par domaine, mini-audit et export index vers Notebook 03.
- Entrée réelle : `UPPA_Notebook01_exports_uppa.zip` ou `corpus_uppa.jsonl` ; entrée de démonstration : six fiches **fictives** issues de la structure Notebook 01.
- Sortie : `UPPA_Notebook02_index_uppa.zip` ou `UPPA_Notebook02_index_synthetic_demo.zip` avec `exports/index_manifest.json`, chunks, rapport et base `qdrant_local/`.
- Le notebook ne collecte pas de pages, ne génère pas de réponses LLM et ne présente pas le corpus fictif comme une source officielle.
- Qdrant en mode local ne nécessite ni Docker ni clé API ; les dépendances et le modèle d'embeddings multilingue sont téléchargés à la première exécution.
- `projet-uppa.html` propose un lien de téléchargement et un bouton Colab. Le bouton fonctionnera dès publication de ce fichier à la racine `tp/` de la branche `main` de `https://github.com/benlahmar/RAG_Cours_Ateliers`.

- `tp/exemples/UPPA_Notebook01_exports_synthetic_demo.zip` : petit jeu de données **fictives** provenant de la sortie du Notebook 01, pour vérifier la transition ZIP → Notebook 02.


## Notebook 03 — Recherche et génération RAG avec Qwen (UPPA)

- `tp/Notebook03_UPPA_Recherche_Generation_RAG.ipynb` : Colab pédagogique connecté aux exports du Notebook 02.
- Utilise `UPPA_Notebook02_index_uppa.zip` (réel) ou `UPPA_Notebook02_index_synthetic_demo.zip` (fictif) ; sans archive, 13 chunks de démonstration explicitement fictifs sont inclus et réellement indexés dans Qdrant à l'exécution.
- Reconnaît la collection, les métadonnées, les dimensions d'embeddings ; réutilise le Qdrant local ou reconstruit l'index depuis les chunks.
- Recherche top-k / filtre par domaine, construction de contexte tracé `[S1]`, génération Qwen2.5-0.5B-Instruct, validation syntaxique des labels, contrôle humain obligatoire de la fidélité et avertissement pour l'admission.
- Deux modes : `qwen` (vrai LLM, téléchargement nécessaire) et `inspect` (retrieval seulement, **pas une réponse générée**).
- Exports : `journal_rag_*.jsonl`, `grille_evaluation_*.csv`, `generation_manifest.json` et archive ZIP à réutiliser dans le Notebook 04.
- Le lien Colab de `projet-uppa.html` est prévu pour `https://colab.research.google.com/github/benlahmar/RAG_Cours_Ateliers/blob/main/tp/Notebook03_UPPA_Recherche_Generation_RAG.ipynb` et deviendra accessible lorsque ce fichier sera publié dans GitHub.
- **Vérification :** syntaxe et exécution hors ligne contrôlées avec composants de substitution ; la génération réelle du modèle et la bibliothèque Qdrant installée dans Colab restent à vérifier par les étudiants.


## Correctif qualité NB01/NB02 — version révisée

- `tp/Notebook01_UPPA_Acquisition_Preparation.ipynb` : nettoyage de l’interface, distinction pages hub / pages utiles, tableau de bord de couverture `couverture_sources_*.csv` et `journal_statuts_*.csv`.
- `tp/Notebook02_UPPA_Chunking_Embeddings_Qdrant.ipynb` : pages hub exclues de Qdrant, tableaux longs scindés avec les en-têtes, heatmap limitée à 120 chunks, récupération multi-domaines diversifiée, création de `questions_a_annoter_uppa.csv` pour les jeux réels.
- Le manifeste du NB02 reste au schéma `uppa_rag_index_v1` ; le Notebook 03 peut lire les mêmes chunks et l’index Qdrant.
- Les tests locaux portent sur la logique hors ligne. Les téléchargements et les modèles réels doivent être testés dans Colab.


## Atelier 02+ — Notebook 02 V3 (complémentaire, baseline préservée)

- `tp/Notebook02_V3_UPPA_Optimisation_Retrieval.ipynb` : optimisation du chunking et de la recherche Qdrant ; NE remplace PAS `tp/Notebook02_UPPA_Chunking_Embeddings_Qdrant.ipynb` (V2).
- Entrées réelles : `UPPA_Notebook01_exports_uppa.zip` (documents sources) ET `UPPA_Notebook02_index_uppa.zip` (chunks réels de V2).
- Sans archives, la démonstration repose sur six documents explicitement fictifs et une baseline reconstituée, jamais confondue avec les résultats du site UPPA.
- Même modèle : `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, même corpus, index Qdrant distincts.
- Expériences : A V2 globale, B V3 globale, C V3 diversifiée et D V3 décomposée.
- Mesures document-level : Hit@6, Recall@6, MRR@6 et latence ; aucun score réel tant que les références ne sont pas annotées.
- Sorties : `UPPA_Notebook02_V3_index_uppa.zip` ou version fictive, format `exports/` + `qdrant_local/` reconnu par Notebook 03. Pour NB03, téléverser l'archive V3 manuellement, car sa détection automatique recherche la nomenclature V2.
- Le fichier Colab direct est lié depuis `projet-uppa.html`, publication GitHub restant à effectuer.
- Vérification : structure/syntaxe du notebook et exécution de ses 20 cellules Python (hors installation) dans un banc de test hors ligne avec embeddings, tokenizer et Qdrant simulés. La vraie exécution Colab avec modèle téléchargé et Qdrant reste à valider.


## Nouvelle bibliothèque et ateliers détaillés

- `outils.html` : catalogue interactif de 23 technologies RAG (recherche, filtres, fiches détaillées, commandes et liens officiels).
- `index.html` : accès direct à l’Atlas des outils.
- `cours1.html`, `cours2.html`, `cours3.html` : déroulés TP remplacés par accordéons riches (objectif, code, observation et discussion).
- Les notebooks, leur contenu et leurs liens sont conservés sans changement.
- Les extraits Python d’illustration sont destinés à être exécutés **après** les cellules précédentes des notebooks correspondants.
- Aucun compte, aucune API ou service tiers n’est requis pour consulter les pages HTML.
