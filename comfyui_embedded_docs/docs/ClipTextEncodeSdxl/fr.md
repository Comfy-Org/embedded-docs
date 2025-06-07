Ce nœud est conçu pour encoder les entrées textuelles en utilisant le modèle CLIP spécifiquement adapté à l'architecture SDXL. Il se concentre sur la conversion des descriptions textuelles en un format qui peut être efficacement utilisé pour générer ou manipuler des images, en tirant parti des capacités du modèle CLIP pour comprendre et traiter le texte dans le contexte du contenu visuel.

## Entrées

| Paramètre | Data Type | Description |
| --- | --- | --- |
| `clip` | `CLIP` | L'instance du modèle CLIP utilisée pour encoder le texte. Elle joue un rôle vital dans le traitement de l'entrée textuelle et sa conversion en un format adapté aux tâches de génération ou de manipulation d'images. |
| `width` | `INT` | Spécifie la largeur de l'image en pixels. Elle détermine les dimensions de l'image générée ou manipulée. |
| `height` | `INT` | Spécifie la hauteur de l'image en pixels. Elle détermine les dimensions de l'image générée ou manipulée. |
| `crop_w` | `INT` | Définit la largeur de la zone de recadrage en pixels. Ce paramètre est utilisé pour recadrer l'image à une largeur spécifique avant le traitement. |
| `crop_h` | `INT` | Définit la hauteur de la zone de recadrage en pixels. Ce paramètre est utilisé pour recadrer l'image à une hauteur spécifique avant le traitement. |
| `target_width` | `INT` | La largeur cible pour l'image de sortie après traitement. Elle permet de redimensionner l'image à une largeur souhaitée. |
| `target_height` | `INT` | La hauteur cible pour l'image de sortie après traitement. Elle permet de redimensionner l'image à une hauteur souhaitée. |
| `text_g` | `STRING` | La description textuelle globale à encoder. Cette entrée est cruciale pour générer les représentations visuelles correspondantes et comprendre le contenu décrit. |
| `text_l` | `STRING` | La description textuelle locale à encoder. Cette entrée fournit des détails ou un contexte supplémentaires à la description globale, améliorant la spécificité de l'image générée ou manipulée. |

## Sorties

| Paramètre | Data Type | Description |
| --- | --- | --- |
| `conditioning` | `CONDITIONING` | La sortie du nœud, qui inclut le texte encodé ainsi que des informations supplémentaires nécessaires pour les tâches de génération ou de manipulation d'images. |
