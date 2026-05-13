> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/fr.md)

Ce document a été généré par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/en.md)

Remplit une image en fonction d'un masque et d'une invite. Ce nœud utilise le modèle Flux.1 pour remplir les zones masquées d'une image selon la description textuelle fournie, générant un nouveau contenu qui s'harmonise avec l'image environnante.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à traiter par inpainting |
| `mask` | MASK | Oui | - | Le masque définissant les zones de l'image à remplir |
| `prompt` | STRING | Non | - | Invite pour la génération d'image (par défaut : chaîne vide) |
| `suréchantillonnage du prompt` | BOOLEAN | Non | - | Indique s'il faut effectuer un suréchantillonnage de l'invite. Si activé, modifie automatiquement l'invite pour une génération plus créative, mais les résultats sont non déterministes (une même graine ne produira pas exactement le même résultat). (par défaut : false) |
| `guidage` | FLOAT | Non | 1,5-100 | Force d'orientation pour le processus de génération d'image (par défaut : 60) |
| `étapes` | INT | Non | 15-50 | Nombre d'étapes pour le processus de génération d'image (par défaut : 50) |
| `seed` | INT | Non | 0-18446744073709551615 | La graine aléatoire utilisée pour créer le bruit. (par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output_image` | IMAGE | L'image générée avec les zones masquées remplies selon l'invite |

---
**Source fingerprint (SHA-256):** `ae2708d9e4b99ecb142fca0693c3973957c5677e8121eb5e34d30f872d7102c0`
