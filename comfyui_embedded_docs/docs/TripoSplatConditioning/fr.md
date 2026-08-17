# Conditionnement TripoSplat

Ce nœud encode une image d’entrée à l’aide de l’encodeur de vision DINOv3 et du VAE Flux2 pour créer des données de conditionnement positives et négatives pour le modèle TripoSplat. Il génère également une cible de bruit de taille fixe (une séquence latente plus un jeton de caméra) qui sert de point de départ pour le KSampler.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip_vision` | Encodeur d’image DINOv3 ViT-H/16+ | CLIP_VISION | Oui | - |
| `vae` | VAE Flux2 | VAE | Oui | - |
| `image` | L’image d’entrée à encoder | IMAGE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------------|
| `positive` | Données de conditionnement positives contenant les caractéristiques d’image DINOv3 et le latent du VAE Flux2 de l’image d’entrée | CONDITIONING |
| `negative` | Données de conditionnement négatives contenant des caractéristiques DINOv3 remplies de zéros et un latent du VAE Flux2 rempli de zéros | CONDITIONING |
| `latent` | Cible de bruit de taille fixe (latent + caméra) pour le KSampler | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`
