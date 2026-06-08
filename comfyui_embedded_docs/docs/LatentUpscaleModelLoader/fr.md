Le nœud LatentUpscaleModelLoader charge un modèle spécialisé conçu pour la mise à l'échelle des représentations latentes. Il lit un fichier de modèle depuis le dossier système désigné et détecte automatiquement son type (720p, 1080p ou autre) afin d'instancier et de configurer l'architecture interne appropriée du modèle. Le modèle chargé est alors prêt à être utilisé par d'autres nœuds pour des tâches de super-résolution dans l'espace latent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model_name` | Le nom du fichier de modèle de mise à l'échelle latente à charger. Les options disponibles sont générées dynamiquement à partir des fichiers présents dans votre répertoire `latent_upscale_models` de ComfyUI. | STRING | Oui | *Tous les fichiers du dossier `latent_upscale_models`* |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle de mise à l'échelle latente chargé, configuré et prêt à être utilisé. | LATENT_UPSCALE_MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/fr.md)

---
**Source fingerprint (SHA-256):** `bd97f3ec1422aaabbd60779aa4112be44791daddc6307de53ae0e4219a90ab0e`
