# InstructPixToPixConditioning

Le nœud InstructPixToPixConditioning prépare les données de conditionnement pour l'édition d'images InstructPix2Pix en combinant des invites textuelles positives et négatives avec des données d'image. Il traite les images d'entrée via un encodeur VAE pour créer des représentations latentes et attache ces latentes aux données de conditionnement positives et négatives. Le nœud gère automatiquement les dimensions de l'image en rognant sur des multiples de 8 pixels pour assurer la compatibilité avec le processus d'encodage VAE.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Données de conditionnement positives contenant les invites textuelles et les paramètres pour les caractéristiques d'image souhaitées | CONDITIONING | Oui | - |
| `négatif` | Données de conditionnement négatives contenant les invites textuelles et les paramètres pour les caractéristiques d'image non souhaitées | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images d'entrée en représentations latentes | VAE | Oui | - |
| `pixels` | Image d'entrée à traiter et à encoder dans l'espace latent | IMAGE | Oui | - |

**Remarque :** Les dimensions de l'image d'entrée sont automatiquement ajustées par un rognage centré sur des multiples de 8 pixels en largeur et en hauteur afin d'assurer la compatibilité avec le processus d'encodage VAE.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Données de conditionnement positives avec représentation latente d'image attachée | CONDITIONING |
| `négatif` | Données de conditionnement négatives avec représentation latente d'image attachée | CONDITIONING |
| `latent` | Tenseur latent vide avec les mêmes dimensions que l'image encodée | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
