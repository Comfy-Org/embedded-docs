# Split Image Channels

Divise une image en ses canaux rouge, vert et bleu, et renvoie le canal alpha sous forme de masque. Chaque sortie de couleur est une image en niveaux de gris à trois canaux, elle s’affiche donc en aperçu et s’enregistre comme une image normale. Utilisez-le pour inspecter ou modifier un canal unique, ou pour extraire la transparence d’une image comportant un canal alpha : les images chargées avec Load Image n’en ont pas, car leur alpha est exposé comme sortie `MASK` séparée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L’image à diviser. Une entrée à un seul canal (niveaux de gris) est étendue de sorte que les trois sorties de couleur portent les mêmes données. | IMAGE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `red` | Le canal rouge, sous forme d’image en niveaux de gris à trois canaux. | IMAGE |
| `green` | Le canal vert, sous forme d’image en niveaux de gris à trois canaux. | IMAGE |
| `blue` | Le canal bleu, sous forme d’image en niveaux de gris à trois canaux. | IMAGE |
| `alpha` | Alpha sous forme de masque, inversé de la même manière que dans Load Image, de sorte que 1 marque les pixels entièrement transparents. Une image sans canal alpha renvoie un masque entièrement à zéro. | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageChannels/fr.md)

---
**Source fingerprint (SHA-256):** `0f300d2e86c74e856001eb82da26c871c94c1dae5ec73a4504ca258420fbcf52`
