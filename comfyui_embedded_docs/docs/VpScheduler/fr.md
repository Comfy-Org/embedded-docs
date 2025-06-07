
Le nœud VPScheduler est conçu pour générer une séquence de niveaux de bruit (sigmas) basée sur la méthode de planification à préservation de variance (VP). Cette séquence est cruciale pour guider le processus de débruitage dans les modèles de diffusion, permettant une génération contrôlée d'images ou d'autres types de données.

## Entrées

| Paramètre   | Data Type | Description                                                                                                                                      |
|-------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `steps`     | INT         | Spécifie le nombre d'étapes dans le processus de diffusion, affectant la granularité des niveaux de bruit générés.                              |
| `beta_d`    | FLOAT       | Détermine la distribution globale du niveau de bruit, influençant la variance des niveaux de bruit générés.                                 |
| `beta_min`  | FLOAT       | Définit la limite minimale pour le niveau de bruit, garantissant que le bruit ne descend pas en dessous d'un certain seuil.                              |
| `eps_s`     | FLOAT       | Ajuste la valeur epsilon de départ, affinant le niveau de bruit initial dans le processus de diffusion.                                    |

## Sorties

| Paramètre   | Data Type | Description                                                                                   |
|-------------|-------------|-----------------------------------------------------------------------------------------------|
| `sigmas`    | SIGMAS      | Une séquence de niveaux de bruit (sigmas) générée selon la méthode de planification VP, utilisée pour guider le processus de débruitage dans les modèles de diffusion. |
