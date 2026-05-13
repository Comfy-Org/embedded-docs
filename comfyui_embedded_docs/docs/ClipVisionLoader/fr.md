> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionLoader/fr.md)

Ce nœud détecte automatiquement les modèles situés dans le dossier `ComfyUI/models/clip_vision`, ainsi que tous les chemins de modèles supplémentaires configurés dans le fichier `extra_model_paths.yaml`. Si vous ajoutez des modèles après avoir démarré ComfyUI, veuillez **actualiser l'interface ComfyUI** pour garantir que les fichiers de modèles les plus récents soient listés.

## Entrées

| Champ        | Type de données | Description |
|-------------|-----------------|-------------|
| `nom_clip` | COMBO[STRING]   | Liste tous les fichiers de modèles pris en charge dans le dossier `ComfyUI/models/clip_vision`. |

## Sorties

| Champ          | Type de données | Description |
|---------------|-----------------|-------------|
| `clip_vision`  | CLIP_VISION     | Modèle CLIP Vision chargé, prêt pour l'encodage d'images ou d'autres tâches liées à la vision. |