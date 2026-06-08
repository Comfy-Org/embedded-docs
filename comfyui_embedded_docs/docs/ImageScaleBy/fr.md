Le nœud ImageScaleBy est conçu pour agrandir des images selon un facteur d'échelle spécifié, en utilisant diverses méthodes d'interpolation. Il permet d'ajuster la taille de l'image de manière flexible, répondant à différents besoins d'agrandissement.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `image` | L'image d'entrée à agrandir. Ce paramètre est essentiel car il fournit l'image de base qui subira le processus d'agrandissement. | `IMAGE` |
| `méthode_d'agrandissement` | Spécifie la méthode d'interpolation à utiliser pour l'agrandissement. Le choix de la méthode peut affecter la qualité et les caractéristiques de l'image agrandie. | COMBO[STRING] |
| `agrandir_par` | Le facteur selon lequel l'image sera agrandie. Il détermine l'augmentation de taille de l'image de sortie par rapport à l'image d'entrée. | `FLOAT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `image` | L'image agrandie, dont la taille est supérieure à celle de l'image d'entrée selon le facteur d'échelle et la méthode d'interpolation spécifiés. | `IMAGE` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleBy/fr.md)
