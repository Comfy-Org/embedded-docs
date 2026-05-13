> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentRotate/fr.md)

Voici la traduction en français de la documentation du nœud LatentRotate :

Le nœud LatentRotate est conçu pour faire pivoter les représentations latentes d'images selon des angles spécifiés. Il abstrait la complexité de la manipulation de l'espace latent pour obtenir des effets de rotation, permettant aux utilisateurs de transformer facilement des images dans l'espace latent d'un modèle génératif.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `samples` | `LATENT`        | Le paramètre 'samples' représente les représentations latentes des images à faire pivoter. Il est crucial pour déterminer le point de départ de l'opération de rotation. |
| `rotation` | COMBO[STRING]  | Le paramètre 'rotation' spécifie l'angle selon lequel les images latentes doivent être pivotées. Il influence directement l'orientation des images résultantes. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `latent`  | `LATENT`        | La sortie est une version modifiée des représentations latentes d'entrée, pivotées selon l'angle spécifié. |