
Ce nœud est conçu pour appliquer un masque de bruit à un ensemble d'échantillons latents. Il modifie les échantillons d'entrée en intégrant un masque spécifié, altérant ainsi leurs caractéristiques de bruit.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | Les échantillons latents auxquels le masque de bruit sera appliqué. Ce paramètre est crucial pour déterminer le contenu de base qui sera modifié. |
| `mask`    | `MASK`      | Le masque à appliquer aux échantillons latents. Il définit les zones et l'intensité de l'altération du bruit au sein des échantillons. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Les échantillons latents modifiés avec le masque de bruit appliqué. |
