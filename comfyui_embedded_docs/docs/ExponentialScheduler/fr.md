Le nœud `ExponentialScheduler` est conçu pour générer une séquence de valeurs sigma suivant un plan exponentiel pour les processus d'échantillonnage par diffusion. Il offre une approche personnalisable pour contrôler les niveaux de bruit appliqués à chaque étape du processus de diffusion, permettant un ajustement précis du comportement d'échantillonnage.

## Entrées

| Paramètre   | Data Type | Description                                                                                   |
|-------------|-------------|---------------------------------------------------------------------------------------------|
| `steps`     | INT         | Spécifie le nombre d'étapes dans le processus de diffusion. Il influence la longueur de la séquence sigma générée et donc la granularité de l'application du bruit. |
| `sigma_max` | FLOAT       | Définit la valeur sigma maximale, fixant la limite supérieure de l'intensité du bruit dans le processus de diffusion. Il joue un rôle crucial dans la détermination de la gamme des niveaux de bruit appliqués. |
| `sigma_min` | FLOAT       | Définit la valeur sigma minimale, établissant la limite inférieure de l'intensité du bruit. Ce paramètre aide à ajuster précisément le point de départ de l'application du bruit. |

## Sorties

| Paramètre | Data Type | Description                                                                                   |
|-----------|-------------|---------------------------------------------------------------------------------------------|
| `sigmas`  | SIGMAS      | Une séquence de valeurs sigma générées selon le plan exponentiel. Ces valeurs sont utilisées pour contrôler les niveaux de bruit à chaque étape du processus de diffusion. |
