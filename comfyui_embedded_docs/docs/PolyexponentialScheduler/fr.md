# PolyexponentialScheduler

Le nœud PolyexponentialScheduler est conçu pour générer une séquence de niveaux de bruit (sigmas) basée sur un programme de bruit polyexponentiel. Ce programme est une fonction polynomiale dans le logarithme de sigma, permettant une progression flexible et personnalisable des niveaux de bruit tout au long du processus de diffusion.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `étapes` | Spécifie le nombre d'étapes dans le processus de diffusion, affectant la granularité des niveaux de bruit générés. | INT |
| `sigma_max` | Le niveau de bruit maximal, définissant la borne supérieure du programme de bruit. | FLOAT |
| `sigma_min` | Le niveau de bruit minimal, définissant la borne inférieure du programme de bruit. | FLOAT |
| `rho` | Un paramètre qui contrôle la forme du programme de bruit polyexponentiel, influençant la progression des niveaux de bruit entre les valeurs minimale et maximale. | FLOAT |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `sigmas` | La sortie est une séquence de niveaux de bruit (sigmas) adaptée au programme de bruit polyexponentiel spécifié. | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PolyexponentialScheduler/fr.md)
