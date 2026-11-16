# Bria Remove Image Background

Ce nœud supprime l'arrière-plan d'une image à l'aide du service Bria RMBG 2.0 ou RMBG 3.0. Il envoie l'image à une API externe pour traitement et renvoie le résultat avec l'arrière-plan supprimé.

## Entrées

Le sélecteur `moderation` révèle des options de modération supplémentaires lorsqu'il est défini sur `"true"`.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée dont l'arrière-plan sera supprimé. | IMAGE | Oui | - |
| `modération` | Paramètres de modération. Lorsqu'ils sont définis sur `"true"`, des options de modération supplémentaires deviennent disponibles. | DYNAMIC_COMBO | Oui | `"false"`<br>`"true"` |
| `graine` | Le paramètre `seed` contrôle si le nœud doit être réexécuté ; la même image donne toujours le même résultat quelle que soit la graine. Valeur par défaut : `0`. | INT | Oui | 0 à 2147483647 |
| `model` | Modèle de suppression d'arrière-plan. `"RMBG2"` est la valeur par défaut ; `"RMBG3"` utilise le modèle plus récent Bria RMBG 3.0. | COMBO | Non | `"RMBG2"`<br>`"RMBG3"` |

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
**Source fingerprint (SHA-256):** `82f7ec2ac2d1579a3da009b464bce7c56fa2d7b1f599744d6158177ecd462cb2`
