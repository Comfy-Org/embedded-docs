> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXL/fr.md)

Ce nœud est conçu pour encoder une entrée textuelle à l'aide d'un modèle CLIP spécifiquement adapté à l'architecture SDXL. Il utilise un système à double encodeur (CLIP-L et CLIP-G) pour traiter les descriptions textuelles, ce qui permet une génération d'images plus précise.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `clip` | CLIP | Instance du modèle CLIP utilisée pour l'encodage du texte. |
| `largeur` | INT | Spécifie la largeur de l'image en pixels, valeur par défaut 1024. |
| `hauteur` | INT | Spécifie la hauteur de l'image en pixels, valeur par défaut 1024. |
| `crop_w` | INT | Largeur de la zone de recadrage en pixels, valeur par défaut 0. |
| `crop_h` | INT | Hauteur de la zone de recadrage en pixels, valeur par défaut 0. |
| `largeur_cible` | INT | Largeur cible pour l'image de sortie, valeur par défaut 1024. |
| `hauteur_cible` | INT | Hauteur cible pour l'image de sortie, valeur par défaut 1024. |
| `text_g` | STRING | Description textuelle globale pour la description générale de la scène. |
| `text_l` | STRING | Description textuelle locale pour la description des détails. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `CONDITIONING` | CONDITIONING | Contient le texte encodé et les informations conditionnelles nécessaires à la génération d'images. |