# Bria Remove Image Background

Ce nœud supprime l'arrière-plan d'une image à l'aide du service Bria RMBG 2.0. Il envoie l'image à une API externe pour traitement et renvoie le résultat avec l'arrière-plan supprimé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée dont l'arrière-plan sera supprimé. | IMAGE | Oui | - |
| `modération` | Paramètres de modération. Lorsqu'il est défini sur `"true"`, des options de modération supplémentaires deviennent disponibles. | COMBO | Non | `"false"`<br>`"true"` |
| `visual_input_moderation` | Active la modération du contenu visuel sur l'image d'entrée. Ce paramètre n'est disponible que lorsque `modération` est défini sur `"true"`. Par défaut : `False`. | BOOLEAN | Non | - |
| `visual_output_moderation` | Active la modération du contenu visuel sur l'image de sortie. Ce paramètre n'est disponible que lorsque `modération` est défini sur `"true"`. Par défaut : `True`. | BOOLEAN | Non | - |
| `graine` | Une valeur de graine qui détermine si le nœud doit être réexécuté. Les résultats sont non déterministes quelle que soit la valeur de la graine. Par défaut : `0`. | INT | Non | 0 à 2147483647 |

**Remarque :** Les paramètres `visual_input_moderation` et `visual_output_moderation` dépendent du paramètre `moderation`. Ils ne sont actifs et requis que si `moderation` est défini sur `"true"`.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image traitée avec son arrière-plan supprimé. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/fr.md)

---
**Source fingerprint (SHA-256):** `2b2dd3ca0d026af1a2bf3f7222165928527b05b65817073b50230ff18d39bc6c`
