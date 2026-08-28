# TextEncodeQwenImageEdit

Le nœud TextEncodeQwenImageEdit convertit les prompts textuels et les images facultatives en données de conditionnement pour la génération ou l’édition d’images. Il utilise un modèle CLIP pour tokeniser l’entrée et peut, en option, encoder des images de référence avec un VAE afin de créer des latents de référence. Lorsqu’une image est fournie, elle est automatiquement redimensionnée pour conserver une échelle de traitement cohérente.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Modèle CLIP utilisé pour la tokenisation du texte et des images. | CLIP | Oui | - |
| `invite` | Prompt textuel pour la génération du conditionnement, prend en charge la saisie multiligne et les prompts dynamiques. | STRING | Oui | - |
| `vae` | Modèle VAE facultatif pour encoder les images de référence en latents. | VAE | Non | - |
| `image` | Image d’entrée facultative à des fins de référence ou d’édition. | IMAGE | Non | - |

**Remarque :** Lorsqu’une image est fournie, elle est redimensionnée afin que son nombre total de pixels reste proche de 1 048 576 (1024 × 1024), et seuls ses canaux RVB sont utilisés. L’image redimensionnée est transmise au tokeniseur CLIP avec le prompt. Lorsque `image` et `vae` sont tous deux fournis, le nœud encode également l’image en latents de référence et les attache à la sortie de conditionnement.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Données de conditionnement contenant des tokens de texte et, le cas échéant, des latents de référence pour la génération d’images. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/fr.md)

---
**Source fingerprint (SHA-256):** `ec6980a63eab0d6c95be3abea00b2bf3018d30a1267f0b39a21be29a3e9228fe`
