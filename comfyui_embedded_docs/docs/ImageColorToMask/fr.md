# ImageCouleurEnMasque

Le nœud `ImageColorToMask` est conçu pour convertir une couleur spécifiée dans une image en masque. Il traite une image et une couleur cible, générant un masque où la couleur spécifiée est mise en évidence, facilitant des opérations telles que la segmentation basée sur la couleur ou l'isolation d'objets.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `image` | Le paramètre `image` représente l'image d'entrée à traiter. Il est essentiel pour déterminer les zones de l'image qui correspondent à la couleur spécifiée à convertir en masque. | `IMAGE` |
| `couleur` | Le paramètre `couleur` spécifie la couleur cible dans l'image à convertir en masque. Il joue un rôle clé dans l'identification des zones de couleur spécifiques à mettre en évidence dans le masque résultant. | `INT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `mask` | La sortie est un masque mettant en évidence les zones de l'image d'entrée qui correspondent à la couleur spécifiée. Ce masque peut être utilisé pour d'autres tâches de traitement d'image, telles que la segmentation ou l'isolation d'objets. | `MASK` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorToMask/fr.md)
