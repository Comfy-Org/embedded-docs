# Flux.1 Remplir l'image

Ce document a été généré par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/en.md)

Remplit une image en fonction d'un masque et d'une invite. Ce nœud utilise le modèle Flux.1 pour remplir les zones masquées d'une image selon la description textuelle fournie, générant un nouveau contenu qui s'harmonise avec l'image environnante.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à traiter par inpainting | IMAGE | Oui | - |
| `mask` | Le masque définissant les zones de l'image à remplir | MASK | Oui | - |
| `prompt` | Invite pour la génération d'image (par défaut : chaîne vide) | STRING | Non | - |
| `suréchantillonnage du prompt` | Indique s'il faut effectuer un suréchantillonnage de l'invite. Si activé, modifie automatiquement l'invite pour une génération plus créative, mais les résultats sont non déterministes (une même graine ne produira pas exactement le même résultat). (par défaut : false) | BOOLEAN | Non | - |
| `guidage` | Force d'orientation pour le processus de génération d'image (par défaut : 60) | FLOAT | Non | 1,5-100 |
| `étapes` | Nombre d'étapes pour le processus de génération d'image (par défaut : 50) | INT | Non | 15-50 |
| `seed` | La graine aléatoire utilisée pour créer le bruit. (par défaut : 0) | INT | Non | 0-18446744073709551615 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output_image` | L'image générée avec les zones masquées remplies selon l'invite | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/fr.md)

---
**Source fingerprint (SHA-256):** `ae2708d9e4b99ecb142fca0693c3973957c5677e8121eb5e34d30f872d7102c0`
