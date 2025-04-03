# BTC-Puzzle-Solver

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-2.15.0-blue)](https://dash.plotly.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description
BTC-Puzzle-Solver est un outil qui tente de résoudre les puzzles Bitcoin en cherchant des clés privées qui correspondent à des adresses Bitcoin spécifiques. L'application utilise une interface web construite avec Dash pour permettre à l'utilisateur de sélectionner un puzzle et de lancer la recherche de solutions.

## À propos des puzzles Bitcoin
Les puzzles Bitcoin sont des défis cryptographiques qui consistent à trouver la clé privée correspondant à une adresse Bitcoin spécifique. Ces puzzles sont numérotés et organisés par plages de difficulté, chacun représentant un intervalle dans l'espace des clés privées possibles. Résoudre un de ces puzzles peut potentiellement donner accès aux bitcoins associés à l'adresse correspondante.

## Fonctionnalités
- Interface graphique conviviale avec Dash
- Sélection de puzzles prédéfinis
- Choix de méthodes de résolution (Séquentielle, Aléatoire, Hybride)
- Configuration du nombre de processeurs à utiliser
- Affichage en temps réel de la vitesse de calcul
- Sauvegarde automatique des résultats dans un fichier de sortie

## Installation
1. Clonez le dépôt:
```bash
git clone https://github.com/votre-username/BTC-Puzzle-Solver.git
cd BTC-Puzzle-Solver
```

2. Installez les dépendances:
```bash
pip install -r requirements.txt
```

## Utilisation
Lancez l'application avec la commande:
```bash
python main.py
```

L'interface web sera accessible à l'adresse `http://127.0.0.1:8050/` dans votre navigateur.

### Comment ça marche
1. Sélectionnez un puzzle dans la liste déroulante
2. Choisissez votre méthode de résolution préférée
3. Définissez le nombre de cœurs CPU à utiliser
4. Cliquez sur "Start solving" pour commencer la recherche
5. Les résultats s'afficheront en temps réel et seront également sauvegardés dans `output.txt`

## Structure du projet
- `main.py` : Application principale avec l'interface Dash
- `calculs.py` : Fonctions utilitaires pour les calculs
- `constants.py` & `constants_app.py` : Constantes et configuration
- `assets/` : Ressources CSS pour l'interface
- `data/` : Données des puzzles à résoudre avec leurs intervalles de recherche

## Technologies utilisées
- Python 3
- Dash pour l'interface web
- bit pour les opérations Bitcoin
- pandas pour la gestion des données

## Avertissement
Veuillez noter que la résolution de ces puzzles est extrêmement difficile en raison de l'immense espace de recherche des clés privées. Ce projet est principalement éducatif et expérimental.

## Performance
Les performances dépendent fortement du matériel utilisé. Sur un processeur moderne, l'application peut vérifier plusieurs milliers de clés par seconde. Cependant, l'espace de recherche pour chaque puzzle est énorme.
