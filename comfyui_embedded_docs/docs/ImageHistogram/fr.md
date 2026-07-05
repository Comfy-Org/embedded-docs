# Histogramme d'image

Le nœud ImageHistogram analyse la distribution des couleurs d'une image d'entrée. Il calcule et produit plusieurs histogrammes, qui sont des graphiques montrant combien de pixels de l'image possèdent chaque valeur d'intensité possible. Il génère des histogrammes distincts pour les canaux de couleur rouge, vert et bleu, un histogramme RVB composite, ainsi qu'un histogramme de luminance basé sur une formule standard de luminosité.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à analyser. Le nœud traite la première image du lot. | IMAGE | Oui | N/A |


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `rgb` | Un histogramme composite représentant l'intensité moyenne des pixels sur les canaux rouge, vert et bleu. | HISTOGRAM |
| `luminance` | Un histogramme de la luminosité perçue de l'image, calculé à l'aide de la formule de luminance standard ITU-R BT.709. | HISTOGRAM |
| `red` | Un histogramme montrant la distribution des intensités des pixels dans le canal de couleur rouge. | HISTOGRAM |
| `green` | Un histogramme montrant la distribution des intensités des pixels dans le canal de couleur vert. | HISTOGRAM |
| `blue` | Un histogramme montrant la distribution des intensités des pixels dans le canal de couleur bleu. | HISTOGRAM |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageHistogram/fr.md)

---
**Source fingerprint (SHA-256):** `9bfcdb2907ab1e5cb2a9a736671fb9286b0e6ce6439fab95187f691b969ea53d`
