Le nœud DiffusersLoader est conçu pour charger des modèles à partir de la bibliothèque diffusers, en gérant spécifiquement le chargement des modèles UNet, CLIP et VAE en fonction des chemins de modèles fournis. Il facilite l'intégration de ces modèles dans le cadre ComfyUI, permettant des fonctionnalités avancées telles que la génération d'images à partir de texte, la manipulation d'images, et plus encore.

## Entrées

| Paramètre    | Data Type | Description |
|--------------|--------------|-------------|
| `model_path` | COMBO[STRING] | Spécifie le chemin vers le modèle à charger. Ce chemin est crucial car il détermine quel modèle sera utilisé pour les opérations ultérieures, affectant la sortie et les capacités du nœud. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `model`   | MODEL     | Le modèle UNet chargé, qui fait partie du tuple de sortie. Ce modèle est essentiel pour les tâches de synthèse et de manipulation d'images dans le cadre ComfyUI. |
| `clip`    | CLIP      | Le modèle CLIP chargé, inclus dans le tuple de sortie si demandé. Ce modèle permet des capacités avancées de compréhension et de manipulation de texte et d'image. |
| `vae`     | VAE       | Le modèle VAE chargé, inclus dans le tuple de sortie si demandé. Ce modèle est crucial pour les tâches impliquant la manipulation de l'espace latent et la génération d'images. |
