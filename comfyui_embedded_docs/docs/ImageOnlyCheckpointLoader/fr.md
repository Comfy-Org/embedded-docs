Ce nœud détecte les modèles situés dans le dossier `ComfyUI/models/checkpoints`, et il peut également lire les modèles des chemins supplémentaires que vous avez configurés dans le fichier extra_model_paths.yaml. Parfois, vous devrez **rafraîchir l'interface ComfyUI** pour qu'elle puisse lire les fichiers de modèle dans le dossier correspondant.

Ce nœud est spécialisé dans le chargement de checkpoints spécifiquement pour les modèles basés sur l'image dans les flux de travail de génération vidéo. Il récupère et configure efficacement les composants nécessaires à partir d'un checkpoint donné, en se concentrant sur les aspects liés à l'image du modèle.

## Entrées

| Champ      | Data Type | Description                                                                       |
|------------|-------------|-----------------------------------------------------------------------------------|
| `ckpt_name`| COMBO[STRING] | Spécifie le nom du checkpoint à charger, crucial pour identifier et récupérer le fichier de checkpoint correct à partir d'une liste prédéfinie. |

## Sorties

| Champ     | Data Type | Description                                                                                   |
|-----------|-------------|-----------------------------------------------------------------------------------------------|
| `model`   | MODEL     | Retourne le modèle principal chargé à partir du checkpoint, configuré pour le traitement d'image dans les contextes de génération vidéo. |
| `clip_vision` | `CLIP_VISION` | Fournit le composant CLIP vision du checkpoint, adapté pour la compréhension de l'image et l'extraction de caractéristiques. |
| `vae`     | VAE       | Fournit le composant Autoencodeur Variationnel (VAE), essentiel pour les tâches de manipulation et de génération d'images. |
