> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositeMasked/fr.md)

Voici la traduction en français de la documentation du nœud `ImageCompositeMasked` :

Le nœud `ImageCompositeMasked` est conçu pour le compositing d'images, permettant la superposition d'une image source sur une image de destination à des coordonnées spécifiées, avec un redimensionnement et un masquage optionnels.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-------------|-------------|
| `destination` | `IMAGE` | L'image de destination sur laquelle l'image source sera compositée. Elle sert d'arrière-plan pour l'opération de compositing. |
| `source` | `IMAGE` | L'image source à composer sur l'image de destination. Cette image peut éventuellement être redimensionnée pour correspondre aux dimensions de l'image de destination. |
| `x` | `INT` | La coordonnée x dans l'image de destination où sera placé le coin supérieur gauche de l'image source. |
| `y` | `INT` | La coordonnée y dans l'image de destination où sera placé le coin supérieur gauche de l'image source. |
| `redimensionner_source` | `BOOLEAN` | Un indicateur booléen indiquant si l'image source doit être redimensionnée pour correspondre aux dimensions de l'image de destination. |
| `masque` | `MASK` | Un masque optionnel qui spécifie quelles parties de l'image source doivent être compositées sur l'image de destination. Cela permet des opérations de compositing plus complexes, telles que le fondu ou les superpositions partielles. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-------------|-------------|
| `image` | `IMAGE` | L'image résultante après l'opération de compositing, qui combine des éléments des deux images. |