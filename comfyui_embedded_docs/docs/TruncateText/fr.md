> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TruncateText/fr.md)

Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TruncateText/en.md)

Ce nœud raccourcit un texte en le coupant à une longueur maximale spécifiée. Il prend n'importe quel texte en entrée et ne renvoie que la première partie, jusqu'au nombre de caractères que vous définissez. C'est un moyen simple de garantir qu'un texte ne dépasse pas une certaine taille.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `text` | STRING | Oui | N/D | La chaîne de texte à tronquer. |
| `max_length` | INT | Oui | 1 à 10000 | Longueur maximale du texte. Le texte sera coupé après ce nombre de caractères (par défaut : 77). |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `string` | STRING | Le texte tronqué, contenant uniquement les premiers `max_length` caractères de l'entrée. |

---
**Source fingerprint (SHA-256):** `271a77a910967c4fd86a07485449679fb8db89f6b3f2bf0a8fa2ff224ea2f7b2`
