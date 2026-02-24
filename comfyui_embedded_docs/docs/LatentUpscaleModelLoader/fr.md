> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/fr.md)

## Vue d'ensemble

Le nœud **LatentUpscaleModelLoader** charge un modèle spécialisé conçu pour le suréchantillonnage (upscaling) de représentations latentes. Il lit un fichier de modèle depuis le dossier désigné du système et détecte automatiquement son type (720p, 1080p ou autre) pour instancier et configurer l'architecture de modèle interne correcte. Le modèle chargé est ensuite prêt à être utilisé par d'autres nœuds pour des tâches de super-résolution dans l'espace latent.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model_name` | STRING | Oui | *Tous les fichiers du dossier `latent_upscale_models`* | Le nom du fichier du modèle de suréchantillonnage latent à charger. Les options disponibles sont dynamiquement peuplées à partir des fichiers présents dans votre répertoire `latent_upscale_models` de ComfyUI. |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | LATENT_UPSCALE_MODEL | Le modèle de suréchantillonnage latent chargé, configuré et prêt à l'emploi. |
