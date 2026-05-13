> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByShorterEdge/fr.md)

Ce nœud redimensionne les images afin que le bord le plus court corresponde à une longueur spécifiée, tout en préservant le rapport hauteur/largeur d'origine. Il calcule de nouvelles dimensions en fonction de la longueur cible pour le côté le plus court et renvoie l'image redimensionnée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à redimensionner. |
| `shorter_edge` | INT | Non | 1 à 8192 | Longueur cible pour le bord le plus court. (valeur par défaut : 512) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `image` | IMAGE | L'image redimensionnée dont le bord le plus court correspond à la longueur cible spécifiée. |

---
**Source fingerprint (SHA-256):** `011949390faa9032587aec210d9e38d55b79e474c7a6dcd5d3c0e75594a1fc29`
