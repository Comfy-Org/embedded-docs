# VaeDecodeTextureTrellis

Ce nœud décode un latent de texture Trellis2 en couleurs de voxels à l’aide d’un VAE. Le latent d’entrée contient des échantillons de caractéristiques épars avec leurs coordonnées ; le nœud reconstruit la couleur de chaque voxel et renvoie le résultat sous forme de grille de voxels que les nœuds en aval, tels que PaintMesh, peuvent utiliser pour colorer un maillage 3D.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `samples` | Le latent de texture à décoder. Il contient les caractéristiques d’échantillons et les coordonnées éparses, et peut inclure des métadonnées facultatives telles que les nombres de coordonnées (`coord_counts`), le repère du modèle (`model_frame`, par défaut : "y_up") et la résolution des coordonnées (`coord_resolution`). | LATENT | Oui | — |
| `vae` | Le VAE Trellis2 utilisé pour décoder le latent de texture en couleurs de voxels. | VAE | Oui | — |
| `shape_subdivides` | Informations de forme utilisées pour guider une reconstruction plus détaillée pendant le décodage. Aide à préserver la cohérence de structure à des résolutions plus élevées. | SHAPE_SUBDIVIDES | Oui | — |

Remarque : Lorsque le latent `samples` inclut `coord_counts`, les nombres doivent être non négatifs, leur total doit correspondre au nombre de lignes de coordonnées, et chaque lot doit contenir exactement le nombre de lignes attendu ; sinon, le nœud lève une erreur. Si le `model_frame` du latent est "z_up", les coordonnées de voxels décodées sont remappées en Y-up afin de s’aligner sur les sommets du maillage. Lorsque `coord_resolution` est fourni, la résolution de texture de sortie est cette valeur multipliée par 16. Sinon, elle est déduite de la plus grande coordonnée de voxel plus un, arrondie vers le haut à l’une des valeurs 256, 512, 1024, 1536 ou 2048 ; si la valeur nécessaire dépasse 2048, cette valeur plus grande est utilisée. Si aucune coordonnée n’est disponible, la résolution par défaut est 1024.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `voxel_colors` | Données de voxels décodées contenant des coordonnées, des caractéristiques de couleur et la résolution de texture. Chaque voxel possède 6 canaux de couleur : couleur de base (RGB), métallique, rugosité et alpha, tous dans l’intervalle [0, 1]. Les consommateurs de couleurs de sommets tels que PaintMesh utilisent les 3 premiers canaux. | VOXEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeTextureTrellis/fr.md)

---
**Source fingerprint (SHA-256):** `952ea7d7a0147519392bebe352a0da731462db278c8640fa527aa5b6f64e4aa7`
