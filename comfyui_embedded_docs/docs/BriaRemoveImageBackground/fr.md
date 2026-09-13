# Bria Remove Image Background

Ce nœud supprime l'arrière-plan d'une image à l'aide du service Bria RMBG 2.0. Il envoie l'image à une API externe pour traitement et renvoie le résultat avec l'arrière-plan supprimé.

## Entrées

Le sélecteur `moderation` révèle des options de modération supplémentaires lorsqu'il est défini sur `"true"`.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée dont l'arrière-plan sera supprimé. | IMAGE | Oui | - |
| `moderation` | Paramètres de modération. Lorsqu'ils sont définis sur `"true"`, des options de modération supplémentaires deviennent disponibles. | DYNAMIC_COMBO | Oui | `"false"`<br>`"true"` |
| `seed` | Le paramètre `seed` contrôle si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quelle que soit la graine. Valeur par défaut : `0`. | INT | Oui | 0 à 2147483647 |

### Entrées lorsque `moderation` est défini sur `"true"`

Ces paramètres apparaissent uniquement lorsque `moderation` est défini sur `"true"`. L'option `"false"` n'ajoute aucune entrée supplémentaire.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `visual_input_moderation` | Active la modération du contenu visuel sur l'image d'entrée. Valeur par défaut : `False`. | BOOLEAN | Non | - |
| `visual_output_moderation` | Active la modération du contenu visuel sur l'image de sortie. Valeur par défaut : `True`. | BOOLEAN | Non | - |

**Remarque :** Les paramètres `visual_input_moderation` et `visual_output_moderation` dépendent du paramètre `moderation`. Ils ne sont actifs que lorsque `moderation` est défini sur `"true"`.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `image` | L'image traitée avec son arrière-plan supprimé. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/fr.md)

---
**Source fingerprint (SHA-256):** `f62dcd5c9406ec09f5aab44585dd7f25ae0f7d9a934faa10a58e46ef116df110`
