# Rodin 3D Gen-2.5 - Texte vers 3D

## Aperçu

Générez un modèle 3D à partir d’un texte d’invite à l’aide de l’API Rodin Gen-2.5. Vous pouvez choisir entre différents modes de qualité (« Fast », « Regular » ou « Extreme-High ») pour équilibrer la vitesse de génération et la qualité de sortie.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `prompt` | Texte d’invite pour le modèle 3D. | STRING | Oui | 1 à 1024 caractères |
| `mode` | Le mode de qualité et de vitesse de génération. « Fast » est le plus rapide, « Extreme-High » produit la qualité la plus élevée mais prend plus de temps. | COMBO | Oui | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` |
| `material` | Le style de matériau du modèle 3D généré. | COMBO | Oui | `"PBR"`<br>`"Matte"`<br>`"Shiny"` |
| `geometry_file_format` | Le format de fichier du modèle 3D de sortie. | COMBO | Oui | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` |
| `texture_mode` | Mode de génération des textures. « None » ne produit aucune texture, « Generated » crée des textures standard, « Generated+HD » crée des textures haute définition. | COMBO | Oui | `"None"`<br>`"Generated"`<br>`"Generated+HD"` |
| `seed` | Graine aléatoire pour des résultats reproductibles. Utiliser la même graine avec les mêmes entrées produira la même sortie. | INT | Oui | 0 à 2147483647 |
| `TAPose` | Indique s’il faut appliquer la pose en T (bras tendus) au modèle généré. | BOOLEAN | Oui | True / False |
| `hd_texture` | Indique s’il faut générer des textures haute définition pour le modèle. | BOOLEAN | Oui | True / False |
| `texture_delight` | Indique s’il faut appliquer le rehaussement de texture (qualité de texture améliorée) au modèle. | BOOLEAN | Oui | True / False |
| `addon_highpack` | Indique s’il faut générer une version à haute densité de polygones du modèle en plus de la version standard. | BOOLEAN | Oui | True / False |
| `bbox_width` | La largeur de la boîte englobante en unités de monde. | INT | Oui | 1 à 1000 |
| `bbox_height` | La hauteur de la boîte englobante en unités de monde. | INT | Oui | 1 à 1000 |
| `bbox_length` | La longueur de la boîte englobante en unités de monde. | INT | Oui | 1 à 1000 |
| `height_cm` | La hauteur du modèle généré en centimètres. | INT | Oui | 1 à 300 |

**Remarque :** Le paramètre `prompt` doit comporter entre 1 et 1024 caractères. Le paramètre `seed` vaut 0 (aléatoire) par défaut s’il n’est pas spécifié.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `fichier_modèle` | Le fichier de modèle 3D généré dans le format spécifié. | FILE3DANY |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/fr.md)

---
**Source fingerprint (SHA-256):** `95d5faa36298f09f0ae4dcda95dfd8913ebb393bb5934ae2c4622acfe79c85d6`
