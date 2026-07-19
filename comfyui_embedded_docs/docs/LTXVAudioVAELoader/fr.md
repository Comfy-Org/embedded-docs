# Chargeur Audio VAE LTXV

Voici la traduction de la documentation du nœud LTXV Audio VAE Loader :

Le nœud LTXV Audio VAE Loader charge un modèle d'autoencodeur variationnel audio (VAE) pré-entraîné à partir d'un fichier de point de contrôle. Il lit le point de contrôle spécifié, charge ses poids et métadonnées, et prépare le modèle pour une utilisation dans des workflows de génération ou de traitement audio au sein de ComfyUI.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `ckpt_name` | Point de contrôle Audio VAE à charger. Il s'agit d'une liste déroulante remplie avec tous les fichiers trouvés dans votre répertoire `checkpoints` de ComfyUI. | STRING | Oui | Tous les fichiers du dossier `checkpoints`.<br>*Exemple : `"audio_vae.safetensors"`* |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `Audio VAE` | Le modèle d'autoencodeur variationnel audio chargé, prêt à être connecté à d'autres nœuds de traitement audio. | VAE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/fr.md)

---
**Source fingerprint (SHA-256):** `44e79f694eed796a83f3ac25c56946baaa12b016568bd8824eb179bf79e50588`
