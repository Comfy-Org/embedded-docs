Ce nœud détectera les modèles situés dans le dossier `ComfyUI/models/clip_vision`, et lira également les modèles des chemins supplémentaires que vous avez configurés dans le fichier extra_model_paths.yaml. Parfois, vous devrez **rafraîchir l'interface ComfyUI** pour qu'elle puisse lire les fichiers de modèle dans le dossier correspondant.

Le nœud CLIPVisionLoader est conçu pour charger les modèles CLIP Vision à partir de chemins spécifiés. Il simplifie la complexité de localisation et d'initialisation des modèles CLIP Vision, les rendant facilement disponibles pour des tâches de traitement ou d'inférence ultérieures.

## Entrées

| Champ       | Data Type | Description                                                                       |
|-------------|-------------|-----------------------------------------------------------------------------------|
| `clip_name` | COMBO[STRING] | Spécifie le nom du modèle CLIP Vision à charger, utilisé pour localiser le fichier du modèle dans une structure de répertoire prédéfinie. |

## Sorties

| Champ          | Comfy dtype     | Description                                                              |
|----------------|-----------------|--------------------------------------------------------------------------|
| `clip_vision`  | `CLIP_VISION`   | Le modèle CLIP Vision chargé, prêt à être utilisé pour encoder des images ou effectuer d'autres tâches liées à la vision. |
