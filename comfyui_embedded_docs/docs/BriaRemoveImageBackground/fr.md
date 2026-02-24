> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/fr.md)

Ce nœud supprime l'arrière-plan d'une image en utilisant le service Bria RMBG 2.0. Il envoie l'image à une API externe pour traitement et renvoie le résultat avec l'arrière-plan supprimé.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée dont l'arrière-plan sera supprimé. |
| `moderation` | COMBO | Non | `"false"`<br>`"true"` | Paramètres de modération. Lorsqu'il est défini sur `"true"`, des options de modération supplémentaires deviennent disponibles. |
| `visual_input_moderation` | BOOLEAN | Non | - | Active la modération du contenu visuel sur l'image d'entrée. Ce paramètre n'est disponible que lorsque `moderation` est défini sur `"true"`. Par défaut : `False`. |
| `visual_output_moderation` | BOOLEAN | Non | - | Active la modération du contenu visuel sur l'image de sortie. Ce paramètre n'est disponible que lorsque `moderation` est défini sur `"true"`. Par défaut : `True`. |
| `seed` | INT | Non | 0 à 2147483647 | Une valeur de seed qui contrôle si le nœud doit être réexécuté. Les résultats sont non déterministes, quelle que soit la valeur du seed. Par défaut : `0`. |

**Note :** Les paramètres `visual_input_moderation` et `visual_output_moderation` dépendent du paramètre `moderation`. Ils ne sont actifs et requis que si `moderation` est défini sur `"true"`.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image traitée avec son arrière-plan supprimé. |
