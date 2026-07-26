# TextEncodeMageFlowEdit

## Aperçu

Ce nœud encode une instruction d'édition (prompt) avec une ou plusieurs images de référence pour le modèle Mage-Flow-Edit. Il redimensionne toutes les images de référence à la résolution de sortie cible, les encode dans l'espace latent si un VAE est fourni, et attache les latents de référence à la sortie conditioning. Un tenseur latent vierge aux dimensions correctes pour l'échantillonnage est également généré, garantissant que la taille correspond toujours à la largeur et hauteur de sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Le modèle CLIP utilisé pour tokeniser et coder les prompts textuels. | CLIP | Oui | |
| `prompt` | L'instruction d'édition (prompt positif) à appliquer. | STRING | Oui | multiligne, prompts dynamiques activés |
| `negative_prompt` | Le prompt négatif pour éviter. Par défaut : chaîne vide (utilise un espace en interne lorsqu'il est vide). | STRING | Non | multiligne, prompts dynamiques activés |
| `vae` | Modèle VAE pour encoder les images de référence dans l'espace latent. S'il n'est pas fourni, aucun latent de référence n'est ajouté au conditioning. | VAE | Non | |
| `images` | Une ou plusieurs images de référence à éditer. Toutes les images sont redimensionnées à la résolution de sortie avant l'encodage. | IMAGE (autogrow) | Non | Jusqu'à 16 images (nommées `image_1`…`image_16`), au moins 0 |
| `width` | Largeur de sortie en pixels. Si réglé sur 0, la largeur de la première image de référence est utilisée. Toujours arrondi à l'inférieur à un multiple de 16. Par défaut : 0. | INT | Oui | 0 à 8192 (pas de 16) |
| `height` | Hauteur de sortie en pixels. Même comportement de repli que pour la largeur. Par défaut : 0. | INT | Oui | 0 à 8192 (pas de 16) |
| `batch_size` | Nombre d'échantillons latents à générer. Par défaut : 1. | INT | Oui | 1 à 4096 |

**Notes sur les dépendances des paramètres :**
- Si `width` et/ou `height` sont à 0 et qu'aucune image de référence n'est fournie, ils utilisent par défaut 1024 chacun.
- Le paramètre `vae` est optionnel ; les latents de référence ne sont générés et attachés au conditioning que lorsqu'un VAE est connecté.
- Le champ `negative_prompt` est optionnel – s'il est laissé vide, un seul espace est utilisé en interne comme texte négatif.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Sortie de conditioning contenant les tokens du prompt positif, plus (si un VAE a été fourni) les latents de référence encodés. | CONDITIONING |
| `negative` | Sortie de conditioning contenant les tokens du prompt négatif, plus les mêmes latents de référence (si VAE fourni). | CONDITIONING |
| `latent` | Un tenseur latent vierge de forme `[batch_size, 128, height÷16, width÷16]` à utiliser comme bruit initial lors de l'échantillonnage. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMageFlowEdit/fr.md)

---
**Source fingerprint (SHA-256):** `880d8856b7f6e656bc68ca953fbf892898d05bc5d65290ae3bf7a4405ee09be3`
