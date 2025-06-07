Ce nœud détecte les modèles situés dans le dossier `ComfyUI/models/controlnet` et lit également les modèles des chemins supplémentaires que vous avez configurés dans le fichier extra_model_paths.yaml. Parfois, vous devrez **rafraîchir l'interface ComfyUI** pour qu'elle puisse lire les fichiers de modèle dans le dossier correspondant.

Le nœud ControlNetLoader est conçu pour charger un modèle ControlNet à partir d'un chemin spécifié. Il joue un rôle crucial dans l'initialisation des modèles ControlNet, qui sont essentiels pour appliquer des mécanismes de contrôle sur le contenu généré ou modifier le contenu existant en fonction des signaux de contrôle.

## Entrées

| Champ             | Comfy dtype       | Description                                                                       |
|-------------------|-------------------|-----------------------------------------------------------------------------------|
| `control_net_name`| `COMBO[STRING]`    | Spécifie le nom du modèle ControlNet à charger, utilisé pour localiser le fichier du modèle dans une structure de répertoire prédéfinie. |

## Sorties

| Champ          | Comfy dtype   | Description                                                              |
|----------------|---------------|--------------------------------------------------------------------------|
| `control_net`  | `CONTROL_NET` | Retourne le modèle ControlNet chargé, prêt à être utilisé pour contrôler ou modifier les processus de génération de contenu. |
