# ConditionnementunCLIP

Ce nœud est conçu pour intégrer les sorties de la vision CLIP dans le processus de conditionnement, en ajustant l'influence de ces sorties en fonction de paramètres spécifiques de force et d'augmentation du bruit. Il enrichit le conditionnement avec un contexte visuel, améliorant ainsi le processus de génération.

## Entrées

| Paramètre | Description | Type Comfy |
| --- | --- | --- |
| `conditionnement` | Les données de conditionnement de base auxquelles les sorties de la vision CLIP doivent être ajoutées, servant de fondement pour les modifications ultérieures. | `CONDITIONING` |
| `sortie_vision_clip` | La sortie d'un modèle de vision CLIP, fournissant un contexte visuel qui est intégré dans le conditionnement. | `CLIP_VISION_OUTPUT` |
| `force` | Détermine l'intensité de l'influence de la sortie de la vision CLIP sur le conditionnement. | `FLOAT` |
| `augmentation_bruit` | Spécifie le niveau d'augmentation du bruit à appliquer à la sortie de la vision CLIP avant de l'intégrer dans le conditionnement. | `FLOAT` |

## Sorties

| Paramètre | Description | Type Comfy |
| --- | --- | --- |
| `conditionnement` | Les données de conditionnement enrichies, contenant désormais les sorties intégrées de la vision CLIP avec la force et l'augmentation du bruit appliquées. | `CONDITIONING` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPConditioning/fr.md)
