Ce nœud détectera les modèles situés dans le dossier `ComfyUI/models/vae`,
et lira également les modèles des chemins supplémentaires que vous avez configurés dans le fichier extra_model_paths.yaml.
Parfois, vous devrez **rafraîchir l'interface ComfyUI** pour qu'elle puisse lire les fichiers de modèle dans le dossier correspondant.

Le nœud VAELoader est conçu pour charger des modèles d'Autoencodeur Variationnel (VAE), spécifiquement adaptés pour gérer à la fois les VAEs standards et approximatifs. Il prend en charge le chargement des VAEs par nom, y compris une gestion spécialisée pour les modèles 'taesd' et 'taesdxl', et s'ajuste dynamiquement en fonction de la configuration spécifique du VAE.

## Entrées

| Champ   | Comfy dtype       | Description                                                                                   |
|---------|-------------------|-----------------------------------------------------------------------------------------------|
| `vae_name` | `COMBO[STRING]`    | Spécifie le nom du VAE à charger, déterminant quel modèle VAE est récupéré et chargé, avec prise en charge d'une gamme de noms de VAE prédéfinis, y compris 'taesd' et 'taesdxl'. |

## Sorties

| Champ | Data Type | Description                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `vae`  | `VAE`       | Retourne le modèle VAE chargé, prêt pour d'autres opérations telles que l'encodage ou le décodage. La sortie est un objet modèle encapsulant l'état du modèle chargé. |
