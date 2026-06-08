Voici la traduction en français de la documentation du nœud ComfyUI, en respectant vos règles :

Agrandissez l'image avec des modifications minimales vers une résolution 4K. Ce nœud utilise l'agrandissement conservateur de Stability AI pour augmenter la résolution de l'image tout en préservant le contenu original et en n'apportant que des changements subtils.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à agrandir | IMAGE | Oui | - |
| `prompt` | Ce que vous souhaitez voir dans l'image de sortie. Une invite forte et descriptive qui définit clairement les éléments, les couleurs et les sujets conduira à de meilleurs résultats. (par défaut : chaîne vide) | STRING | Oui | - |
| `créativité` | Contrôle la probabilité de créer des détails supplémentaires qui ne sont pas fortement conditionnés par l'image initiale. (par défaut : 0.35) | FLOAT | Oui | 0.2-0.5 |
| `seed` | La graine aléatoire utilisée pour créer le bruit. (par défaut : 0) | INT | Oui | 0-4294967294 |
| `prompt négatif` | Mots-clés de ce que vous ne souhaitez pas voir dans l'image de sortie. Il s'agit d'une fonctionnalité avancée. (par défaut : chaîne vide) | STRING | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image agrandie en résolution 4K | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleConservativeNode/fr.md)

---
**Source fingerprint (SHA-256):** `0a6eed22a37c1019ee97035bba70660b9619b0d65e443111d1d330968ded009a`
