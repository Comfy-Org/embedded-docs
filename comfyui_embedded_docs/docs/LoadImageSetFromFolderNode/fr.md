Le nœud LoadImageSetFromFolderNode charge plusieurs images depuis un dossier spécifié à des fins d’entraînement. Il détecte automatiquement les formats d’image courants et peut éventuellement redimensionner les images selon différentes méthodes avant de les retourner sous forme de lot.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `folder` | Le dossier à partir duquel charger les images. | STRING | Oui | Plusieurs options disponibles |
| `resize_method` | La méthode à utiliser pour redimensionner les images (par défaut : "None"). | STRING | Non | "None"<br>"Stretch"<br>"Crop"<br>"Pad" |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | Le lot d’images chargées sous forme d’un seul tenseur. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/fr.md)

---
**Source fingerprint (SHA-256):** `46fcfbf6a2ad95e707e32e54ed7b4c06bfd1cc290df122042187689f41bed828`
