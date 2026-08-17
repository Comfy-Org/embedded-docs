# HunyuanImageToVideo

Le nœud HunyuanImageToVideo convertit des images en représentations latentes vidéo à l'aide du modèle vidéo Hunyuan. Il prend en entrée des conditionnements et des images de départ optionnelles pour générer des latents vidéo pouvant être ensuite traités par des modèles de génération vidéo. Le nœud prend en charge différents types de guidage pour contrôler la manière dont l'image de départ influence le processus de génération vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Conditionnement positif pour guider la génération vidéo | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images dans l'espace latent | VAE | Oui | - |
| `width` | Largeur de la vidéo de sortie en pixels (défaut : 848, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `height` | Hauteur de la vidéo de sortie en pixels (défaut : 480, pas : 16) | INT | Oui | 16 à MAX_RESOLUTION |
| `length` | Nombre d'images (frames) dans la vidéo de sortie (défaut : 53, pas : 4) | INT | Oui | 1 à MAX_RESOLUTION |
| `batch_size` | Nombre de vidéos à générer simultanément (défaut : 1) | INT | Oui | 1 à 4096 |
| `guidance_type` | Méthode pour intégrer l'image de départ dans la génération vidéo (défaut : "v1 (concat)") | COMBO | Oui | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `start_image` | Image de départ optionnelle pour initialiser la génération vidéo | IMAGE | Non | - |

**Remarque :** Lorsque `start_image` est fourni, le nœud utilise différentes méthodes de guidage selon le `guidance_type` sélectionné :

- "v1 (concat)" : Concatène le latent de l'image avec le latent vidéo et applique un masque pour fusionner l'image dans la vidéo.
- "v2 (replace)" : Remplace les premières images vidéo par le latent de l'image et applique un masque de bruit.
- "custom" : Utilise l'image comme latent de référence pour le guidage.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif modifié avec guidage d'image appliqué lorsque `start_image` est fourni | CONDITIONING |
| `latent` | Représentation latente vidéo prête pour un traitement ultérieur par les modèles de génération vidéo | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `0ed00d59513492f31760a18ce3b0edf10b64cad848ba52c4e47d5f61fae9accc`
