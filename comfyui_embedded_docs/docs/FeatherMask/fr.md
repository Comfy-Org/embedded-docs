Le nœud `FeatherMask` applique un effet de fondu aux bords d'un masque donné, en transitionnant progressivement les contours du masque par un ajustement de leur opacité en fonction des distances spécifiées depuis chaque bord. Cela crée un effet de bord plus doux et estompé.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `masque` | Le masque auquel l'effet de fondu sera appliqué. Il détermine la zone de l'image qui sera affectée par l'estompage. | MASK |
| `gauche` | Spécifie la distance depuis le bord gauche à l'intérieur de laquelle l'effet de fondu sera appliqué. | INT |
| `haut` | Spécifie la distance depuis le bord supérieur à l'intérieur de laquelle l'effet de fondu sera appliqué. | INT |
| `droite` | Spécifie la distance depuis le bord droit à l'intérieur de laquelle l'effet de fondu sera appliqué. | INT |
| `bas` | Spécifie la distance depuis le bord inférieur à l'intérieur de laquelle l'effet de fondu sera appliqué. | INT |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `masque` | La sortie est une version modifiée du masque d'entrée avec un effet de fondu appliqué à ses bords. | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FeatherMask/fr.md)
