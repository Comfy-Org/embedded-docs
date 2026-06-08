Voici la traduction en français de la documentation du nœud TextEncodeQwenImageEdit :

Le nœud TextEncodeQwenImageEdit traite les invites textuelles et les images optionnelles pour générer des données de conditionnement destinées à la génération ou à l'édition d'images. Il utilise un modèle CLIP pour tokeniser l'entrée et peut éventuellement encoder des images de référence à l'aide d'un VAE pour créer des latents de référence. Lorsqu'une image est fournie, elle est automatiquement redimensionnée pour garantir des dimensions de traitement cohérentes.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour la tokenisation du texte et des images | CLIP | Oui | - |
| `invite` | Invite textuelle pour la génération de conditionnement, prend en charge les entrées multilignes et les invites dynamiques | STRING | Oui | - |
| `vae` | Modèle VAE optionnel pour encoder les images de référence en latents | VAE | Non | - |
| `image` | Image d'entrée optionnelle à des fins de référence ou d'édition | IMAGE | Non | - |

**Remarque :** Lorsque `image` et `vae` sont tous deux fournis, le nœud encode l'image en latents de référence et les attache à la sortie de conditionnement. L'image est automatiquement redimensionnée pour maintenir une échelle de traitement cohérente d'environ 1024x1024 pixels.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Données de conditionnement contenant les tokens textuels et les latents de référence optionnels pour la génération d'images | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/fr.md)

---
**Source fingerprint (SHA-256):** `143af2c93aa56ace3594ecb257cac9dbaef2666665f3fb6dfd7a987cd2ea326f`
