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
Ce dossier regroupe les documents rédigés pendant le projet.

On y retrouve notamment :

- le journal d’avancement
- le rapport d’audit
- les documents de suivi

### `rendu_final/`
Ce dossier contient les livrables finaux du projet.

Il a vocation à regrouper :

- le rapport final
- la présentation de soutenance
- les exports ou fichiers définitifs remis pour le rendu

### `resultats/`
Ce dossier centralise les résultats produits pendant la phase de vérification et d’automatisation.

Il contient notamment :

- les exports générés par le script Python
- les captures liées au JSON
- les captures liées au CSV
- les captures de l’exécution du script sur la machine virtuelle

### `screenshots/`
Ce dossier regroupe l’ensemble des captures d’écran utilisées comme preuves techniques dans le projet.

Les captures sont classées par thème afin de faciliter :

- la rédaction du rapport
- la préparation de la soutenance
- la lecture globale du projet

On y retrouve par exemple des captures liées à :

- l’audit initial
- la configuration SSH
- le pare-feu UFW
- fail2ban
- les logs
- la VM et le réseau
- les utilisateurs et les droits

### `scripts/`
Ce dossier contient le script Python principal du projet.

Ce script permet de vérifier automatiquement plusieurs points de conformité sur la machine sécurisée, puis de générer des résultats exploitables pour le rapport.

### `.gitignore`
Ce fichier permet d’exclure du versionnement Git les fichiers qui n’ont pas vocation à être suivis dans le dépôt.

### `README.md`
Ce fichier présente le projet, son organisation générale et le rôle des différents dossiers du dépôt.
