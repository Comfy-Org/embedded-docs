> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuadrupleCLIPLoader/fr.md)

Voici la traduction en français de la documentation du nœud Quadruple CLIP Loader :

Le Chargeur CLIP Quadruple, QuadrupleCLIPLoader, est l'un des nœuds fondamentaux de ComfyUI, initialement ajouté pour prendre en charge le modèle HiDream I1 version. Si ce nœud est manquant, essayez de mettre à jour ComfyUI vers la dernière version pour garantir la prise en charge du nœud.

Il nécessite 4 modèles CLIP, correspondant aux paramètres `clip_name1`, `clip_name2`, `clip_name3` et `clip_name4`, et fournira une sortie de modèle CLIP pour les nœuds suivants.

Ce nœud détectera les modèles situés dans le dossier `ComfyUI/models/text_encoders`,
 et lira également les modèles à partir de chemins supplémentaires configurés dans le fichier extra_model_paths.yaml.
 Parfois, après avoir ajouté des modèles, vous devrez peut-être **recharger l'interface ComfyUI** pour lui permettre de lire les fichiers de modèles dans le dossier correspondant.