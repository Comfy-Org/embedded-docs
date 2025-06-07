Ce nœud détectera les modèles situés dans le dossier `ComfyUI/models/loras`,
et lira également les modèles des chemins supplémentaires que vous avez configurés dans le fichier extra_model_paths.yaml.
Parfois, vous devrez **rafraîchir l'interface ComfyUI** pour qu'elle puisse lire les fichiers de modèle dans le dossier correspondant.

Ce nœud est spécialisé dans le chargement d'un modèle LoRA sans nécessiter de modèle CLIP, en se concentrant sur l'amélioration ou la modification d'un modèle donné basé sur les paramètres LoRA. Il permet l'ajustement dynamique de la force du modèle via les paramètres LoRA, facilitant un contrôle précis du comportement du modèle.

## Entrées - Lora Loader Model Only

| Champ             | Comfy dtype       | Description                                                                                   |
|-------------------|-------------------|-----------------------------------------------------------------------------------------------|
| `model`           | `MODEL`           | Le modèle de base pour les modifications, auquel les ajustements LoRA seront appliqués.        |
| `lora_name`       | `COMBO[STRING]`   | Le nom du fichier LoRA à charger, spécifiant les ajustements à appliquer au modèle.            |
| `strength_model`  | `FLOAT`           | Détermine l'intensité des ajustements LoRA, des valeurs plus élevées indiquant des modifications plus fortes. |

## Sorties - Lora Loader Model Only

| Champ   | Data Type | Description                                                              |
|---------|-------------|--------------------------------------------------------------------------|
| `model` | `MODEL`     | Le modèle modifié avec les ajustements LoRA appliqués, reflétant les changements de comportement ou de capacités du modèle. |
