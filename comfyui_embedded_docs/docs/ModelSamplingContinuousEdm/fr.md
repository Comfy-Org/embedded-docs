> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousEDM/fr.md)

Ce nœud est conçu pour améliorer les capacités d'échantillonnage d'un modèle en intégrant des techniques d'échantillonnage EDM (Energy-based Diffusion Models) continu. Il permet un ajustement dynamique des niveaux de bruit dans le processus d'échantillonnage du modèle, offrant un contrôle plus précis sur la qualité et la diversité de la génération.

## Entrées

| Paramètre   | Type de données | Type Python        | Description |
|-------------|-----------------|----------------------|-------------|
| `modèle`     | `MODEL`         | `torch.nn.Module`   | Le modèle à améliorer avec des capacités d'échantillonnage EDM continu. Il sert de base pour l'application des techniques d'échantillonnage avancées. |
| `échantillonnage`  | COMBO[STRING]   | `str`               | Spécifie le type d'échantillonnage à appliquer, soit 'eps' pour l'échantillonnage epsilon, soit 'v_prediction' pour la prédiction de vélocité, influençant le comportement du modèle pendant le processus d'échantillonnage. |
| `sigma_max` | `FLOAT`         | `float`             | La valeur sigma maximale pour le niveau de bruit, permettant un contrôle de la limite supérieure dans le processus d'injection de bruit pendant l'échantillonnage. |
| `sigma_min` | `FLOAT`         | `float`             | La valeur sigma minimale pour le niveau de bruit, définissant la limite inférieure pour l'injection de bruit, affectant ainsi la précision d'échantillonnage du modèle. |

## Sorties

| Paramètre | Type de données | Type Python        | Description |
|-----------|-----------------|----------------------|-------------|
| `modèle`   | MODEL           | `torch.nn.Module`   | Le modèle amélioré avec des capacités d'échantillonnage EDM continu intégrées, prêt à être utilisé dans des tâches de génération. |