# Charger Point de Contrôle

Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/en.md)

## Aperçu

Charge un fichier de point de contrôle (checkpoint) de modèle de diffusion et le décompose en trois composants principaux : le modèle principal utilisé pour le débruitage des latents, l'encodeur de texte CLIP et l'encodeur/décodeur d'images VAE. Ce nœud détecte automatiquement tous les fichiers de modèle dans le dossier `ComfyUI/models/checkpoints` ainsi que tous les chemins supplémentaires configurés dans votre fichier `extra_model_paths.yaml`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `nom_ckpt` | Le nom du point de contrôle (modèle) à charger. Sélectionnez le nom du fichier du modèle de point de contrôle, qui détermine le modèle d'IA utilisé pour la génération d'images ultérieure. | STRING | Oui | Tous les fichiers de modèle dans le dossier checkpoints |

**Remarque :** Si de nouveaux fichiers de modèle sont ajoutés pendant que ComfyUI est en cours d'exécution, vous devez actualiser le navigateur (Ctrl+R) pour voir les nouveaux fichiers dans la liste déroulante.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle utilisé pour le débruitage des latents. Il s'agit du modèle de diffusion principal utilisé pour la génération d'images. | MODEL |
| `CLIP` | Le modèle CLIP utilisé pour encoder les invites textuelles, convertissant les descriptions textuelles en informations compréhensibles par l'IA. | CLIP |
| `VAE` | Le modèle VAE utilisé pour encoder et décoder les images vers et depuis l'espace latent. | VAE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/fr.md)

---
**Source fingerprint (SHA-256):** `2fd8866ae659f8080f46c16d3a9864fa563d2090815d897ea2f42ba8d66d9b39`
