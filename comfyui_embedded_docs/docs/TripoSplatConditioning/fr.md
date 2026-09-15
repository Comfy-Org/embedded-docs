# Conditionnement TripoSplat

Ce nœud encode une image d'entrée avec l'encodeur d'images DINOv3 et le VAE Flux2 pour produire des données de conditionnement positives et négatives destinées au modèle TripoSplat. Il crée également une cible de bruit de taille fixe (latent plus données de caméra) qui sert de point de départ au KSampler.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip_vision` | Encodeur d'images DINOv3 ViT-H/16+ | CLIP_VISION | Oui | - |
| `vae` | VAE Flux2 | VAE | Oui | - |
| `image` | Image d'entrée à encoder | IMAGE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------------|
| `positive` | Données de conditionnement positives contenant la séquence de caractéristiques DINOv3 et le latent du VAE Flux2 transporté comme latent de référence | CONDITIONING |
| `negative` | Données de conditionnement négatives contenant des caractéristiques DINOv3 remplies de zéros et un latent de référence du VAE Flux2 rempli de zéros | CONDITIONING |
| `latent` | La cible de bruit de taille fixe (latent + caméra) pour le KSampler. Le latent est une séquence de codes de forme à dimensions constantes (8192 x 16) associée à un unique jeton de caméra (1 x 5) | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`
