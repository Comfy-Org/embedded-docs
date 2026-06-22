# CLIPTextEncodeSDXL

Ce nœud est conçu pour encoder une entrée textuelle à l'aide d'un modèle CLIP spécifiquement adapté à l'architecture SDXL. Il utilise un système à double encodeur (CLIP-L et CLIP-G) pour traiter les descriptions textuelles, ce qui permet une génération d'images plus précise.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `clip` | Instance du modèle CLIP utilisée pour l'encodage du texte. | CLIP |
| `largeur` | Spécifie la largeur de l'image en pixels, valeur par défaut 1024. | INT |
| `hauteur` | Spécifie la hauteur de l'image en pixels, valeur par défaut 1024. | INT |
| `crop_w` | Largeur de la zone de recadrage en pixels, valeur par défaut 0. | INT |
| `crop_h` | Hauteur de la zone de recadrage en pixels, valeur par défaut 0. | INT |
| `largeur_cible` | Largeur cible pour l'image de sortie, valeur par défaut 1024. | INT |
| `hauteur_cible` | Hauteur cible pour l'image de sortie, valeur par défaut 1024. | INT |
| `text_g` | Description textuelle globale pour la description générale de la scène. | STRING |
| `text_l` | Description textuelle locale pour la description des détails. | STRING |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Contient le texte encodé et les informations conditionnelles nécessaires à la génération d'images. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXL/fr.md)
