Le nœud ImageToMask est conçu pour convertir une image en masque en fonction d'un canal de couleur spécifié. Il permet d'extraire des couches de masque correspondant aux canaux rouge, vert, bleu ou alpha d'une image, facilitant les opérations nécessitant un masquage ou un traitement spécifique à un canal.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `image` | Le paramètre `image` représente l'image d'entrée à partir de laquelle un masque sera généré en fonction du canal de couleur spécifié. Il joue un rôle crucial dans la détermination du contenu et des caractéristiques du masque résultant. | `IMAGE` |
| `canal` | Le paramètre `canal` spécifie quel canal de couleur (rouge, vert, bleu ou alpha) de l'image d'entrée doit être utilisé pour générer le masque. Ce choix influence directement l'apparence du masque et les parties de l'image qui sont mises en évidence ou masquées. | COMBO[STRING] |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `mask` | Le masque de sortie `mask` est une représentation binaire ou en niveaux de gris du canal de couleur spécifié provenant de l'image d'entrée, utile pour d'autres opérations de traitement d'image ou de masquage. | `MASK` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageToMask/fr.md)
