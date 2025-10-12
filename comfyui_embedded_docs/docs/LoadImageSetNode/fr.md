> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetNode/fr.md)

Le LoadImageSetNode charge plusieurs images depuis le répertoire d'entrée pour le traitement par lots et l'entraînement. Il prend en charge divers formats d'image et peut optionnellement redimensionner les images en utilisant différentes méthodes. Ce nœud traite toutes les images sélectionnées comme un lot et les retourne sous forme d'un seul tenseur.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Oui | Fichiers d'images multiples | Sélectionnez plusieurs images depuis le répertoire d'entrée. Prend en charge les formats PNG, JPG, JPEG, WEBP, BMP, GIF, JPE, APNG, TIF et TIFF. Permet la sélection par lots d'images. |
| `resize_method` | STRING | Non | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | Méthode optionnelle pour redimensionner les images chargées (par défaut : "None"). Choisissez "None" pour conserver les tailles originales, "Stretch" pour forcer le redimensionnement, "Crop" pour maintenir le ratio d'aspect par recadrage, ou "Pad" pour maintenir le ratio d'aspect en ajoutant un remplissage. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Un tenseur contenant toutes les images chargées sous forme de lot pour un traitement ultérieur. |
