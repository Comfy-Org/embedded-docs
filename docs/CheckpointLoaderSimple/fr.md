Ce nœud détectera les modèles situés dans le dossier `ComfyUI/models/checkpoints`, 
et lira également les modèles des chemins supplémentaires que vous avez configurés dans le fichier extra_model_paths.yaml. 
Parfois, vous devrez **rafraîchir l'interface ComfyUI** pour qu'elle puisse lire les fichiers de modèle dans le dossier correspondant.


Le nœud CheckpointLoaderSimple est conçu pour charger des checkpoints de modèle sans avoir besoin de spécifier une configuration. Il simplifie le processus de chargement de checkpoint en ne nécessitant que le nom du checkpoint, le rendant plus accessible pour les utilisateurs qui pourraient ne pas être familiers avec les détails de configuration.
## Types d'entrée

| Champ     | Comfy dtype | Description                                                                       |
|-----------|-------------|-----------------------------------------------------------------------------------|
| `ckpt_name`| `COMBO[STRING]` | Spécifie le nom du checkpoint à charger, déterminant quel fichier de checkpoint le nœud tentera de charger et affectant l'exécution du nœud ainsi que le modèle chargé. |

## Types de sortie

| Champ | Comfy dtype | Description                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `model` | `MODEL` | Retourne le modèle chargé, permettant son utilisation pour un traitement ou une inférence ultérieure. |
| `clip`  | `CLIP`     | Retourne le modèle CLIP associé au checkpoint chargé, si disponible. |
| `vae`   | `VAE`      | Retourne le modèle VAE associé au checkpoint chargé, si disponible. |