> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextSetFromFolderNode/fr.md)

Voici la traduction de la documentation du nœud ComfyUI :

Charge un lot d'images et leurs légendes textuelles correspondantes depuis un répertoire spécifié à des fins d'entraînement. Le nœud recherche automatiquement les fichiers image et leurs fichiers de légende texte associés, traite les images selon les paramètres de redimensionnement spécifiés, et encode les légendes à l'aide du modèle CLIP fourni.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `folder` | STRING | Oui | - | Le dossier à partir duquel charger les images. |
| `clip` | CLIP | Oui | - | Le modèle CLIP utilisé pour encoder le texte. |
| `resize_method` | COMBO | Non | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | La méthode utilisée pour redimensionner les images (par défaut : "None"). |
| `width` | INT | Non | -1 à 10000 | La largeur à laquelle redimensionner les images. -1 signifie utiliser la largeur d'origine (par défaut : -1). |
| `height` | INT | Non | -1 à 10000 | La hauteur à laquelle redimensionner les images. -1 signifie utiliser la hauteur d'origine (par défaut : -1). |

**Remarque :** L'entrée CLIP doit être valide et ne peut pas être None. Si le modèle CLIP provient d'un nœud de chargeur de point de contrôle, assurez-vous que le point de contrôle contient un modèle CLIP ou un encodeur de texte valide.

**Remarque sur la structure des dossiers :** Le nœud prend en charge la structure de dossiers kohya-ss/sd-scripts. Si le nom d'un sous-dossier commence par un nombre suivi d'un tiret bas (par exemple, `5_myclass`), ce nombre est utilisé comme un compteur de répétition, et les images contenues dans ce sous-dossier seront chargées autant de fois.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `IMAGE` | IMAGE | Le lot d'images chargées et traitées. |
| `CONDITIONING` | CONDITIONING | Les données de conditionnement encodées provenant des légendes textuelles. |

---
**Source fingerprint (SHA-256):** `ffd6399783fc281a58bae811112d9ecacb51ab8ea3b512befa9b9fab2c6860de`
