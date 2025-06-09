Le chargeur Quadruple CLIP, QuadrupleCLIPLoader, est l'un des nœuds principaux de ComfyUI, ajouté pour la première fois pour prendre en charge le modèle de la version HiDream I1. Si vous constatez que ce nœud est manquant, essayez de mettre à jour ComfyUI vers la dernière version pour garantir le support du nœud.

Il nécessite 4 modèles CLIP, correspondant aux paramètres `clip_name1`, `clip_name2`, `clip_name3` et `clip_name4`, et fournira une sortie de modèle CLIP pour les nœuds suivants.

Ce nœud détectera les modèles situés dans le dossier `ComfyUI/models/text_encoders`,
et lira également les modèles des chemins supplémentaires configurés dans le fichier extra_model_paths.yaml.
Parfois, après avoir ajouté des modèles, vous devrez peut-être **recharger l'interface de ComfyUI** pour lui permettre de lire les fichiers de modèle dans le dossier correspondant.
