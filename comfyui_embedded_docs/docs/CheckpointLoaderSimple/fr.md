# Charger Point de Contrôle

Charge un fichier de checkpoint de modèle de diffusion et le divise en trois composants principaux : le modèle principal utilisé pour le débruitage des latents, l’encodeur de texte CLIP et l’encodeur/décodeur d’images VAE. Le nœud détecte automatiquement tous les fichiers de modèle dans le dossier `ComfyUI/models/checkpoints` ainsi que les chemins supplémentaires configurés dans votre fichier `extra_model_paths.yaml`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `ckpt_name` | Le nom du checkpoint (modèle) à charger. Sélectionnez le nom du fichier de modèle de checkpoint, qui détermine le modèle d’IA utilisé pour la génération d’images suivante. | COMBO | Oui | Tous les fichiers de modèle trouvés dans le dossier des checkpoints |

**Remarque :** Si de nouveaux fichiers de modèle sont ajoutés pendant que ComfyUI est en cours d’exécution, vous devez actualiser le navigateur (Ctrl+R) pour voir les nouveaux fichiers dans la liste déroulante.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle utilisé pour le débruitage des latents. Il s’agit du modèle de diffusion principal utilisé pour la génération d’images. | MODEL |
| `CLIP` | Le modèle CLIP utilisé pour encoder les prompts textuels, en convertissant les descriptions textuelles en informations que l’IA peut comprendre. | CLIP |
| `VAE` | Le modèle VAE utilisé pour encoder et décoder les images vers et depuis l’espace latent. | VAE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/fr.md)

---
**Source fingerprint (SHA-256):** `db99a8ba83a586491463df0d4e99ba5f77d4511c6d8337a721d76edd3450f310`
