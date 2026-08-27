# Trellis2Conditioning

Trellis2Conditioning convertit une image d'entrée en données de conditionnement pour le modèle TRELLIS.2. Il utilise un modèle de vision CLIP pour encoder l'image en deux ensembles de caractéristiques (aux échelles 512 et 1024) et les regroupe en une paire de conditionnement positive, tout en créant également une paire de conditionnement négative remplie de zéros correspondante qui sert de référence vide.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip_vision_model` | Le modèle de vision CLIP utilisé pour encoder l'image en caractéristiques de conditionnement. | CLIP_VISION | Oui | Tout modèle de vision CLIP disponible |
| `image` | Image prétraitée provenant d'ImageCropToMask (pad_factor=1.0 pour TRELLIS.2). | IMAGE | Oui | Toute image |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positif` | Conditionnement contenant les caractéristiques de l'image encodées aux échelles 512 et 1024, utilisé comme conditionnement positif pour le modèle TRELLIS.2. | CONDITIONING |
| `négatif` | Conditionnement rempli de zéros avec la même forme que le conditionnement positif, utilisé comme référence négative vide. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2Conditioning/fr.md)

---
**Source fingerprint (SHA-256):** `467698e58558ceca9ac633d63aacf360a1eb674ac4ebd47de7423f85e62c0fe6`
