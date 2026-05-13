> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UpscaleModelLoader/fr.md)

Ce nœud détecte les modèles situés dans le dossier `ComfyUI/models/upscale_models`, et il lira également les modèles à partir de chemins supplémentaires configurés dans le fichier extra_model_paths.yaml. Il peut parfois être nécessaire d'**actualiser l'interface ComfyUI** pour lui permettre de lire les fichiers de modèles depuis le dossier correspondant.

Le nœud UpscaleModelLoader est conçu pour charger des modèles de suréchantillonnage à partir d'un répertoire spécifié. Il facilite la récupération et la préparation des modèles de suréchantillonnage pour les tâches d'agrandissement d'image, garantissant que les modèles sont correctement chargés et configurés pour l'évaluation.

## Entrées

| Champ          | Type Comfy         | Description                                                                       |
|----------------|-------------------|-----------------------------------------------------------------------------------|
| `nom_du_modèle`   | `COMBO[STRING]`    | Spécifie le nom du modèle de suréchantillonnage à charger, identifiant et récupérant le fichier de modèle correct depuis le répertoire des modèles de suréchantillonnage. |

## Sorties

| Champ            | Type Comfy         | Description                                                              |
|-------------------|---------------------|--------------------------------------------------------------------------|
| `upscale_model`  | `UPSCALE_MODEL`     | Renvoie le modèle de suréchantillonnage chargé et préparé, prêt à être utilisé dans les tâches d'agrandissement d'image. |