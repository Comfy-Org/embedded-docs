# TextEncodeQwenImageEdit

Le nœud `TextEncodeQwenImageEdit` traite les invites textuelles et des images optionnelles pour générer des données de conditionnement pour la génération ou l'édition d'images. Il utilise un modèle CLIP pour tokeniser l'entrée et peut éventuellement encoder des images de référence à l'aide d'un VAE pour créer des latents de référence. Lorsqu'une image est fournie, il redimensionne automatiquement l'image pour maintenir des dimensions de traitement cohérentes.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour la tokenisation du texte et des images | CLIP | Oui | - |
| `prompt` | Invite textuelle pour la génération du conditionnement, prend en charge les entrées multilignes et les invites dynamiques | STRING | Oui | - |
| `vae` | Modèle VAE optionnel pour encoder les images de référence en latents | VAE | Non | - |
| `image` | Image d'entrée optionnelle pour la référence ou l'édition | IMAGE | Non | - |

**Remarque :** Lorsque `image` et `vae` sont tous deux fournis, le nœud encode l'image en latents de référence et les attache à la sortie de conditionnement. L'image est automatiquement redimensionnée pour maintenir une échelle de traitement cohérente d'environ 1024x1024 pixels.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Données de conditionnement contenant des jetons de texte et des latents de référence optionnels pour la génération d'images | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/fr.md)

---
**Source fingerprint (SHA-256):** `ec6980a63eab0d6c95be3abea00b2bf3018d30a1267f0b39a21be29a3e9228fe`
