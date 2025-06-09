Le nœud `ImageBatch` est conçu pour combiner deux images en un seul lot. Si les dimensions des images ne correspondent pas, il redimensionne automatiquement la deuxième image pour qu'elle corresponde aux dimensions de la première avant de les combiner.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `image1`  | `IMAGE`     | La première image à combiner dans le lot. Elle sert de référence pour les dimensions auxquelles la deuxième image sera ajustée si nécessaire. |
| `image2`  | `IMAGE`     | La deuxième image à combiner dans le lot. Elle est automatiquement redimensionnée pour correspondre aux dimensions de la première image si elles diffèrent. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | Le lot d'images combinées, avec la deuxième image redimensionnée pour correspondre aux dimensions de la première si nécessaire. |
