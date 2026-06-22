# Mise à l'échelle Latente

Voici la traduction en français de la documentation du nœud ComfyUI `LatentUpscale` :

Le nœud LatentUpscale est conçu pour le suréchantillonnage des représentations latentes d'images. Il permet d'ajuster les dimensions de l'image de sortie ainsi que la méthode de suréchantillonnage, offrant une flexibilité pour améliorer la résolution des images latentes.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `samples` | La représentation latente d'une image à suréchantillonner. Ce paramètre est crucial pour déterminer le point de départ du processus de suréchantillonnage. | `LATENT` |
| `méthode_de_mise_à_l'échelle` | Spécifie la méthode utilisée pour suréchantillonner l'image latente. Différentes méthodes peuvent affecter la qualité et les caractéristiques de l'image suréchantillonnée. | COMBO[STRING] |
| `largeur` | La largeur souhaitée de l'image suréchantillonnée. Si définie sur 0, elle sera calculée en fonction de la hauteur pour conserver le rapport hauteur/largeur. | `INT` |
| `hauteur` | La hauteur souhaitée de l'image suréchantillonnée. Si définie sur 0, elle sera calculée en fonction de la largeur pour conserver le rapport hauteur/largeur. | `INT` |
| `recadrage` | Détermine comment l'image suréchantillonnée doit être recadrée, affectant l'apparence finale et les dimensions de la sortie. | COMBO[STRING] |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `latent` | La représentation latente suréchantillonnée de l'image, prête pour un traitement ou une génération ultérieure. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscale/fr.md)
