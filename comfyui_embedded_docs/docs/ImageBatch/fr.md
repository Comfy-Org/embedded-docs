Le nœud `ImageBatch` est conçu pour combiner deux images en un seul lot. Si les dimensions des images ne correspondent pas, il redimensionne automatiquement la seconde image pour qu'elle corresponde aux dimensions de la première avant de les combiner.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `image1` | La première image à combiner dans le lot. Elle sert de référence pour les dimensions auxquelles la seconde image sera ajustée si nécessaire. | `IMAGE` |
| `image2` | La seconde image à combiner dans le lot. Elle est automatiquement redimensionnée pour correspondre aux dimensions de la première image si elles diffèrent. | `IMAGE` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `image` | Le lot d'images combiné, avec la seconde image redimensionnée pour correspondre aux dimensions de la première si nécessaire. | `IMAGE` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBatch/fr.md)
