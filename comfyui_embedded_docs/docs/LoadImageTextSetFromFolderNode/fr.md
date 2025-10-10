> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextSetFromFolderNode/fr.md)

Charge un lot d'images et leurs légendes textuelles correspondantes à partir d'un répertoire spécifié à des fins d'entraînement. Le nœud recherche automatiquement les fichiers image et leurs fichiers texte de légende associés, traite les images selon les paramètres de redimensionnement spécifiés et encode les légendes en utilisant le modèle CLIP fourni.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | Oui | - | Le dossier à partir duquel charger les images. |
| `clip` | CLIP | Oui | - | Le modèle CLIP utilisé pour encoder le texte. |
| `resize_method` | COMBO | Non | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | La méthode utilisée pour redimensionner les images (par défaut : "None"). |
| `width` | INT | Non | -1 à 10000 | La largeur à laquelle redimensionner les images. -1 signifie utiliser la largeur originale (par défaut : -1). |
| `height` | INT | Non | -1 à 10000 | La hauteur à laquelle redimensionner les images. -1 signifie utiliser la hauteur originale (par défaut : -1). |

**Note :** L'entrée CLIP doit être valide et ne peut pas être None. Si le modèle CLIP provient d'un nœud de chargeur de checkpoint, assurez-vous que le checkpoint contient un modèle CLIP ou un encodeur de texte valide.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Le lot d'images chargées et traitées. |
| `CONDITIONING` | CONDITIONING | Les données de conditionnement encodées à partir des légendes textuelles. |