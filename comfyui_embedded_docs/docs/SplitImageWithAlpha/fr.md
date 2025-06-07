
Le nœud SplitImageWithAlpha est conçu pour séparer les composants couleur et alpha d'une image. Il traite un tenseur d'image d'entrée, extrayant les canaux RGB comme composant couleur et le canal alpha comme composant de transparence, facilitant les opérations nécessitant la manipulation de ces aspects distincts de l'image.

## Entrées

| Paramètre | Type Comfy | Description |
|-----------|------------|-------------|
| `image`   | `IMAGE`    | Le paramètre 'image' représente le tenseur d'image d'entrée à partir duquel les canaux RGB et alpha doivent être séparés. Il est crucial pour l'opération car il fournit les données sources pour la séparation. |

## Sorties

| Paramètre | Type Comfy | Description |
|-----------|------------|-------------|
| `image`   | `IMAGE`    | La sortie 'image' représente les canaux RGB séparés de l'image d'entrée, fournissant le composant couleur sans les informations de transparence. |
| `mask`    | `MASK`     | La sortie 'mask' représente le canal alpha séparé de l'image d'entrée, fournissant les informations de transparence. |
