# Charger le Modèle d'Agrandissement Latent

Le nœud LatentUpscaleModelLoader charge un modèle spécialisé dans l'upscaling des représentations latentes à partir d'un fichier stocké dans le dossier `latent_upscale_models` de ComfyUI. Il détecte automatiquement le type de modèle (720p, 1080p, ou un autre suréchantillonneur latent) à partir du contenu du fichier et configure l'architecture interne correspondante, rendant le modèle chargé prêt à être utilisé par d'autres nœuds.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model_name` | Le nom du fichier de modèle d'upscaling latent à charger. Les options disponibles sont remplies dynamiquement à partir des fichiers présents dans le répertoire `latent_upscale_models` de ComfyUI. | COMBO | Oui | Tous les fichiers présents dans le dossier `latent_upscale_models` |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle d'upscaling latent chargé, configuré et prêt à être utilisé. | LATENT_UPSCALE_MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/fr.md)

---
**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`
