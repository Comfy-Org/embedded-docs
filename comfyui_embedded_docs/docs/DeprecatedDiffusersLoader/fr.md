> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedDiffusersLoader/fr.md)

Le nœud DiffusersLoader est conçu pour charger des modèles depuis la bibliothèque diffusers, en gérant spécifiquement le chargement des modèles UNet, CLIP et VAE en fonction des chemins de modèles fournis. Il facilite l'intégration de ces modèles dans le framework ComfyUI, permettant des fonctionnalités avancées telles que la génération d'images à partir de texte, la manipulation d'images, et plus encore.

## Entrées

| Paramètre    | Type de données | Description |
|--------------|--------------|-------------|
| `model_path` | COMBO[STRING] | Spécifie le chemin du modèle à charger. Ce chemin est crucial car il détermine quel modèle sera utilisé pour les opérations suivantes, affectant la sortie et les capacités du nœud. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-------------|-------------|
| `model`   | MODEL     | Le modèle UNet chargé, qui fait partie du tuple de sortie. Ce modèle est essentiel pour les tâches de synthèse et de manipulation d'images dans le framework ComfyUI. |
| `clip`    | CLIP      | Le modèle CLIP chargé, inclus dans le tuple de sortie si demandé. Ce modèle permet des capacités avancées de compréhension et de manipulation de texte et d'images. |
| `vae`     | VAE       | Le modèle VAE chargé, inclus dans le tuple de sortie si demandé. Ce modèle est crucial pour les tâches impliquant la manipulation de l'espace latent et la génération d'images. |