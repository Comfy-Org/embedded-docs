> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/fr.md)

Le nœud LatentOperationTonemapReinhard applique un mappage tonal Reinhard aux vecteurs latents. Cette technique normalise les vecteurs latents et ajuste leur amplitude à l'aide d'une approche statistique basée sur la moyenne et l'écart type, l'intensité étant contrôlée par un paramètre multiplicateur.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `multiplicateur` | FLOAT | Non | 0.0 à 100.0 | Contrôle l'intensité de l'effet de mappage tonal (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `operation` | LATENT_OPERATION | Renvoie une opération de mappage tonal pouvant être appliquée aux vecteurs latents |

---
**Source fingerprint (SHA-256):** `70c04eaef06b749392a0c65f3d1267e52484f7cf956f87173d10ad935afcf98c`
