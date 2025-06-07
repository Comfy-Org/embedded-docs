
Le nœud LatentUpscale est conçu pour agrandir les représentations latentes des images. Il permet d'ajuster les dimensions de l'image de sortie et la méthode d'agrandissement, offrant une flexibilité dans l'amélioration de la résolution des images latentes.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | La représentation latente d'une image à agrandir. Ce paramètre est crucial pour déterminer le point de départ du processus d'agrandissement. |
| `upscale_method` | COMBO[STRING] | Spécifie la méthode utilisée pour agrandir l'image latente. Différentes méthodes peuvent affecter la qualité et les caractéristiques de l'image agrandie. |
| `width`   | `INT`       | La largeur souhaitée de l'image agrandie. Si elle est définie sur 0, elle sera calculée en fonction de la hauteur pour maintenir le rapport d'aspect. |
| `height`  | `INT`       | La hauteur souhaitée de l'image agrandie. Si elle est définie sur 0, elle sera calculée en fonction de la largeur pour maintenir le rapport d'aspect. |
| `crop`    | COMBO[STRING] | Détermine comment l'image agrandie doit être recadrée, affectant l'apparence finale et les dimensions de la sortie. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La représentation latente agrandie de l'image, prête pour un traitement ou une génération ultérieure. |
