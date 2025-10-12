> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/fr.md)

Le nœud LoadImageSetFromFolderNode charge plusieurs images à partir d'un dossier spécifié à des fins d'entraînement. Il détecte automatiquement les formats d'image courants et peut optionnellement redimensionner les images en utilisant différentes méthodes avant de les retourner sous forme de lot.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | Oui | Plusieurs options disponibles | Le dossier à partir duquel charger les images. |
| `resize_method` | STRING | Non | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | La méthode à utiliser pour redimensionner les images (par défaut : "None"). |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Le lot d'images chargées sous forme de tenseur unique. |
