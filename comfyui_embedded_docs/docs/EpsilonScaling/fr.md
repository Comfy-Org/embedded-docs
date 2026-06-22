# EpsilonScaling

Implémente la méthode d'échelle epsilon (Epsilon Scaling) issue de l'article de recherche « Elucidating the Exposure Bias in Diffusion Models ». Cette méthode améliore la qualité des échantillons en ajustant l'échelle du bruit prédit pendant le processus d'échantillonnage. Elle utilise un programme uniforme pour atténuer le biais d'exposition dans les modèles de diffusion.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel appliquer l'échelle epsilon | MODEL | Oui | - |
| `scaling_factor` | Le facteur utilisé pour mettre à l'échelle le bruit prédit (par défaut : 1,005) | FLOAT | Non | 0,5 - 1,5 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle avec l'échelle epsilon appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EpsilonScaling/fr.md)
