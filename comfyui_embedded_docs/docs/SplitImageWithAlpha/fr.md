Voici la traduction en français de la documentation du nœud **SplitImageWithAlpha** :

Le nœud SplitImageWithAlpha est conçu pour séparer les composantes de couleur et alpha d’une image. Il traite un tenseur d’image en entrée, en extrayant les canaux RVB comme composante couleur et le canal alpha comme composante de transparence, facilitant ainsi les opérations nécessitant la manipulation de ces aspects distincts de l’image.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `image` | Le paramètre `image` représente le tenseur d’image d’entrée à partir duquel les canaux RVB et alpha doivent être séparés. Il est essentiel pour l’opération car il fournit les données sources pour la séparation. | `IMAGE` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `image` | La sortie `image` représente les canaux RVB séparés de l’image d’entrée, fournissant la composante couleur sans l’information de transparence. | `IMAGE` |
| `mask` | La sortie `mask` représente le canal alpha séparé de l’image d’entrée, fournissant l’information de transparence. | `MASK` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageWithAlpha/fr.md)
