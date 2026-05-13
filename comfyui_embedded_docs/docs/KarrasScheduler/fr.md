> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KarrasScheduler/fr.md)

Le nœud KarrasScheduler est conçu pour générer une séquence de niveaux de bruit (sigmas) basée sur le plan de bruit de Karras et al. (2022). Ce planificateur est utile pour contrôler le processus de diffusion dans les modèles génératifs, permettant des ajustements précis des niveaux de bruit appliqués à chaque étape du processus de génération.

## Entrées

| Paramètre   | Type de données | Description                                                                                      |
|-------------|-----------------|------------------------------------------------------------------------------------------------|
| `étapes`     | INT             | Spécifie le nombre d'étapes dans le plan de bruit, affectant la granularité de la séquence de sigmas générée. |
| `sigma_max` | FLOAT           | La valeur sigma maximale dans le plan de bruit, définissant la limite supérieure des niveaux de bruit.                    |
| `sigma_min` | FLOAT           | La valeur sigma minimale dans le plan de bruit, définissant la limite inférieure des niveaux de bruit.                    |
| `rho`       | FLOAT           | Un paramètre qui contrôle la forme de la courbe du plan de bruit, influençant la progression des niveaux de bruit de sigma_min à sigma_max. |

## Sorties

| Paramètre | Type de données | Description                                                                 |
|-----------|-----------------|-----------------------------------------------------------------------------|
| `sigmas`  | SIGMAS          | La séquence générée de niveaux de bruit (sigmas) suivant le plan de bruit de Karras et al. (2022). |