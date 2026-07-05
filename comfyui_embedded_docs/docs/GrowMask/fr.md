# GrowMask

Le nœud `GrowMask` est conçu pour modifier la taille d'un masque donné, en l'agrandissant ou en le réduisant, avec la possibilité d'appliquer un effet d'atténuation sur les coins. Cette fonctionnalité est essentielle pour ajuster dynamiquement les limites d'un masque dans les tâches de traitement d'image, offrant un contrôle plus flexible et précis sur la zone d'intérêt.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `masque` | Le masque d'entrée à modifier. Ce paramètre est central au fonctionnement du nœud, servant de base sur laquelle le masque est soit agrandi, soit réduit. | MASK |
| `agrandir` | Détermine l'ampleur et la direction de la modification du masque. Les valeurs positives agrandissent le masque, tandis que les valeurs négatives le réduisent. Ce paramètre influence directement la taille finale du masque. | INT |
| `coins_évasés` | Un indicateur booléen qui, lorsqu'il est défini sur Vrai, applique un effet d'atténuation aux coins du masque lors de la modification. Cette option permet des transitions plus douces et des résultats visuellement agréables. | BOOLEAN |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `masque` | Le masque modifié après application de l'agrandissement/réduction spécifié et de l'effet d'atténuation optionnel des coins. | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrowMask/fr.md)
