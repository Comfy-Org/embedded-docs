# InstructPixToPixConditioning

Le nœud InstructPixToPixConditioning prépare les données de conditionnement pour l’édition d’images InstructPix2Pix en combinant une image d’entrée avec le conditionnement textuel positif et négatif. Il encode l’image avec le VAE en une représentation latente, attache ce latent aux deux ensembles de conditionnement, puis crée un tenseur latent rempli de zéros aux dimensions correspondantes. Si la largeur ou la hauteur de l’image n’est pas un multiple de 8 pixels, l’image est recadrée automatiquement avant l’encodage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Données de conditionnement positives contenant les invites texte et les réglages pour les caractéristiques souhaitées de l’image. | CONDITIONING | Oui | - |
| `negative` | Données de conditionnement négatives contenant les invites texte et les réglages pour les caractéristiques indésirables de l’image. | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour encoder l’image d’entrée en une représentation latente. | VAE | Oui | - |
| `pixels` | Image d’entrée à traiter et à encoder dans l’espace latent. | IMAGE | Oui | - |

**Remarque :** L’image d’entrée est automatiquement recadrée pour que sa largeur et sa hauteur soient des multiples de 8 pixels, en arrondissant à l’inférieur, afin de garantir la compatibilité avec le processus d’encodage du VAE.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Données de conditionnement positives avec le latent de l’image encodée attaché. | CONDITIONING |
| `negative` | Données de conditionnement négatives avec le latent de l’image encodée attaché. | CONDITIONING |
| `latent` | Tenseur latent rempli de zéros avec les mêmes dimensions que l’image encodée. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
