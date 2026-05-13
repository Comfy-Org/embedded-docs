> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/fr.md)

Le nœud InstructPixToPixConditioning prépare les données de conditionnement pour l'édition d'images InstructPix2Pix en combinant des invites textuelles positives et négatives avec des données d'image. Il traite les images d'entrée via un encodeur VAE pour créer des représentations latentes et attache ces latentes aux données de conditionnement positives et négatives. Le nœud gère automatiquement les dimensions de l'image en recadrant aux multiples de 8 pixels pour assurer la compatibilité avec le processus d'encodage VAE.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Données de conditionnement positives contenant les invites textuelles et les paramètres pour les caractéristiques d'image souhaitées |
| `negative` | CONDITIONING | Oui | - | Données de conditionnement négatives contenant les invites textuelles et les paramètres pour les caractéristiques d'image indésirables |
| `vae` | VAE | Oui | - | Modèle VAE utilisé pour encoder les images d'entrée en représentations latentes |
| `pixels` | IMAGE | Oui | - | Image d'entrée à traiter et encoder dans l'espace latent |

**Remarque :** Les dimensions de l'image d'entrée sont automatiquement ajustées en recadrant au multiple de 8 pixels le plus proche en largeur et en hauteur pour garantir la compatibilité avec le processus d'encodage VAE.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `positive` | CONDITIONING | Données de conditionnement positives avec représentation d'image latente attachée |
| `negative` | CONDITIONING | Données de conditionnement négatives avec représentation d'image latente attachée |
| `latent` | LATENT | Tenseur latent vide avec les mêmes dimensions que l'image encodée |

---
**Source fingerprint (SHA-256):** `4b2383c9d64efdb558758359bf544fc5a1be65c12b23b54152e2df79a6dd8d79`
