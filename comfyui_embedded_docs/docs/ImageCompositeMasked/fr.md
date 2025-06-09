Le nœud `ImageCompositeMasked` est conçu pour la composition d'images, permettant la superposition d'une image source sur une image de destination à des coordonnées spécifiées, avec redimensionnement et masquage optionnels.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `destination` | `IMAGE` | L'image de destination sur laquelle l'image source sera composée. Elle sert de fond pour l'opération de composition. |
| `source` | `IMAGE` | L'image source à composer sur l'image de destination. Cette image peut être redimensionnée pour s'adapter aux dimensions de l'image de destination. |
| `x` | `INT` | La coordonnée x dans l'image de destination où le coin supérieur gauche de l'image source sera placé. |
| `y` | `INT` | La coordonnée y dans l'image de destination où le coin supérieur gauche de l'image source sera placé. |
| `resize_source` | `BOOLEAN` | Un indicateur booléen indiquant si l'image source doit être redimensionnée pour correspondre aux dimensions de l'image de destination. |
| `mask` | `MASK` | Un masque optionnel qui spécifie quelles parties de l'image source doivent être composées sur l'image de destination. Cela permet des opérations de composition plus complexes, telles que le mélange ou les superpositions partielles. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `image` | `IMAGE` | L'image résultante après l'opération de composition, qui combine des éléments des deux images. |
