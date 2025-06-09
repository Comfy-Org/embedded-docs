
Le nœud KarrasScheduler est conçu pour générer une séquence de niveaux de bruit (sigmas) basée sur le calendrier de bruit de Karras et al. (2022). Ce planificateur est utile pour contrôler le processus de diffusion dans les modèles génératifs, permettant des ajustements précis des niveaux de bruit appliqués à chaque étape du processus de génération.

## Entrées

| Paramètre   | Data Type | Description                                                                                      |
|-------------|-------------|------------------------------------------------------------------------------------------------|
| `steps`     | INT         | Spécifie le nombre d'étapes dans le calendrier de bruit, affectant la granularité de la séquence de sigmas générée. |
| `sigma_max` | FLOAT       | La valeur maximale de sigma dans le calendrier de bruit, définissant la limite supérieure des niveaux de bruit.                    |
| `sigma_min` | FLOAT       | La valeur minimale de sigma dans le calendrier de bruit, définissant la limite inférieure des niveaux de bruit.                    |
| `rho`       | FLOAT       | Un paramètre qui contrôle la forme de la courbe du calendrier de bruit, influençant la progression des niveaux de bruit de sigma_min à sigma_max. |

## Sorties

| Paramètre | Data Type | Description                                                                 |
|-----------|-------------|-----------------------------------------------------------------------------|
| `sigmas`  | SIGMAS      | La séquence générée de niveaux de bruit (sigmas) suivant le calendrier de bruit de Karras et al. (2022). |
