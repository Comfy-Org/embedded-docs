> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/fr.md)

Voici la traduction en français de la documentation technique du nœud ComfyUI Rodin Gen-2.5 Text :

## Aperçu

Générez un modèle 3D à partir d'une invite textuelle en utilisant l'API Rodin Gen-2.5. Vous pouvez choisir entre différents modes de qualité (Rapide, Normal ou Très élevé) pour équilibrer la vitesse de génération et la qualité du résultat.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | 2500 caractères max | Invite textuelle décrivant le modèle 3D que vous souhaitez générer. |
| `mode` | COMBO | Oui | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` | Le mode de qualité et de vitesse de génération. "Fast" est le plus rapide, "Extreme-High" produit la meilleure qualité mais prend plus de temps. |
| `material` | COMBO | Oui | `"PBR"`<br>`"Matte"`<br>`"Shiny"` | Le style de matériau pour le modèle 3D généré. |
| `geometry_file_format` | COMBO | Oui | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` | Le format de fichier pour le modèle 3D de sortie. |
| `texture_mode` | COMBO | Oui | `"None"`<br>`"Generated"`<br>`"Generated+HD"` | Mode de génération de texture. "None" ne produit aucune texture, "Generated" crée des textures standard, "Generated+HD" crée des textures haute définition. |
| `seed` | INT | Oui | 0 à 2147483647 | Graine aléatoire pour des résultats reproductibles. Utiliser la même graine avec les mêmes entrées produira la même sortie. |
| `TAPose` | BOOLEAN | Oui | Vrai / Faux | Indique s'il faut appliquer la pose en T (bras tendus) au modèle généré. |
| `hd_texture` | BOOLEAN | Oui | Vrai / Faux | Indique s'il faut générer des textures haute définition pour le modèle. |
| `texture_delight` | BOOLEAN | Oui | Vrai / Faux | Indique s'il faut appliquer un rehaussement de texture (qualité de texture améliorée) au modèle. |
| `addon_highpack` | BOOLEAN | Oui | Vrai / Faux | Indique s'il faut générer une version haute polygone du modèle en plus de la version standard. |
| `bbox_width` | INT | Oui | 1 à 1000 | La largeur de la boîte englobante en unités monde. |
| `bbox_height` | INT | Oui | 1 à 1000 | La hauteur de la boîte englobante en unités monde. |
| `bbox_length` | INT | Oui | 1 à 1000 | La longueur de la boîte englobante en unités monde. |
| `height_cm` | INT | Oui | 1 à 300 | La hauteur du modèle généré en centimètres. |

**Remarque :** Le paramètre `prompt` doit contenir entre 1 et 2500 caractères. Le paramètre `seed` est par défaut à 0 (aléatoire) s'il n'est pas spécifié.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `model_file` | FILE3DANY | Le fichier de modèle 3D généré dans le format spécifié. |

---
**Source fingerprint (SHA-256):** `79fbaf466e9af88cdfdac0f9136a2df17ba4bc2e5bb65a35b9ad2b1181da94db`
