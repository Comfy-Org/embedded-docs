> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageHistogram/fr.md)

## Vue d'ensemble

Le nœud ImageHistogram analyse la distribution des couleurs d'une image d'entrée. Il calcule et génère plusieurs histogrammes, qui sont des graphiques montrant combien de pixels dans l'image possèdent chaque valeur d'intensité possible. Il produit des histogrammes distincts pour les canaux de couleur rouge, vert et bleu, un histogramme RVB composite, ainsi qu'un histogramme de luminance basé sur une formule de luminosité standard.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | N/A | L'image d'entrée à analyser. Le nœud traite la première image du lot. |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `rgb` | HISTOGRAM | Un histogramme composite représentant l'intensité moyenne des pixels à travers les canaux rouge, vert et bleu. |
| `luminance` | HISTOGRAM | Un histogramme de la luminosité perçue de l'image, calculée à l'aide de la formule de luminance standard ITU-R BT.709. |
| `red` | HISTOGRAM | Un histogramme montrant la distribution des intensités des pixels dans le canal de couleur rouge. |
| `green` | HISTOGRAM | Un histogramme montrant la distribution des intensités des pixels dans le canal de couleur vert. |
| `blue` | HISTOGRAM | Un histogramme montrant la distribution des intensités des pixels dans le canal de couleur bleu. |