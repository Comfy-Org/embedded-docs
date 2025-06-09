Le nœud `GrowMask` est conçu pour modifier la taille d'un masque donné, soit en l'agrandissant, soit en le contractant, tout en appliquant éventuellement un effet effilé aux coins. Cette fonctionnalité est cruciale pour ajuster dynamiquement les limites du masque dans les tâches de traitement d'image, permettant un contrôle plus flexible et précis de la zone d'intérêt.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `mask`    | MASK        | Le masque d'entrée à modifier. Ce paramètre est central dans l'opération du nœud, servant de base sur laquelle le masque est soit agrandi, soit contracté. |
| `expand`  | INT         | Détermine l'ampleur et la direction de la modification du masque. Les valeurs positives provoquent l'agrandissement du masque, tandis que les valeurs négatives entraînent sa contraction. Ce paramètre influence directement la taille finale du masque. |
| `tapered_corners` | BOOLEAN    | Un indicateur booléen qui, lorsqu'il est réglé sur True, applique un effet effilé aux coins du masque lors de la modification. Cette option permet des transitions plus douces et des résultats visuellement attrayants. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `mask`    | MASK        | Le masque modifié après application de l'agrandissement/contraction spécifié et de l'effet optionnel aux coins effilés. |
S
