# Password Cracker
Ce projet permet de cracker des mots de passe dans des interfaces webs.

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-red.svg)
![Tests](https://img.shields.io/badge/unit_tests-OK-green.svg)

## Sommaire
- [Installation](#installation)
- [Use](#use)
- [Tests](#tests)
- [Structure du projet](#structure-of-project)
- [Autors](#autors)

## Première utilisation 
Pour la première utilisation il faut lancer les deux scripts : 
- install.py : il créé l'environnement virtuel et installe toutes les dépendances pour faire fonctionner ce projet
- run.py : il exécute simplement le programme

Commande pour récupérer les sources
```bash
git clone https://github.com/plouiserre/hacking-tools.git
cd tools/password_cracker/scripts
```
Lancer install.py : 
```bash
python install.py
```
Lancer run.py : 
```bash
python run.py
```

## A partir de la deuxième utulisation
Il suffit juste de lancer le script run.py
```bash
cd tools/password_cracker/scripts
python run.py
```

## Tests
Execute all tests : 
```bash
python -m unittest discover -s tests
```

## Structure of project
La structure du projet à partir du dossier "password_cracker"
```
password_cracker
├─── scripts/
├─── src/
│   ├───cli/
│       ├───main.py
```

## Autors
**Pierre-Louis Serré** – Principle Developer