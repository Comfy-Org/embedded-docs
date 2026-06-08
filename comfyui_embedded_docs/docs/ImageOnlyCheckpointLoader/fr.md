Ce nœud détecte les modèles situés dans le dossier `ComfyUI/models/checkpoints`, et lit également les modèles depuis les chemins supplémentaires configurés dans le fichier extra_model_paths.yaml. Il peut parfois être nécessaire d'**actualiser l'interface ComfyUI** pour lui permettre de lire les fichiers de modèles depuis le dossier correspondant.

Ce nœud est spécialisé dans le chargement de points de contrôle (checkpoints) spécifiquement pour les modèles basés sur l'image au sein de workflows de génération vidéo. Il récupère et configure efficacement les composants nécessaires à partir d'un point de contrôle donné, en se concentrant sur les aspects liés à l'image du modèle.

## Entrées

| Champ | Description | Type de données |
| --- | --- | --- |
| `nom_ckpt` | Spécifie le nom du point de contrôle à charger, essentiel pour identifier et récupérer le fichier de point de contrôle correct depuis une liste prédéfinie. | COMBO[STRING] |

## Sorties

| Champ | Description | Type de données |
| --- | --- | --- |
| `model` | Renvoie le modèle principal chargé depuis le point de contrôle, configuré pour le traitement d'image dans des contextes de génération vidéo. | MODEL |
| `clip_vision` | Fournit le composant CLIP vision du point de contrôle, adapté à la compréhension d'image et à l'extraction de caractéristiques. | `CLIP_VISION` |
| `vae` | Délivre le composant Autoencodeur Variationnel (VAE), essentiel pour les tâches de manipulation et de génération d'image. | VAE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointLoader/fr.md)
