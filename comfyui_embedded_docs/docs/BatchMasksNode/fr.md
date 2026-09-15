# Masques par lot

Le nœud Batch Masks combine plusieurs entrées de masques individuelles en un seul lot. Il prend un nombre variable d'entrées de masques et les renvoie sous forme d'un unique tenseur de masques regroupés en lot, ce qui permet le traitement par lots des masques dans les nœuds suivants. Si les masques d'entrée ont des tailles différentes, ils sont automatiquement redimensionnés pour correspondre aux dimensions du premier masque.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `mask` | Les entrées de masques à combiner en un lot. Au moins un masque est requis. Vous pouvez ajouter jusqu'à 50 masques au total en cliquant sur le bouton « + » du nœud. Si les masques ont des tailles différentes, ils sont automatiquement redimensionnés pour correspondre aux dimensions du premier masque. | MASK | Oui | 1 à 50 masques |

**Remarque :** Ce nœud utilise un modèle d'entrée à croissance automatique. Vous devez connecter au moins un masque. Vous pouvez ajouter jusqu'à 49 entrées de masque supplémentaires pour un total de 50 masques. Tous les masques connectés seront combinés en un seul lot. Si les masques ont des hauteurs ou des largeurs différentes, ils sont automatiquement redimensionnés pour correspondre aux dimensions du premier masque à l'aide d'une interpolation bilinéaire.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Un unique masque regroupé en lot contenant tous les masques d'entrée empilés ensemble. Si aucun masque n'est fourni, renvoie None. | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchMasksNode/fr.md)

---
**Source fingerprint (SHA-256):** `7e9bc4be72c7fa8fceab2cf167c72b7e1ff858c0281d977f2ad3ab433d9d58d6`
