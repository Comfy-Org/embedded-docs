> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCrop/fr.md)

Le nœud LatentCrop est conçu pour effectuer des opérations de recadrage sur les représentations latentes des images. Il permet de spécifier les dimensions et la position du recadrage, offrant ainsi des modifications ciblées de l'espace latent.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `échantillons` | `LATENT`        | Le paramètre `échantillons` représente les représentations latentes à recadrer. Il est essentiel pour définir les données sur lesquelles l'opération de recadrage sera effectuée. |
| `largeur`   | `INT`           | Spécifie la largeur de la zone de recadrage. Il influence directement les dimensions de la représentation latente de sortie. |
| `hauteur`  | `INT`           | Spécifie la hauteur de la zone de recadrage, affectant la taille de la représentation latente recadrée résultante. |
| `x`       | `INT`           | Détermine la coordonnée x de départ de la zone de recadrage, influençant la position du recadrage dans la représentation latente d'origine. |
| `y`       | `INT`           | Détermine la coordonnée y de départ de la zone de recadrage, définissant la position du recadrage dans la représentation latente d'origine. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `latent`  | `LATENT`        | La sortie est une représentation latente modifiée à laquelle le recadrage spécifié a été appliqué. |