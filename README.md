# TechSud - Projet Cybersécurité

## Présentation du projet
Dans le cadre du projet AEGIS en Sécurité des Systèmes d’Information, notre groupe intervient sur un scénario fictif autour de l’entreprise TechSud, une PME ayant subi une compromission de son système d’information.

Notre mission consiste à analyser les vulnérabilités présentes sur l’infrastructure, mettre en place des mesures de sécurisation adaptées, automatiser certaines vérifications grâce à un script Python, puis documenter l’ensemble du travail réalisé dans un rapport et une soutenance.

## Objectifs
- auditer l’existant
- identifier les faiblesses de sécurité
- déployer et configurer une VM Linux
- sécuriser l’accès SSH
- configurer un pare-feu
- mettre en place fail2ban
- gérer les utilisateurs et les droits
- consulter les journaux système
- développer un script Python d’audit
- documenter les actions menées
- préparer la soutenance finale

## Membres du groupe
- Jules Elie
- Evann Carnot
- Quentin Godebert

## Répartition des rôles

### Jules Elie - Infrastructure sécurisée et audit technique
Jules prend principalement en charge la partie technique liée à la machine virtuelle Linux et à son audit initial.

Ses missions principales :
- créer et configurer la VM Ubuntu Server
- vérifier la connectivité réseau
- installer et tester SSH
- réaliser les premières observations techniques
- identifier les services actifs et les ports ouverts
- participer à la mise en place du durcissement système
- configurer les éléments de sécurité comme le firewall et fail2ban
- fournir les preuves techniques nécessaires au rapport

### Evann Carnot - Script Python de vérification automatique
Evann prend principalement en charge la partie automatisation et contrôle de conformité.

Ses missions principales :
- réfléchir à la logique du script d’audit
- développer le script Python
- automatiser l’inventaire des services actifs
- vérifier certains ports ouverts
- contrôler quelques éléments de sécurité de base
- générer une sortie exploitable au format JSON ou CSV
- préparer une démonstration simple du script

### Quentin Godebert - Documentation, rapport et soutenance
Quentin prend principalement en charge l’organisation documentaire du projet.

Ses missions principales :
- structurer le dépôt GitHub
- organiser les captures d’écran
- rédiger les documents de suivi
- construire le rapport écrit
- centraliser les preuves techniques
- préparer le support PowerPoint
- organiser le contenu de la soutenance

## Organisation de la semaine
### Lundi
Analyse du contexte, répartition des rôles, création du dépôt GitHub, mise en place de la VM et premières observations

### Mardi
Déploiement de l’environnement, configuration réseau et accès SSH

### Mercredi
Durcissement de la configuration, firewall, fail2ban, utilisateurs et droits

### Jeudi
Développement du script Python, finalisation de la documentation et préparation de la soutenance

### Vendredi
Finalisation des livrables et soutenance

## Arborescence du dépôt
```text
TechSud_Projet_Cybersecurite/
├── config/
├── docs/
├── presentation/
├── resultats/
├── screenshots/
├── scripts/
├── .gitignore
└── README.md
```

## Contenu du GitHub

- docs/ : contient les documents de suivi, le contexte du projet, la répartition des rôles et le journal d’avancement
- scripts/ : contient le script Python d’audit et les fichiers associés
- screenshots/ : contient les captures d’écran classées par thème : audit initial, SSH, firewall, fail2ban, logs, utilisateurs, réseau, etc.
- presentation/ : contient les éléments liés à la soutenance orale et au support PowerPoint
- config/ : contient les notes et éléments de configuration utiles au projet
- resultats/ : contient les résultats produits par le script d’audit ou d’autres vérifications
