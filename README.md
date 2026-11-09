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

- `architecture-ragarchitecture-rag.webp` — indexation / interrogation ;
- `strategies-chunkingstrategies-chunking.webp` — cinq méthodes ;
- `embeddings-bases-vectoriellesembeddings-bases-vectorielles.webp` — corpus, vecteurs, top-k, moteurs vectoriels.

Cliquez sur une figure dans le cours pour l’ouvrir à sa taille complète. Aucun hébergeur d’images externe n’est nécessaire.

**Colab après push :** Les boutons des TP renvoient directement vers les notebooks de la branche `main`.

**Publication GitHub Pages (facultative) :** dans Settings > Pages, sélectionner « Deploy from a branch », puis la branche `main` et le répertoire `/(root)`.
