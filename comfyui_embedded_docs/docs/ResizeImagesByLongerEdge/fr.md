> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByLongerEdge/fr.md)

Le nœud Redimensionner par Bord le Plus Long redimensionne une ou plusieurs images afin que leur côté le plus long corresponde à une longueur cible spécifiée. Il détermine automatiquement si la largeur ou la hauteur est la plus longue et met à l'échelle l'autre dimension proportionnellement pour préserver le rapport hauteur/largeur d'origine. Cela est utile pour standardiser les tailles d'images en fonction de leur plus grande dimension.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée ou le lot d'images à redimensionner. |
| `longer_edge` | INT | Oui | 1 - 8192 | Longueur cible pour le bord le plus long. Le bord le plus court sera mis à l'échelle proportionnellement. (valeur par défaut : 1024) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `image` | IMAGE | L'image ou le lot d'images redimensionné(e). La sortie aura le même nombre d'images que l'entrée, chaque image ayant son bord le plus long correspondant à la longueur `longer_edge` spécifiée. |

---
**Source fingerprint (SHA-256):** `687d5f159967eccbf64f0ec529ae6edeb94f4707ae10a3c75a5d0b08c86dd828`
