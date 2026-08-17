# Charger le Modèle d'Agrandissement Latent

Le nœud LatentUpscaleModelLoader charge un modèle spécialisé conçu pour la mise à l'échelle des représentations latentes. Il lit un fichier modèle dans le dossier désigné du système et détecte automatiquement son type (720p, 1080p ou autre) pour instancier et configurer l'architecture de modèle interne correcte. Le modèle chargé est ensuite prêt à être utilisé par d'autres nœuds pour des tâches de super-résolution dans l'espace latent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model_name` | Le nom du fichier de modèle de mise à l'échelle latente à charger. Les options disponibles sont remplies dynamiquement à partir des fichiers présents dans votre répertoire `latent_upscale_models` de ComfyUI. | COMBO | Oui | Tous les fichiers du dossier `latent_upscale_models` |

Remarque : Le nœud détecte automatiquement l'architecture du modèle à partir du contenu du fichier. Les modèles contenant des couches de super-résolution HunyuanVideo 720p sont chargés comme modèles 720p, les modèles avec des couches de suréchantillonnage de style 1080p sont chargés comme modèles 1080p, et les modèles avec d'autres structures de couches sont chargés comme modèles LatentUpsampler.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle de mise à l'échelle latente chargé, configuré et prêt à l'emploi. | LATENT_UPSCALE_MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/fr.md)

---
**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`
