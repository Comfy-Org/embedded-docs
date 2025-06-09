
Le nœud PolyexponentialScheduler est conçu pour générer une séquence de niveaux de bruit (sigmas) basée sur un calendrier de bruit polyexponentiel. Ce calendrier est une fonction polynomiale dans le logarithme de sigma, permettant une progression flexible et personnalisable des niveaux de bruit tout au long du processus de diffusion.

## Entrées

| Paramètre   | Data Type | Description                                                                                                                                                        |
| ----------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `steps`     | INT         | Spécifie le nombre d'étapes dans le processus de diffusion, affectant la granularité des niveaux de bruit générés.                                                 |
| `sigma_max` | FLOAT       | Le niveau de bruit maximal, fixant la limite supérieure du calendrier de bruit.                                                                                    |
| `sigma_min` | FLOAT       | Le niveau de bruit minimal, fixant la limite inférieure du calendrier de bruit.                                                                                    |
| `rho`       | FLOAT       | Un paramètre qui contrôle la forme du calendrier de bruit polyexponentiel, influençant la progression des niveaux de bruit entre les valeurs minimale et maximale. |

## Sorties

| Paramètre | Data Type | Description                                                                                                      |
| --------- | ----------- | ---------------------------------------------------------------------------------------------------------------- |
| `sigmas`  | SIGMAS      | La sortie est une séquence de niveaux de bruit (sigmas) adaptée au calendrier de bruit polyexponentiel spécifié. |
