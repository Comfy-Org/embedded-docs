> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAELoader/fr.md)

Ce nœud détecte les modèles situés dans le dossier `ComfyUI/models/vae`, et lit également les modèles provenant de chemins supplémentaires configurés dans le fichier extra_model_paths.yaml. Il peut parfois être nécessaire de **rafraîchir l'interface ComfyUI** pour lui permettre de lire les fichiers de modèles depuis le dossier correspondant.

Le nœud VAELoader est conçu pour charger des modèles d'autoencodeur variationnel (VAE), spécifiquement adapté pour gérer à la fois les VAE standards et approximatifs. Il prend en charge le chargement des VAE par nom, y compris une gestion spécialisée pour les modèles 'taesd' et 'taesdxl', et s'ajuste dynamiquement en fonction de la configuration spécifique du VAE.

## Entrées

| Champ       | Type Comfy        | Description                                                                                   |
|-------------|-------------------|-----------------------------------------------------------------------------------------------|
| `vae_name`  | `COMBO[STRING]`   | Spécifie le nom du VAE à charger, déterminant quel modèle VAE est récupéré et chargé, avec prise en charge d'une gamme de noms de VAE prédéfinis, y compris 'taesd' et 'taesdxl'. |

## Sorties

| Champ | Type de données | Description                                                              |
|-------|-----------------|--------------------------------------------------------------------------|
| `vae` | `VAE`           | Renvoie le modèle VAE chargé, prêt pour d'autres opérations telles que l'encodage ou le décodage. La sortie est un objet modèle encapsulant l'état du modèle chargé. |