# Chargeur Audio VAE LTXV

Le nœud LTXV Audio VAE Loader charge un modèle d’autoencodeur variationnel audio (VAE) pré-entraîné à partir d’un fichier de checkpoint. Il lit le checkpoint spécifié, charge ses poids et ses métadonnées, et prépare le modèle pour une utilisation dans des flux de travail de génération ou de traitement audio au sein de ComfyUI.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `ckpt_name` | Checkpoint audio VAE à charger. Il s’agit d’une liste déroulante remplie avec tous les fichiers trouvés dans votre répertoire `checkpoints` de ComfyUI. | COMBO | Oui | Tous les fichiers du dossier `checkpoints` (rempli dynamiquement).<br>*Exemple : `"audio_vae.safetensors"`* |

Remarque : Le nœud génère une erreur si le fichier de checkpoint sélectionné est introuvable ou ne contient pas un VAE audio valide.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `Audio VAE` | Le modèle d’autoencodeur variationnel audio chargé, prêt à être connecté à d’autres nœuds de traitement audio. | VAE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/fr.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`
