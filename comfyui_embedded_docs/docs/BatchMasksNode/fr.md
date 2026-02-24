> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchMasksNode/fr.md)

Le nœud Batch Masks combine plusieurs masques individuels en un seul lot. Il prend un nombre variable de masques en entrée et les sort sous la forme d'un seul tenseur de masques groupés, permettant ainsi un traitement par lots des masques dans les nœuds suivants.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `mask_0` | MASK | Oui | - | Le premier masque en entrée. |
| `mask_1` | MASK | Oui | - | Le deuxième masque en entrée. |
| `mask_2` à `mask_49` | MASK | Non | - | Masques supplémentaires optionnels. Le nœud peut accepter un minimum de 2 et un maximum de 50 masques au total. |

**Note :** Ce nœud utilise un modèle d'entrée à croissance automatique. Vous devez connecter au moins deux masques (`mask_0` et `mask_1`). Vous pouvez ajouter jusqu'à 48 masques optionnels supplémentaires (`mask_2` à `mask_49`) pour un total de 50 masques. Tous les masques connectés seront combinés en un seul lot.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | MASK | Un seul masque groupé contenant tous les masques d'entrée empilés ensemble. |
