Le nœud `FeatherMask` applique un effet de plume aux bords d'un masque donné, en transitionnant en douceur les bords du masque en ajustant leur opacité en fonction des distances spécifiées à partir de chaque bord. Cela crée un effet de bord plus doux et plus fondu.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|--------------|-------------|
| `mask`    | MASK         | Le masque auquel l'effet de plume sera appliqué. Il détermine la zone de l'image qui sera affectée par l'effet de plume. |
| `left`    | INT          | Spécifie la distance à partir du bord gauche dans laquelle l'effet de plume sera appliqué. |
| `top`     | INT          | Spécifie la distance à partir du bord supérieur dans laquelle l'effet de plume sera appliqué. |
| `right`   | INT          | Spécifie la distance à partir du bord droit dans laquelle l'effet de plume sera appliqué. |
| `bottom`  | INT          | Spécifie la distance à partir du bord inférieur dans laquelle l'effet de plume sera appliqué. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|--------------|-------------|
| `mask`    | MASK         | La sortie est une version modifiée du masque d'entrée avec un effet de plume appliqué à ses bords. |
