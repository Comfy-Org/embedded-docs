
Le nœud LatentRotate est conçu pour faire pivoter les représentations latentes des images selon des angles spécifiés. Il simplifie la complexité de la manipulation de l'espace latent pour obtenir des effets de rotation, permettant aux utilisateurs de transformer facilement les images dans l'espace latent d'un modèle génératif.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | Le paramètre 'samples' représente les représentations latentes des images à faire pivoter. Il est crucial pour déterminer le point de départ de l'opération de rotation. |
| `rotation` | COMBO[STRING] | Le paramètre 'rotation' spécifie l'angle selon lequel les images latentes doivent être pivotées. Il influence directement l'orientation des images résultantes. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La sortie est une version modifiée des représentations latentes d'entrée, pivotée selon l'angle spécifié. |
