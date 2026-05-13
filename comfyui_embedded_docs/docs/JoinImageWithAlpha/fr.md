> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JoinImageWithAlpha/fr.md)

Ce nœud est conçu pour des opérations de composition, plus précisément pour fusionner une image avec son masque alpha correspondant afin de produire une image de sortie unique. Il combine efficacement le contenu visuel avec les informations de transparence, permettant de créer des images où certaines zones sont transparentes ou semi-transparentes.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `image`   | `IMAGE`         | Le contenu visuel principal à combiner avec un masque alpha. Il représente l'image sans information de transparence. |
| `alpha`   | `MASK`          | Le masque alpha qui définit la transparence de l'image correspondante. Il est utilisé pour déterminer quelles parties de l'image doivent être transparentes ou semi-transparentes. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `image`   | `IMAGE`         | La sortie est une image unique qui combine l'image d'entrée avec le masque alpha, intégrant les informations de transparence dans le contenu visuel. |