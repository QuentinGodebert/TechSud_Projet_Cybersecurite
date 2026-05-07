# TechSud - Projet Cybersécurité

TechSud est un projet d'audit et de sécurisation d'une machine Linux. Il regroupe la documentation du projet, les preuves techniques, les résultats d'audit et un script Python permettant d'automatiser plusieurs vérifications de conformité.

Ce projet a été réalisé en groupe de 3 dans le cadre d'un travail de formation.

## Objectif

L'objectif était d'analyser l'état de sécurité d'une machine, de mettre en place des mesures de durcissement, puis de produire un rendu clair avec preuves, captures et résultats exploitables.

## Points travaillés

- audit initial de la machine ;
- configuration et vérification du service SSH ;
- vérification du pare-feu UFW ;
- mise en place et contrôle de fail2ban ;
- analyse des ports ouverts ;
- contrôle des utilisateurs et des droits ;
- génération de résultats au format exploitable pour le rapport.

## Technologies et outils utilisés

- Linux / Ubuntu
- Python
- SSH
- UFW
- fail2ban
- Virtualisation
- JSON / CSV

## Script d'audit

Le dossier `scripts/` contient le script principal `audit_techsud.py`.

Ce script permet notamment de vérifier automatiquement :

- le nom de la machine ;
- l'état du service SSH ;
- l'installation et l'état de fail2ban ;
- l'état du pare-feu UFW ;
- la configuration SSH ;
- les ports ouverts ;
- plusieurs informations utiles pour le rapport final.

## Arborescence du dépôt

```text
TechSud_Projet_Cybersecurite/
├── documentation/
├── rendu_final/
├── resultats/
├── screenshots/
├── scripts/
├── .gitignore
└── README.md
```

## Description des dossiers

### `documentation/`

Documents rédigés pendant le projet : journal d'avancement, rapport d'audit et documents de suivi.

### `rendu_final/`

Livrables finaux du projet : rapport final, présentation de soutenance et fichiers définitifs remis pour le rendu.

### `resultats/`

Résultats produits pendant la phase de vérification et d'automatisation, notamment les exports générés par le script Python.

### `screenshots/`

Captures d'écran utilisées comme preuves techniques : audit initial, SSH, UFW, fail2ban, logs, réseau, utilisateurs et droits.

### `scripts/`

Scripts Python utilisés pour automatiser les vérifications techniques.

## Statut

Projet terminé dans le cadre d'un travail de groupe.