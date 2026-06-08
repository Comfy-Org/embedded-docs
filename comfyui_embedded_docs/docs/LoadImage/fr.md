Voici la traduction en français de la documentation du nœud LoadImage :

Le nœud LoadImage est conçu pour charger et prétraiter des images à partir d'un chemin spécifié. Il gère les formats d'image avec plusieurs trames, applique les transformations nécessaires telles que la rotation basée sur les données EXIF, normalise les valeurs des pixels et génère éventuellement un masque pour les images comportant un canal alpha. Ce nœud est essentiel pour préparer les images en vue d'un traitement ou d'une analyse ultérieure dans un pipeline.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `image` | Le paramètre `image` spécifie l'identifiant de l'image à charger et à traiter. Il est crucial pour déterminer le chemin d'accès au fichier image et pour charger ensuite l'image en vue de sa transformation et de sa normalisation. | COMBO[STRING] |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `image` | L'image traitée, dont les valeurs des pixels sont normalisées et les transformations appliquées si nécessaire. Elle est prête pour un traitement ou une analyse ultérieure. | `IMAGE` |
| `mask` | Une sortie facultative fournissant un masque pour l'image, utile dans les scénarios où l'image comprend un canal alpha pour la transparence. | `MASK` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImage/fr.md)
