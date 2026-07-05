# Rodin 3D Gen-2.5 - Texte vers 3D

Voici la traduction en français de la documentation technique du nœud ComfyUI Rodin Gen-2.5 Text :

## Aperçu

Générez un modèle 3D à partir d'une invite textuelle en utilisant l'API Rodin Gen-2.5. Vous pouvez choisir entre différents modes de qualité (Rapide, Normal ou Très élevé) pour équilibrer la vitesse de génération et la qualité du résultat.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Invite textuelle décrivant le modèle 3D que vous souhaitez générer. | STRING | Oui | 2500 caractères max |
| `mode` | Le mode de qualité et de vitesse de génération. "Fast" est le plus rapide, "Extreme-High" produit la meilleure qualité mais prend plus de temps. | COMBO | Oui | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` |
| `material` | Le style de matériau pour le modèle 3D généré. | COMBO | Oui | `"PBR"`<br>`"Matte"`<br>`"Shiny"` |
| `geometry_file_format` | Le format de fichier pour le modèle 3D de sortie. | COMBO | Oui | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` |
| `texture_mode` | Mode de génération de texture. "None" ne produit aucune texture, "Generated" crée des textures standard, "Generated+HD" crée des textures haute définition. | COMBO | Oui | `"None"`<br>`"Generated"`<br>`"Generated+HD"` |
| `seed` | Graine aléatoire pour des résultats reproductibles. Utiliser la même graine avec les mêmes entrées produira la même sortie. | INT | Oui | 0 à 2147483647 |
| `TAPose` | Indique s'il faut appliquer la pose en T (bras tendus) au modèle généré. | BOOLEAN | Oui | Vrai / Faux |
| `hd_texture` | Indique s'il faut générer des textures haute définition pour le modèle. | BOOLEAN | Oui | Vrai / Faux |
| `texture_delight` | Indique s'il faut appliquer un rehaussement de texture (qualité de texture améliorée) au modèle. | BOOLEAN | Oui | Vrai / Faux |
| `addon_highpack` | Indique s'il faut générer une version haute polygone du modèle en plus de la version standard. | BOOLEAN | Oui | Vrai / Faux |
| `bbox_width` | La largeur de la boîte englobante en unités monde. | INT | Oui | 1 à 1000 |
| `bbox_height` | La hauteur de la boîte englobante en unités monde. | INT | Oui | 1 à 1000 |
| `bbox_length` | La longueur de la boîte englobante en unités monde. | INT | Oui | 1 à 1000 |
| `height_cm` | La hauteur du modèle généré en centimètres. | INT | Oui | 1 à 300 |

**Remarque :** Le paramètre `prompt` doit contenir entre 1 et 2500 caractères. Le paramètre `seed` est par défaut à 0 (aléatoire) s'il n'est pas spécifié.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `fichier_modèle` | Le fichier de modèle 3D généré dans le format spécifié. | FILE3DANY |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/fr.md)

---
**Source fingerprint (SHA-256):** `79fbaf466e9af88cdfdac0f9136a2df17ba4bc2e5bb65a35b9ad2b1181da94db`
