> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageQuantize/fr.md)

Le nœud ImageQuantize est conçu pour réduire le nombre de couleurs d'une image à un nombre spécifié, en appliquant éventuellement des techniques de tramage (dithering) pour préserver la qualité visuelle. Ce processus est utile pour créer des images basées sur une palette ou pour réduire la complexité chromatique dans certaines applications.

## Entrées

| Champ    | Type de données | Description                                                                                          |
|----------|-----------------|------------------------------------------------------------------------------------------------------|
| `image`  | `IMAGE`         | Le tenseur d'image d'entrée à quantifier. Il affecte l'exécution du nœud en étant la donnée principale sur laquelle la réduction des couleurs est effectuée. |
| `colors` | `INT`           | Spécifie le nombre de couleurs auquel réduire l'image. Il influence directement le processus de quantification en déterminant la taille de la palette de couleurs. |
| `dither` | COMBO[STRING]   | Détermine la technique de tramage à appliquer lors de la quantification, affectant la qualité visuelle et l'apparence de l'image de sortie. |

## Sorties

| Champ   | Type de données | Description                                                                                          |
|---------|-----------------|------------------------------------------------------------------------------------------------------|
| `image` | `IMAGE`         | La version quantifiée de l'image d'entrée, avec une complexité chromatique réduite et éventuellement tramée pour préserver la qualité visuelle. |