Jour 1

La première journée a servi à lancer le projet.
Nous avons analysé le contexte TechSud, réparti les rôles, créé le dépôt GitHub et mis en place la VM Ubuntu Server.
Un premier audit a ensuite été réalisé pour relever l’adresse IP, les services actifs, les ports ouverts, l’état de SSH, du firewall et l’absence de fail2ban. 
Cette étape a permis d’obtenir un premier état de la machine avant sécurisation.
Nous avons aussi commencé à préparer le script Python qui servira à automatiser certaines vérifications de sécurité.

Jour 2

La deuxième journée a porté sur la configuration du service SSH. 
Nous avons vérifié l’accès distant à la VM, puis modifié la configuration pour renforcer la sécurité. 
Le port SSH a été changé en 2222, l’accès root a été désactivé et l’authentification par clé a été mise en place. 
La connexion finale se fait désormais avec le compte admintech, sur le port 2222, sans mot de passe.
Nous avons aussi avancé sur le script Python afin de préparer la suite du projet et les futures vérifications automatiques.

Jour 3

La troisième journée a été consacrée au renforcement final de la sécurité de la VM.
Nous avons activé UFW, installé et configuré fail2ban, puis consulté les logs pour vérifier le bon fonctionnement des protections.
Nous avons aussi terminé le script Python d’audit, testé les contrôles de conformité et généré les résultats en JSON et CSV pour le rendu final.
