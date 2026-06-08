Ce document a été généré par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/en.md)

Ce nœud charge plusieurs images à partir d'un sous-dossier spécifié dans le répertoire d'entrée de ComfyUI. Il analyse le dossier choisi pour les types de fichiers image courants et les renvoie sous forme de liste, ce qui le rend utile pour le traitement par lots ou la préparation de jeux de données.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `folder` | Le dossier à partir duquel charger les images. Les options correspondent aux sous-dossiers présents dans le répertoire d'entrée principal de ComfyUI. | STRING | Oui | *Plusieurs options disponibles* |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | Liste des images chargées. Le nœud charge tous les fichiers image valides (PNG, JPG, JPEG, WEBP) trouvés dans le dossier sélectionné. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/fr.md)

---
**Source fingerprint (SHA-256):** `0f6e1b3d159f7d7c0c9530350ee057118a2618796f149586bae925253ecc8cf0`
