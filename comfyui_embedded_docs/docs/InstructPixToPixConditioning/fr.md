# InstructPixToPixConditioning

Le nœud InstructPixToPixConditioning prépare les données de conditionnement pour l’édition d’image InstructPix2Pix en combinant des prompts textuels positifs et négatifs avec les données d’image. Il encode l’image d’entrée via un VAE en une représentation latente et attache ce latent aux conditionnements positif et négatif, tout en renvoyant également un latent vide correspondant. Les dimensions de l’image sont automatiquement recadrées sur des multiples de 8 pixels afin que le VAE puisse les traiter.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Données de conditionnement positives contenant les prompts textuels et les réglages pour les caractéristiques d’image souhaitées | CONDITIONING | Oui | - |
| `négatif` | Données de conditionnement négatives contenant les prompts textuels et les réglages pour les caractéristiques d’image non souhaitées | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder les images d’entrée en représentations latentes | VAE | Oui | - |
| `pixels` | Image d’entrée à traiter et à encoder dans l’espace latent | IMAGE | Oui | - |

**Remarque :** Les dimensions de l’image d’entrée sont automatiquement ajustées par recadrage centré sur des multiples de 8 pixels en largeur et en hauteur afin de garantir la compatibilité avec le processus d’encodage du VAE.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Données de conditionnement positives avec le latent d’image encodé attaché en tant que `concat_latent_image` | CONDITIONING |
| `negative` | Données de conditionnement négatives avec le latent d’image encodé attaché en tant que `concat_latent_image` | CONDITIONING |
| `latent` | Tenseur latent de zéros ayant les mêmes dimensions que l’image encodée | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
