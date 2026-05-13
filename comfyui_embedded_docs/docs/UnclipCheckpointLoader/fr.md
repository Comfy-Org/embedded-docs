> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPCheckpointLoader/fr.md)

Ce nœud détecte les modèles situés dans le dossier `ComfyUI/models/checkpoints`, et lit également les modèles provenant de chemins supplémentaires configurés dans le fichier `extra_model_paths.yaml`. Il peut parfois être nécessaire de **rafraîchir l'interface ComfyUI** pour lui permettre de lire les fichiers de modèles depuis le dossier correspondant.

Le nœud unCLIPCheckpointLoader est conçu pour charger des points de contrôle spécifiquement adaptés aux modèles unCLIP. Il facilite la récupération et l'initialisation des modèles, des modules CLIP vision et des VAE à partir d'un point de contrôle spécifié, simplifiant ainsi le processus de configuration pour des opérations ou analyses ultérieures.

## Entrées

| Champ        | Type Comfy        | Description                                                                       |
|--------------|-------------------|-----------------------------------------------------------------------------------|
| `ckpt_name`  | `COMBO[STRING]`   | Spécifie le nom du point de contrôle à charger, identifiant et récupérant le fichier de point de contrôle correct depuis un répertoire prédéfini, déterminant l'initialisation des modèles et des configurations. |

## Sorties

| Champ         | Type Comfy    | Description                                                              | Type Python          |
|---------------|---------------|--------------------------------------------------------------------------|----------------------|
| `model`       | `MODEL`       | Représente le modèle principal chargé depuis le point de contrôle.        | `torch.nn.Module`    |
| `clip`        | `CLIP`        | Représente le module CLIP chargé depuis le point de contrôle, s'il est disponible. | `torch.nn.Module`    |
| `vae`         | `VAE`         | Représente le module VAE chargé depuis le point de contrôle, s'il est disponible.   | `torch.nn.Module`    |
| `clip_vision` | `CLIP_VISION` | Représente le module CLIP vision chargé depuis le point de contrôle, s'il est disponible. | `torch.nn.Module`    |