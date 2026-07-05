# Conditionnement TripoSplat

Ce nœud encode une image d'entrée à l'aide de DINOv3 et du VAE Flux2 pour créer des données de conditionnement positives et négatives pour le modèle TripoSplat. Il génère également une cible de bruit de taille fixe (latente plus données de caméra) qui sert de point de départ pour le KSampler.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip_vision` | Encodeur d'image DINOv3 ViT-H/16+ | CLIP_VISION | Oui | - |
| `vae` | VAE Flux2 | VAE | Oui | - |
| `image` | L'image d'entrée à encoder | IMAGE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positif` | Données de conditionnement positives contenant les caractéristiques DINOv3 et la latente du VAE Flux2 | CONDITIONING |
| `négatif` | Données de conditionnement négatives contenant des caractéristiques DINOv3 remplies de zéros et une latente du VAE Flux2 remplie de zéros | CONDITIONING |
| `latent` | La cible de bruit de taille fixe (séquence latente plus jeton de caméra) pour le KSampler | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `9187a4a020818b9adc762eb41e913086b59d62c47abe92d4bafdb14bc8779f51`
