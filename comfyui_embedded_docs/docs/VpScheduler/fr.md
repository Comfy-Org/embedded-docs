# PlanificateurVP

Le nœud VPScheduler est conçu pour générer une séquence de niveaux de bruit (sigmas) basée sur la méthode de planification à préservation de variance (VP). Cette séquence est cruciale pour guider le processus de débruitage dans les modèles de diffusion, permettant une génération contrôlée d'images ou d'autres types de données.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `étapes` | Spécifie le nombre d'étapes dans le processus de diffusion, affectant la granularité des niveaux de bruit générés. | INT |
| `beta_d` | Détermine la distribution globale des niveaux de bruit, influençant la variance des niveaux de bruit générés. | FLOAT |
| `beta_min` | Définit la limite minimale pour le niveau de bruit, garantissant que le bruit ne descend pas en dessous d'un certain seuil. | FLOAT |
| `eps_s` | Ajuste la valeur epsilon de départ, permettant un réglage fin du niveau de bruit initial dans le processus de diffusion. | FLOAT |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `sigmas` | Une séquence de niveaux de bruit (sigmas) générée selon la méthode de planification VP, utilisée pour guider le processus de débruitage dans les modèles de diffusion. | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VPScheduler/fr.md)
