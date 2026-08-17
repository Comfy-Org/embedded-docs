# Histogramme d'image

Le nœud ImageHistogram analyse la distribution des couleurs d'une image d'entrée. Il calcule et produit plusieurs histogrammes, qui sont des graphiques montrant combien de pixels de l'image ont chaque valeur d'intensité possible. Il génère des histogrammes distincts pour les canaux de couleur rouge, vert et bleu, un histogramme RVB composite, et un histogramme de luminance basé sur une formule standard de luminosité.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à analyser. Le nœud traite la première image du lot. | IMAGE | Oui | N/A |

## Sorties

Tous les histogrammes de sortie contiennent 256 valeurs, une pour chaque niveau d'intensité de 0 à 255.

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `rgb` | Un histogramme composite représentant l'intensité moyenne des pixels sur les canaux rouge, vert et bleu. | HISTOGRAM |
| `luminance` | Un histogramme de la luminosité perçue de l'image, calculé à l'aide de la formule de luminance standard ITU-R BT.709. | HISTOGRAM |
| `red` | Un histogramme montrant la distribution des intensités de pixels dans le canal de couleur rouge. | HISTOGRAM |
| `green` | Un histogramme montrant la distribution des intensités de pixels dans le canal de couleur vert. | HISTOGRAM |
| `blue` | Un histogramme montrant la distribution des intensités de pixels dans le canal de couleur bleu. | HISTOGRAM |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageHistogram/fr.md)

---
**Source fingerprint (SHA-256):** `5020f5cedd325250a207a00950011f4b6dc19ddfe4d172665ffca4982731dd5e`
