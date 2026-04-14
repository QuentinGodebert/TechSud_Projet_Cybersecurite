Jour 1

La première journée a servi à lancer le projet.
Nous avons analysé le contexte TechSud, réparti les rôles, créé le dépôt GitHub et mis en place la VM Ubuntu Server.
Un premier audit a ensuite été réalisé pour relever l’adresse IP, les services actifs, les ports ouverts, l’état de SSH, du firewall et l’absence de fail2ban. 
Cette étape a permis d’obtenir un premier état de la machine avant sécurisation.

Jour 2

La deuxième journée a porté sur la configuration du service SSH. 
Nous avons vérifié l’accès distant à la VM, puis modifié la configuration pour renforcer la sécurité. 
Le port SSH a été changé en 2222, l’accès root a été désactivé et l’authentification par clé a été mise en place. 
La connexion finale se fait désormais avec le compte admintech, sur le port 2222, sans mot de passe.

Jour 3

