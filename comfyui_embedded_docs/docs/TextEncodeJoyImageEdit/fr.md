# TextEncodeJoyImageEdit

Ce nœud encode un prompt textuel et des images optionnelles en données de conditionnement pour une utilisation avec les modèles JoyImage. Il combine un encodeur textuel CLIP avec des entrées d'images optionnelles pour créer un conditionnement riche pouvant guider des tâches de génération ou d'édition d'images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Le modèle CLIP utilisé pour encoder le prompt textuel | CLIP | Oui | - |
| `prompt` | Le prompt textuel à encoder, prenant en charge les entrées multilignes et les prompts dynamiques | STRING | Oui | - |
| `vae` | Un modèle VAE pour encoder les images dans l'espace latent (optionnel) | VAE | Non | - |
| `images` | Une ou plusieurs images à inclure dans le conditionnement, jusqu'à un maximum de 6 images | IMAGE | Non | 0 à 6 images |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `CONDITIONING` | Les données de conditionnement encodées combinant le prompt textuel et les éventuelles images fournies | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeJoyImageEdit/fr.md)

---
**Source fingerprint (SHA-256):** `ef48523aa9fc990b2839d755cef272bcdfbacef5af8d961736fde5200c6f082d`
