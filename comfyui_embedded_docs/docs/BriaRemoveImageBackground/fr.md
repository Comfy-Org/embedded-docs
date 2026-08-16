# Bria Remove Image Background

Ce nœud supprime l'arrière-plan d'une image à l'aide du service Bria RMBG 2.0. Il envoie l'image à une API externe pour traitement et renvoie le résultat avec l'arrière-plan supprimé.

## Entrées

Le sélecteur `moderation` révèle des options de modération supplémentaires lorsqu'il est défini sur `"true"`.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `moderation` | Paramètres de modération. Lorsqu'il est défini sur `"true"`, des options de modération supplémentaires deviennent disponibles. | DYNAMIC_COMBO | Oui | `"false"`<br>`"true"` |
| `image` | L'image d'entrée dont l'arrière-plan sera supprimé. | IMAGE | Oui | - |
| `seed` | La graine contrôle si le nœud doit se réexécuter ; les résultats sont non déterministes quelle que soit la graine. Par défaut : `0`. | INT | Oui | 0 à 2147483647 |

### Entrées de modération « true »

Ces paramètres n'apparaissent que lorsque `moderation` est défini sur `"true"`. L'option `"false"` n'ajoute aucune entrée supplémentaire.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `visual_input_moderation` | Active la modération du contenu visuel sur l'image d'entrée. Par défaut : `False`. | BOOLEAN | Non | - |
| `visual_output_moderation` | Active la modération du contenu visuel sur l'image de sortie. Par défaut : `True`. | BOOLEAN | Non | - |

**Remarque :** Les paramètres `visual_input_moderation` et `visual_output_moderation` dépendent du paramètre `moderation`. Ils ne sont actifs que lorsque `moderation` est défini sur `"true"`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image traitée avec son arrière-plan supprimé. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/fr.md)

---
**Source fingerprint (SHA-256):** `f62dcd5c9406ec09f5aab44585dd7f25ae0f7d9a934faa10a58e46ef116df110`
