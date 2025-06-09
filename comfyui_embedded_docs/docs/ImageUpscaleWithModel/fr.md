
Ce nœud est conçu pour agrandir les images en utilisant un modèle d'agrandissement spécifié. Il gère le processus d'agrandissement en ajustant l'image à l'appareil approprié, en gérant efficacement la mémoire et en appliquant le modèle d'agrandissement de manière segmentée pour éviter les erreurs de mémoire insuffisante.

## Entrées

| Paramètre         | Comfy dtype       | Description                                                                 |
|-------------------|-------------------|----------------------------------------------------------------------------|
| `upscale_model`   | `UPSCALE_MODEL`   | Le modèle d'agrandissement à utiliser pour agrandir l'image. Il est crucial pour définir l'algorithme d'agrandissement et ses paramètres. |
| `image`           | `IMAGE`           | L'image à agrandir. Cette entrée est essentielle pour déterminer le contenu source qui subira le processus d'agrandissement. |

## Sorties

| Paramètre | Data Type | Description                                        |
|-----------|-------------|----------------------------------------------------|
| `image`   | `IMAGE`     | L'image agrandie, traitée par le modèle d'agrandissement. Cette sortie est le résultat de l'opération d'agrandissement, montrant la résolution ou la qualité améliorée. |
