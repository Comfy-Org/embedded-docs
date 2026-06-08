Le nœud `ExponentialScheduler` est conçu pour générer une séquence de valeurs sigma suivant un programme exponentiel pour les processus d'échantillonnage par diffusion. Il offre une approche personnalisable pour contrôler les niveaux de bruit appliqués à chaque étape du processus de diffusion, permettant un réglage fin du comportement d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `étapes` | Spécifie le nombre d'étapes dans le processus de diffusion. Il influence la longueur de la séquence sigma générée et donc la granularité de l'application du bruit. | INT |
| `sigma_max` | Définit la valeur sigma maximale, fixant la limite supérieure de l'intensité du bruit dans le processus de diffusion. Il joue un rôle crucial dans la détermination de la plage des niveaux de bruit appliqués. | FLOAT |
| `sigma_min` | Définit la valeur sigma minimale, établissant la limite inférieure de l'intensité du bruit. Ce paramètre permet d'affiner le point de départ de l'application du bruit. | FLOAT |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `sigmas` | Une séquence de valeurs sigma générées selon le programme exponentiel. Ces valeurs sont utilisées pour contrôler les niveaux de bruit à chaque étape du processus de diffusion. | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExponentialScheduler/fr.md)
