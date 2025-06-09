Ce nœud est conçu pour modifier le comportement d'un modèle CLIP en définissant une couche spécifique comme la dernière à être exécutée. Cela permet de personnaliser la profondeur de traitement au sein du modèle CLIP, affectant potentiellement la sortie du modèle en limitant la quantité d'informations traitées.

## Entrées

| Paramètre            | Data Type | Description |
|---------------------|--------------|-------------|
| `clip`               | `CLIP`      | Le modèle CLIP à modifier. Ce paramètre permet au nœud d'interagir directement avec et de modifier la structure du modèle CLIP. |
| `stop_at_clip_layer` | `INT`       | Spécifie la couche à laquelle le modèle CLIP doit arrêter le traitement. Cela permet de contrôler la profondeur de calcul et peut être utilisé pour ajuster le comportement ou la performance du modèle. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `clip`    | CLIP      | Le modèle CLIP modifié avec la couche spécifiée définie comme la dernière. Cette sortie permet une utilisation ou une analyse ultérieure du modèle ajusté. |
