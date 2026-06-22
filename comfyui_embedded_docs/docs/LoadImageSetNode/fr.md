# LoadImageSetNode

Le nœud LoadImageSetNode charge plusieurs images depuis le répertoire d'entrée pour le traitement par lots et l'entraînement. Il prend en charge divers formats d'image et peut éventuellement redimensionner les images à l'aide de différentes méthodes. Ce nœud traite toutes les images sélectionnées sous forme de lot et les renvoie sous forme d'un seul tenseur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Sélectionnez plusieurs images dans le répertoire d'entrée. Prend en charge les formats PNG, JPG, JPEG, WEBP, BMP, GIF, JPE, APNG, TIF et TIFF. Permet la sélection par lots d'images. | IMAGE | Oui | Plusieurs fichiers image |
| `resize_method` | Méthode facultative pour redimensionner les images chargées (par défaut : "None"). Choisissez "None" pour conserver les tailles d'origine, "Stretch" pour forcer le redimensionnement, "Crop" pour conserver le rapport hauteur/largeur en recadrant, ou "Pad" pour conserver le rapport hauteur/largeur en ajoutant des marges. | STRING | Non | "None"<br>"Stretch"<br>"Crop"<br>"Pad" |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | Un tenseur contenant toutes les images chargées sous forme de lot pour un traitement ultérieur. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetNode/fr.md)

---
**Source fingerprint (SHA-256):** `acf0255bcf170ef3ac3b86a3f3e060c3b81064ca8924918a026ec8e3b86f7ac0`
