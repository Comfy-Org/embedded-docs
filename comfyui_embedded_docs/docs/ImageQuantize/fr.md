Le nœud ImageQuantize est conçu pour réduire le nombre de couleurs dans une image à un nombre spécifié, en appliquant éventuellement des techniques de dithering pour maintenir la qualité visuelle. Ce processus est utile pour créer des images basées sur une palette ou réduire la complexité des couleurs pour certaines applications.

## Entrées

| Champ   | Data Type | Description                                                                       |
|---------|-------------|-----------------------------------------------------------------------------------|
| `image` | `IMAGE`     | Le tenseur d'image d'entrée à quantifier. Il affecte l'exécution du nœud en étant la donnée principale sur laquelle la réduction des couleurs est effectuée. |
| `colors`| `INT`       | Spécifie le nombre de couleurs auquel réduire l'image. Il influence directement le processus de quantification en déterminant la taille de la palette de couleurs. |
| `dither`| COMBO[STRING] | Détermine la technique de dithering à appliquer lors de la quantification, affectant la qualité visuelle et l'apparence de l'image de sortie. |

## Sorties

| Champ | Data Type | Description                                                                   |
|-------|-------------|-------------------------------------------------------------------------------|
| `image`| `IMAGE`     | La version quantifiée de l'image d'entrée, avec une complexité de couleur réduite et éventuellement dithered pour maintenir la qualité visuelle. |
