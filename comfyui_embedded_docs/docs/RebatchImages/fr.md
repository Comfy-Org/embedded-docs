> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchImages/fr.md)

Le nœud RebatchImages est conçu pour réorganiser un lot d'images en une nouvelle configuration de lot, en ajustant la taille du lot selon les spécifications. Ce processus est essentiel pour gérer et optimiser le traitement des données d'image dans les opérations par lots, garantissant que les images sont regroupées selon la taille de lot souhaitée pour un traitement efficace.

## Entrées

| Champ        | Type de données | Description                                                                         |
|--------------|-----------------|-------------------------------------------------------------------------------------|
| `images`     | `IMAGE`         | Une liste d'images à réorganiser en lots. Ce paramètre est crucial pour déterminer les données d'entrée qui subiront le processus de réorganisation. |
| `batch_size` | `INT`           | Spécifie la taille souhaitée des lots de sortie. Ce paramètre influence directement la manière dont les images d'entrée sont regroupées et traitées, impactant la structure de la sortie. |

## Sorties

| Champ   | Type de données | Description                                                                   |
|---------|-----------------|-------------------------------------------------------------------------------|
| `image` | `IMAGE`         | La sortie consiste en une liste de lots d'images, réorganisés selon la taille de lot spécifiée. Cela permet un traitement flexible et efficace des données d'image dans les opérations par lots. |