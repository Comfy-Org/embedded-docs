Le nœud ImageScaleBy est conçu pour agrandir les images par un facteur d'échelle spécifié en utilisant diverses méthodes d'interpolation. Il permet d'ajuster la taille de l'image de manière flexible, répondant à différents besoins d'agrandissement.

## Entrées

| Paramètre       | Data Type | Description                                                                 |
|-----------------|-------------|----------------------------------------------------------------------------|
| `image`         | `IMAGE`     | L'image d'entrée à agrandir. Ce paramètre est crucial car il fournit l'image de base qui subira le processus d'agrandissement. |
| `upscale_method`| COMBO[STRING] | Spécifie la méthode d'interpolation à utiliser pour l'agrandissement. Le choix de la méthode peut affecter la qualité et les caractéristiques de l'image agrandie. |
| `scale_by`      | `FLOAT`     | Le facteur par lequel l'image sera agrandie. Cela détermine l'augmentation de la taille de l'image de sortie par rapport à l'image d'entrée. |

## Sorties

| Paramètre | Data Type | Description                                                   |
|-----------|-------------|---------------------------------------------------------------|
| `image`   | `IMAGE`     | L'image agrandie, qui est plus grande que l'image d'entrée selon le facteur d'échelle spécifié et la méthode d'interpolation. |
