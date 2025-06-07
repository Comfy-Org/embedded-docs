Ce nœud détectera les modèles situés dans le dossier `ComfyUI/models/upscale_models`,
et lira également les modèles des chemins supplémentaires que vous avez configurés dans le fichier extra_model_paths.yaml.
Parfois, vous devrez **rafraîchir l'interface ComfyUI** pour qu'elle puisse lire les fichiers de modèle dans le dossier correspondant.

Le nœud UpscaleModelLoader est conçu pour charger des modèles d'agrandissement à partir d'un répertoire spécifié. Il facilite la récupération et la préparation des modèles d'agrandissement pour les tâches d'agrandissement d'image, garantissant que les modèles sont correctement chargés et configurés pour l'évaluation.

## Entrées

| Champ          | Comfy dtype       | Description                                                                       |
|----------------|-------------------|-----------------------------------------------------------------------------------|
| `model_name`   | `COMBO[STRING]`    | Spécifie le nom du modèle d'agrandissement à charger, identifiant et récupérant le fichier de modèle correct dans le répertoire des modèles d'agrandissement. |

## Sorties

| Champ            | Comfy dtype         | Description                                                              |
|-------------------|---------------------|--------------------------------------------------------------------------|
| `upscale_model`  | `UPSCALE_MODEL`     | Retourne le modèle d'agrandissement chargé et préparé, prêt à être utilisé dans les tâches d'agrandissement d'image. |
