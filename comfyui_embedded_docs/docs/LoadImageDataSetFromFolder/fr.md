> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/fr.md)

Ce nœud charge plusieurs images à partir d'un sous-dossier spécifié dans le répertoire d'entrée de ComfyUI. Il parcourt le dossier choisi à la recherche des types de fichiers image courants et les renvoie sous forme de liste, ce qui le rend utile pour le traitement par lots ou la préparation de jeux de données.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | Oui | *Plusieurs options disponibles* | Le dossier à partir duquel charger les images. Les options correspondent aux sous-dossiers présents dans le répertoire d'entrée principal de ComfyUI. |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `images` | IMAGE | Liste des images chargées. Le nœud charge tous les fichiers image valides (PNG, JPG, JPEG, WEBP) trouvés dans le dossier sélectionné. |
