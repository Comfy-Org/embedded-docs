> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscale/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI `LatentUpscale` :

Le nœud LatentUpscale est conçu pour le suréchantillonnage des représentations latentes d'images. Il permet d'ajuster les dimensions de l'image de sortie ainsi que la méthode de suréchantillonnage, offrant une flexibilité pour améliorer la résolution des images latentes.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `samples` | `LATENT`        | La représentation latente d'une image à suréchantillonner. Ce paramètre est crucial pour déterminer le point de départ du processus de suréchantillonnage. |
| `upscale_method` | COMBO[STRING] | Spécifie la méthode utilisée pour suréchantillonner l'image latente. Différentes méthodes peuvent affecter la qualité et les caractéristiques de l'image suréchantillonnée. |
| `width`   | `INT`           | La largeur souhaitée de l'image suréchantillonnée. Si définie sur 0, elle sera calculée en fonction de la hauteur pour conserver le rapport hauteur/largeur. |
| `height`  | `INT`           | La hauteur souhaitée de l'image suréchantillonnée. Si définie sur 0, elle sera calculée en fonction de la largeur pour conserver le rapport hauteur/largeur. |
| `crop`    | COMBO[STRING]   | Détermine comment l'image suréchantillonnée doit être recadrée, affectant l'apparence finale et les dimensions de la sortie. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `latent`  | `LATENT`        | La représentation latente suréchantillonnée de l'image, prête pour un traitement ou une génération ultérieure. |