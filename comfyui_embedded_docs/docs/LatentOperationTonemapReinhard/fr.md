# Opération de Mappage de Tons Reinhard Latent

LatentOperationTonemapReinhard applique un mappage de tons de type Reinhard aux vecteurs latents. Cette technique normalise les vecteurs latents et ajuste leur magnitude à l'aide d'une approche statistique basée sur la moyenne et l'écart type des magnitudes, l'intensité étant contrôlée par un paramètre multiplicateur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `multiplier` | Contrôle l'intensité de l'effet de mappage de tons (défaut : 1.0) | FLOAT | Oui | 0.0 à 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `operation` | Renvoie une opération de mappage de tons pouvant être appliquée aux vecteurs latents | LATENT_OPERATION |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/fr.md)

---
**Source fingerprint (SHA-256):** `19d58c288967ab27eb1e84e60bc35a6d6c8b4e643168de689132396ae0ee3cbe`
