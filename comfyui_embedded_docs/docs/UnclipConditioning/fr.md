
Ce nœud est conçu pour intégrer les sorties de vision CLIP dans le processus de conditionnement, en ajustant l'influence de ces sorties en fonction des paramètres de force et d'augmentation de bruit spécifiés. Il enrichit le conditionnement avec un contexte visuel, améliorant ainsi le processus de génération.

## Entrées

| Paramètre              | Comfy dtype            | Description |
|------------------------|------------------------|-------------|
| `conditioning`         | `CONDITIONING`         | Les données de conditionnement de base auxquelles les sorties de vision CLIP doivent être ajoutées, servant de fondation pour d'autres modifications. |
| `clip_vision_output`   | `CLIP_VISION_OUTPUT`   | La sortie d'un modèle de vision CLIP, fournissant un contexte visuel intégré dans le conditionnement. |
| `strength`             | `FLOAT`                | Détermine l'intensité de l'influence de la sortie de vision CLIP sur le conditionnement. |
| `noise_augmentation`   | `FLOAT`                | Spécifie le niveau d'augmentation de bruit à appliquer à la sortie de vision CLIP avant de l'intégrer dans le conditionnement. |

## Sorties

| Paramètre             | Comfy dtype            | Description |
|-----------------------|------------------------|-------------|
| `conditioning`         | `CONDITIONING`         | Les données de conditionnement enrichies, contenant désormais des sorties de vision CLIP intégrées avec la force et l'augmentation de bruit appliquées. |
