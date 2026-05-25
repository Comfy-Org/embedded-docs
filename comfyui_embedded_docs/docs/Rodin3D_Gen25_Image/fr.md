> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Image/fr.md)

Voici la traduction en français de la documentation technique du nœud ComfyUI :

## Aperçu

Ce nœud génère un modèle 3D à partir d'une à cinq images de référence en utilisant l'API Rodin Gen-2.5. Vous pouvez choisir entre les modes de qualité Rapide, Standard ou Extrême-Haute pour équilibrer la vitesse de génération et le coût.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `images` | IMAGE | Oui | 1 à 5 images | Une à cinq images d'entrée. La première image est utilisée pour les matériaux lorsque plusieurs images sont fournies. |
| `mode` | COMBO | Oui | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` | Le mode de qualité de génération. Les modes de qualité supérieure produisent de meilleurs résultats mais coûtent plus cher. |
| `material` | COMBO | Oui | `"PBR"`<br>`"Matte"` | Le type de matériau pour le modèle 3D généré. |
| `geometry_file_format` | COMBO | Oui | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` | Le format de fichier de sortie pour la géométrie du modèle 3D. |
| `texture_mode` | COMBO | Oui | `"Original"`<br>`"Clean"`<br>`"Style"` | Le mode de génération de texture. "Original" préserve les textures d'entrée, "Clean" les supprime et "Style" applique une texture stylisée. |
| `seed` | INT | Oui | 0 à 2147483647 | Une graine aléatoire pour des résultats reproductibles. Utilisez la même graine pour obtenir la même sortie. |
| `TAPose` | BOOLEAN | Oui | Vrai / Faux | Indique si la pose en T doit être appliquée au modèle généré. |
| `hd_texture` | BOOLEAN | Oui | Vrai / Faux | Indique s'il faut générer une carte de texture haute définition. |
| `texture_delight` | BOOLEAN | Oui | Vrai / Faux | Indique s'il faut supprimer l'éclairage des images d'entrée avant la génération de la texture. |
| `use_original_alpha` | BOOLEAN | Oui | Vrai / Faux | Indique s'il faut utiliser le canal alpha d'origine des images d'entrée. |
| `addon_highpack` | BOOLEAN | Oui | Vrai / Faux | Indique s'il faut générer une version haute polygone du modèle en plus de la version standard. |
| `bbox_width` | INT | Oui | 1 à 1000 | La largeur de la boîte englobante du modèle généré en centimètres. |
| `bbox_height` | INT | Oui | 1 à 1000 | La hauteur de la boîte englobante du modèle généré en centimètres. |
| `bbox_length` | INT | Oui | 1 à 1000 | La longueur de la boîte englobante du modèle généré en centimètres. |
| `height_cm` | INT | Oui | 1 à 300 | La hauteur du modèle généré en centimètres. |

**Remarque sur le nombre d'images :** Le nœud accepte entre 1 et 5 images. Si vous fournissez un lot d'images (par exemple, un lot de 4 images), chaque image du lot est traitée comme une image d'entrée distincte. Fournir plus de 5 images entraînera une erreur.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `model_file` | FILE3D | Le fichier du modèle 3D généré dans le format de géométrie sélectionné. |

---
**Source fingerprint (SHA-256):** `65f755a2c3bd2317eb61c4681a406b51b06f960e36864d3602c3d03a44aa4878`
