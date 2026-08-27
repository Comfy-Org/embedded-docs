# VaeDecodeTextureTrellis

Ce nœud décode un latent de texture Trellis2 en couleurs de voxels à l'aide d'un VAE. Le latent d'entrée contient des échantillons de caractéristiques épars avec coordonnées ; le nœud reconstruit la couleur de chaque voxel et renvoie le résultat sous forme de grille de voxels que les nœuds en aval, tels que PaintMesh, peuvent utiliser pour coloriser un maillage 3D.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `samples` | Le latent de texture à décoder. Il contient les caractéristiques des échantillons et les coordonnées éparses, et peut inclure des métadonnées facultatives telles que les compteurs de coordonnées, le repère du modèle et la résolution des coordonnées. | LATENT | Oui | — |
| `vae` | Le VAE Trellis2 utilisé pour décoder le latent de texture en couleurs de voxels. | VAE | Oui | — |
| `shape_subdivides` | Informations de forme utilisées pour guider la reconstruction à plus haute résolution pendant le décodage. Aide à préserver la cohérence de la structure aux résolutions supérieures. | SHAPE_SUBDIVIDES | Oui | — |

Remarque : Lorsque le latent `samples` inclut des compteurs de coordonnées, ces compteurs doivent être non négatifs, leur total doit correspondre au nombre de lignes de coordonnées, et chaque lot doit avoir exactement le nombre de lignes attendu ; sinon, le nœud lève une erreur. Si le repère du modèle du latent est « z_up », les coordonnées de voxels décodées sont reconfigurées en Y-up afin de s'aligner sur les sommets du maillage. Lorsqu'une résolution de coordonnées est fournie, la résolution de texture de sortie est cette valeur multipliée par 16 ; sinon, elle est déduite de la plus grande coordonnée de voxel et arrondie à la valeur supérieure parmi 256, 512, 1024, 1536 ou 2048 (1024 lorsqu'aucune coordonnée n'est disponible).

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `voxel_colors` | Données de voxels décodées contenant les coordonnées, les caractéristiques de couleur et la résolution de texture. Chaque voxel possède 6 canaux de couleur : couleur de base (RVB), métallique, rugosité et alpha, tous dans la plage [0, 1]. Les consommateurs de couleurs de sommets, tels que PaintMesh, utilisent les 3 premiers canaux. | VOXEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeTextureTrellis/fr.md)

---
**Source fingerprint (SHA-256):** `cfbe59efb18d2c3c7c597c5212900fea54d660aa98005817debf4711401a6967`
