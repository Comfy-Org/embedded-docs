# Recraft Crisp Upscale Image

Upscale une image d'entrée de manière synchrone à l'aide de l'outil « crisp upscale », augmentant sa résolution et la rendant plus nette et plus propre. Chaque image du lot d'entrée est traitée indépendamment, et les résultats suréchantillonnés sont renvoyés sous forme de lot.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à suréchantillonner. Accepte un lot d'images. | IMAGE | Oui | — |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image suréchantillonnée avec une résolution et une netteté améliorées. Renvoie un lot d'images si un lot a été fourni en entrée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCrispUpscaleNode/fr.md)

---
**Source fingerprint (SHA-256):** `7a60c563504df7a81ce5d50e989bc4a8853f4bb30805a014c9fb567d8ec83e33`
