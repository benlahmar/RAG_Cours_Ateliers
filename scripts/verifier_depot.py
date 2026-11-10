#!/usr/bin/env python3
"""Contrôles rapides du dépôt, sans réseau ni modèle.

    python scripts/verifier_depot.py

Vérifie que :
  1. chaque notebook est un JSON nbformat 4 valide et que ses cellules de code sont syntaxiquement correctes ;
  2. le corpus recopié dans les notebooks des TP (identifiants, titres, textes) est identique à
     data/corpus_industrie_logistique.json ;
  3. les liens locaux des pages HTML (notebooks, archives, pages) pointent vers des fichiers existants.

Ce script ne remplace pas une exécution complète dans Colab : il ne télécharge aucun modèle.
"""
import ast, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []

def check_notebooks():
    core = lambda docs: [{k: d.get(k) for k in ('id','titre','domaine','theme','texte')} for d in docs]
    reference = core(json.loads((ROOT/'data'/'corpus_industrie_logistique.json').read_text(encoding='utf-8'))['documents'])
    for path in sorted((ROOT/'tp').glob('*.ipynb')):
        try:
            nb = json.loads(path.read_text(encoding='utf-8'))
        except json.JSONDecodeError as exc:
            errors.append(f'{path.name} : JSON invalide ({exc})'); continue
        if nb.get('nbformat') != 4:
            errors.append(f'{path.name} : nbformat inattendu')
        for n, cell in enumerate(nb['cells']):
            if cell['cell_type'] != 'code': continue
            source = ''.join(cell['source'])
            # Les commandes Colab (%pip, !commande) ne sont pas du Python : on les neutralise.
            python = re.sub(r'^(\s*)[%!].*$', r'\1pass', source, flags=re.M)
            try:
                ast.parse(python)
            except SyntaxError as exc:
                errors.append(f'{path.name} cellule {n} : erreur de syntaxe ligne {exc.lineno} ({exc.msg})')
            match = re.search(r"json\.loads\(r'''(\{\"documents\".*?)'''\)", source, flags=re.S)
            if match:
                embedded = core(json.loads(match.group(1))['documents'])
                if embedded != reference:
                    errors.append(f'{path.name} cellule {n} : le corpus recopié diffère de data/corpus_industrie_logistique.json')
        print(f'  notebook contrôlé : {path.name} ({len(nb["cells"])} cellules)')

def check_links():
    for page in sorted(ROOT.glob('*.html')):
        html = page.read_text(encoding='utf-8')
        for target in sorted(set(re.findall(r'(?:href|src)="([^"#?]+)', html))):
            if re.match(r'^(?:[a-z]+:|//)', target): continue
            if not (ROOT/target).exists():
                errors.append(f'{page.name} : lien local cassé vers {target}')
        print(f'  page contrôlée : {page.name}')

if __name__ == '__main__':
    check_notebooks()
    check_links()
    if errors:
        print('\nPROBLÈMES :'); [print(' -', e) for e in errors]; sys.exit(1)
    print('\nTout est cohérent.')
