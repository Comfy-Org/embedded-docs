Ce nœud est conçu pour encoder le texte d'entrée en utilisant un modèle CLIP spécialement adapté pour l'architecture SDXL. Il utilise un système de double encodeur (CLIP-L et CLIP-G) pour traiter les descriptions textuelles, permettant une génération d'images plus précise.

## Entrées

| Paramètre | Data Type | Description |
|-----------|-----------|-------------|
| `clip` | CLIP | Instance du modèle CLIP utilisée pour l'encodage du texte. |
| `largeur` | INT | Spécifie la largeur de l'image en pixels, par défaut 1024. |
| `hauteur` | INT | Spécifie la hauteur de l'image en pixels, par défaut 1024. |
| `crop_w` | INT | Largeur de la zone de recadrage en pixels, par défaut 0. |
| `crop_h` | INT | Hauteur de la zone de recadrage en pixels, par défaut 0. |
| `largeur_cible` | INT | Largeur cible pour l'image de sortie, par défaut 1024. |
| `hauteur_cible` | INT | Hauteur cible pour l'image de sortie, par défaut 1024. |
| `text_g` | STRING | Description textuelle globale pour la description générale de la scène. |
| `text_l` | STRING | Description textuelle locale pour les détails. |

## Sorties

| Paramètre | Data Type | Description |
|-----------|-----------|-------------|
| `CONDITIONNEMENT` | CONDITIONING | Contient le texte encodé et les informations conditionnelles nécessaires à la génération d'images. |
