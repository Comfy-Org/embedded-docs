Ce nœud détectera les modèles situés dans le dossier `ComfyUI/models/checkpoints`,
et lira également les modèles des chemins supplémentaires que vous avez configurés dans le fichier extra_model_paths.yaml.
Parfois, vous devrez **rafraîchir l'interface ComfyUI** pour qu'elle puisse lire les fichiers de modèle dans le dossier correspondant.

Le nœud unCLIPCheckpointLoader est conçu pour charger des checkpoints spécifiquement adaptés aux modèles unCLIP. Il facilite la récupération et l'initialisation des modèles, des modules de vision CLIP et des VAEs à partir d'un checkpoint spécifié, simplifiant ainsi le processus de configuration pour des opérations ou analyses ultérieures.

## Entrées

| Champ      | Comfy dtype       | Description                                                                       |
|------------|-------------------|-----------------------------------------------------------------------------------|
| `ckpt_name`| `COMBO[STRING]`    | Spécifie le nom du checkpoint à charger, identifiant et récupérant le fichier de checkpoint correct à partir d'un répertoire prédéfini, déterminant l'initialisation des modèles et des configurations. |

## Sorties

| Champ       | Comfy dtype   | Description                                                              | Python dtype         |
|-------------|---------------|--------------------------------------------------------------------------|---------------------|
| `model`     | `MODEL`       | Représente le modèle principal chargé à partir du checkpoint.                   | `torch.nn.Module`   |
| `clip`      | `CLIP`        | Représente le module CLIP chargé à partir du checkpoint, si disponible.      | `torch.nn.Module`   |
| `vae`       | `VAE`         | Représente le module VAE chargé à partir du checkpoint, si disponible.        | `torch.nn.Module`   |
| `clip_vision`| `CLIP_VISION` | Représente le module de vision CLIP chargé à partir du checkpoint, si disponible.| `torch.nn.Module`   |
