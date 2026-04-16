# Rapport d’audit de sécurité - TechSud

## Quentin Godebert - Jules Elie - Evann Carnot

---

## 1. Introduction

Dans le cadre du projet **AEGIS** en **Sécurité des Systèmes d’Information**, notre groupe intervient sur un scénario fictif mettant en scène l’entreprise **TechSud**, une PME spécialisée dans la distribution de matériel industriel.

L’entreprise a été victime d’un incident de sécurité. Une activité anormale a été observée sur ses systèmes, notamment des connexions SSH suspectes, un fichier inhabituel, une tâche planifiée inconnue et la présence probable d’un webshell sur le serveur web.

Notre mission consiste à :

- analyser le contexte et les risques
- identifier les failles et mauvaises pratiques
- mettre en place des mesures de sécurisation
- vérifier la configuration du système
- développer un script Python d’audit
- produire une documentation et une soutenance

Ce rapport présente le travail réalisé au cours du projet, les choix techniques, les résultats obtenus et les recommandations formulées.

---

## 2. Contexte de mission

### 2.1 Présentation de TechSud

TechSud est une PME fictive de **47 collaborateurs**, basée à **Toulouse**, opérant dans le secteur de la distribution **B2B**.

Selon le **brief de mission**, un incident de sécurité a été signalé le **vendredi 18 avril 2026 à 23h47**. Une alerte de **charge CPU à 98 %** a été déclenchée hors des heures ouvrées. L’analyse préliminaire mentionne plusieurs éléments suspects :

- connexions SSH depuis une adresse IP inconnue
- présence d’un fichier suspect
- tâche cron anormale
- traces incomplètes dans les journaux
- activité réseau sortante suspecte
- présence probable d’un webshell PHP

Ces éléments laissent penser à une **compromission partielle du système d’information**.

### 2.2 Objectif de la mission

À partir du scénario fourni, notre groupe a pour objectif de :

- mettre en place un environnement de démonstration
- réaliser un audit initial
- sécuriser le service SSH
- activer un pare-feu
- mettre en place fail2ban
- exploiter les logs
- automatiser des contrôles avec un script Python
- produire un rapport clair et structuré

---

## 3. Organisation du groupe

Le projet a été réalisé à trois.

### Jules Elie

Infrastructure sécurisée et audit technique

Missions principales :

- mise en place de la VM Ubuntu Server
- vérification réseau
- sécurisation de SSH
- configuration de UFW
- installation et configuration de fail2ban
- collecte des preuves techniques

### Evann Carnot

Développement du script Python d’audit

Missions principales :

- réflexion sur les contrôles de conformité
- développement du script Python
- génération des exports JSON et CSV
- validation des résultats

### Quentin Godebert

Documentation et soutenance

Missions principales :

- structuration du dépôt GitHub
- organisation des captures d’écran
- rédaction du rapport
- préparation du diaporama et de la soutenance

---

## 4. Mise en place de l’environnement

Afin de travailler dans un cadre cohérent, nous avons déployé une **machine virtuelle Ubuntu Server** qui sert de support technique principal au projet.

Nous avons vérifié la configuration réseau et relevé l’adresse IP de la machine.

### Schéma réseau / configuration de la VM

<p align="center">
  <img src="screenshots/vm_reseaux/techsud_reseaux_nat_pont.png" width="80%">
</p>

### Vérification de l’adresse IP

<p align="center">
  <img src="screenshots/vm_reseaux/ip_a.png" width="70%">
</p>

Cette étape nous a permis de préparer les tests à distance et le scan de la machine.

---

## 5. Audit initial

Avant toute sécurisation, nous avons effectué un **audit de l’état initial** de la machine.

L’objectif était de relever :

- les services actifs
- les ports ouverts
- la configuration du réseau
- l’état du service SSH
- l’état du pare-feu
- l’absence de fail2ban

### Scan réseau initial avec Nmap

<p align="center">
  <img src="screenshots/audit_initial/nmap_initial.png" width="80%">
</p>

Le scan montre que la machine répond sur le **port 22**, avec le service **SSH** actif.

### Vérification du service SSH

<p align="center">
  <img src="screenshots/audit_initial/systemctl_status_ssh.png" width="78%">
</p>

### Vérification des ports ouverts

<p align="center">
  <img src="screenshots/audit_initial/ss_tulpn.png" width="82%">
</p>

À ce stade :

- le service SSH écoute sur le **port 22**
- aucun filtrage n’est encore appliqué
- fail2ban n’est pas installé
- l’administration distante n’est pas encore durcie

---

## 6. Vulnérabilités et risques identifiés

À partir du brief de mission et de notre audit initial, plusieurs risques ressortent.

### 6.1 Exposition du service SSH

Le port **22** est exposé, ce qui rend le service SSH facilement détectable.  
Dans le brief, il est également question d’un **accès root activé** sur un serveur web, ce qui constitue un risque important.

**Risque :** accès distant non autorisé  
**Criticité :** élevée

### 6.2 Mauvaises pratiques d’authentification

Le scénario mentionne des **mots de passe faibles** et l’absence d’une politique de sécurité stricte.

**Risque :** bruteforce ou compromission par mot de passe  
**Criticité :** élevée

### 6.3 Absence de surveillance efficace

Le brief évoque des **logs partiellement effacés** et une **absence de centralisation des journaux**.

**Risque :** difficulté de détection et de traçabilité  
**Criticité :** élevée

### 6.4 Service web et base de données exposés

Le dossier mentionne :

- un site en **HTTP sans HTTPS**
- un **webshell probable**
- une **base MariaDB potentiellement exposée**

**Risque :** exécution de code à distance, accès non autorisé  
**Criticité :** élevée

### 6.5 Sauvegardes et règles de sécurité non suivies

Les sauvegardes ne sont pas testées régulièrement et les règles du pare-feu sont peu documentées.

**Risque :** faible résilience et manque de maîtrise de la sécurité  
**Criticité :** moyenne à élevée

---

## 7. Sécurisation de SSH

Nous avons ensuite durci le service SSH pour limiter les risques d’accès non autorisé.

Les mesures mises en place sont les suivantes :

- changement du port SSH de `22` vers `2222`
- désactivation de l’accès root avec `PermitRootLogin no`
- désactivation de l’authentification par mot de passe
- mise en place d’une authentification par clé
- utilisation du compte `admintech` pour l’administration distante

### Fichier de configuration SSH

<p align="center">
  <img src="screenshots/ssh/config_ssh.png" width="80%">
</p>

### Vérification de l’écoute sur le port 2222

<p align="center">
  <img src="screenshots/ssh/ss_tulnp_grep_ssh.png" width="80%">
</p>

### Connexion à la VM avec le compte `admintech` sur le port `2222`

<p align="center">
  <img src="screenshots/ssh/connexion_pc_vers_vm_avec_port_2222.png" width="80%">
</p>

Cette étape permet de **réduire l’exposition du service**, d’**empêcher les connexions root** et de **renforcer l’authentification**.

---

## 8. Mise en place du pare-feu UFW

Pour limiter l’exposition réseau de la machine, nous avons installé et configuré **UFW**.

L’objectif est de n’autoriser que les flux nécessaires à l’administration.

### Installation et activation de UFW

<p align="center">
  <img src="screenshots/firewall/installation_ufw.png" width="80%">
</p>

### Configuration des règles et vérification de l’état du pare-feu

<p align="center">
  <img src="screenshots/firewall/config_ufw.png" width="75%">
</p>

UFW permet ici de :

- limiter les accès réseau
- n’autoriser que le **port 2222/tcp**
- réduire la surface d’attaque

---

## 9. Protection contre les tentatives abusives avec fail2ban

Nous avons ensuite installé **fail2ban** afin de protéger le service SSH contre les tentatives répétées d’authentification.

Une **jail `sshd`** a été configurée pour surveiller le port `2222`.

### Configuration de `jail.local`

<p align="center">
  <img src="screenshots/fail2ban/config_jail.local.png" width="55%">
</p>

### Vérification du statut de fail2ban

<p align="center">
  <img src="screenshots/fail2ban/fail2ban-client_check.png" width="60%">
</p>

Le service est actif et surveille bien le service SSH.

Nous avons également réalisé un test avec plusieurs tentatives de connexion invalides afin de vérifier le fonctionnement du bannissement.

---

## 10. Consultation et surveillance des logs

La surveillance des journaux est indispensable pour vérifier le fonctionnement des services et repérer les comportements anormaux.

Nous avons consulté les journaux de **SSH** et de **fail2ban**.

### Logs du service SSH

<p align="center">
  <img src="screenshots/logs_surveillance/logs_ssh.png" width="82%">
</p>

Ces journaux permettent de visualiser :

- les connexions réussies
- les tentatives refusées
- les redémarrages du service
- les événements liés à l’authentification

### Logs de fail2ban

<p align="center">
  <img src="screenshots/logs_surveillance/logs_fail2ban.png" width="82%">
</p>

Ces journaux permettent de vérifier :

- le démarrage du service
- la prise en compte de la jail `sshd`
- les éventuels bannissements

Cette étape montre qu’une machine sécurisée doit être **surveillée** et non simplement configurée.

---

## 11. Script Python d’audit

Afin d’automatiser certaines vérifications, nous avons développé un **script Python local**.

Ce script réalise plusieurs contrôles de conformité, notamment :

- état du service SSH
- port configuré
- écoute sur le port `2222`
- désactivation du compte root
- désactivation du mot de passe pour SSH
- état de UFW
- présence et activité de fail2ban
- activité de la jail `sshd`

### Exécution du script

<p align="center">
  <img src="resultats/resultats_vm_1.png" width="48%">
</p>

<p align="center">
  <img src="resultats/resultats_vm_2.png" width="60%">
</p>

Le résultat final indique que **9 contrôles sur 9 sont validés**, ce qui confirme que la machine est correctement sécurisée au regard des objectifs du projet.

---

## 12. Exports JSON et CSV

Le script génère également deux fichiers d’export :

- `audit_result.json`
- `audit_result.csv`

Ces formats facilitent la lecture et la réutilisation des résultats.

### Export JSON

<p align="center">
  <img src="resultats/json_1.png" width="38%">
</p>

### Export CSV

<p align="center">
  <img src="resultats/csv.png" width="60%">
</p>

Ces exports permettent de conserver une trace structurée des vérifications et d’intégrer les résultats dans la documentation finale.

---

## 13. Bilan des mesures mises en place

Au terme du projet, nous avons mis en œuvre plusieurs actions concrètes :

- déploiement d’une VM Ubuntu Server
- audit initial de l’environnement
- durcissement du service SSH
- passage sur le port `2222`
- désactivation de l’accès root
- authentification par clé
- activation de UFW
- installation et configuration de fail2ban
- consultation des logs
- développement d’un script Python d’audit
- génération d’exports JSON et CSV

Les résultats obtenus sont conformes aux objectifs fixés.

---

## 14. Recommandations pour TechSud

Même si notre mise en œuvre a été réalisée sur une **VM de démonstration**, le brief met en évidence plusieurs recommandations importantes pour TechSud.

### Recommandations prioritaires

- conserver l’authentification SSH par clé et désactiver les mots de passe
- limiter l’exposition des services d’administration sur Internet
- centraliser les logs
- documenter les règles de pare-feu
- tester régulièrement les sauvegardes
- mettre en place **HTTPS** sur les services web exposés
- limiter l’accès à la base de données au strict nécessaire
- renforcer les politiques de mot de passe
- surveiller les connexions et les événements suspects

---

## 15. Conclusion

Ce projet nous a permis de travailler à partir d’un **scénario réaliste de compromission**, puis de proposer une réponse technique cohérente sur un environnement de démonstration.

Nous avons réalisé un audit initial, identifié les risques principaux, sécurisé l’accès SSH, mis en place un pare-feu, protégé le service contre les tentatives abusives avec fail2ban, consulté les logs et développé un script Python d’audit.

L’ensemble du travail a été documenté dans un dépôt GitHub et présenté dans une soutenance.

Même si nous n’avons pas reproduit toute l’infrastructure du brief, nous avons répondu à plusieurs priorités de sécurité mises en avant dans la mission et proposé des recommandations pertinentes pour l’entreprise TechSud.

---

## 16. Annexes

### Outils utilisés

- Ubuntu Server
- OpenSSH
- UFW
- fail2ban
- Python 3
- GitHub
- PowerShell
- Nmap

### Fichiers produits

- `scripts/audit_techsud.py`
- `audit_result.json`
- `audit_result.csv`

### Dépôt GitHub

Le dépôt contient :

- les captures d’écran
- le script Python
- les exports JSON et CSV
- le journal de projet
- le support de présentation
- le rapport d’audit
