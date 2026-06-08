Ce nœud est conçu pour améliorer les capacités d'échantillonnage d'un modèle en intégrant des techniques d'échantillonnage EDM (Energy-based Diffusion Models) continu. Il permet un ajustement dynamique des niveaux de bruit dans le processus d'échantillonnage du modèle, offrant un contrôle plus précis sur la qualité et la diversité de la génération.

## Entrées

| Paramètre | Description | Type de données | Type Python |
| --- | --- | --- | --- |
| `modèle` | Le modèle à améliorer avec des capacités d'échantillonnage EDM continu. Il sert de base pour l'application des techniques d'échantillonnage avancées. | `MODEL` | `torch.nn.Module` |
| `échantillonnage` | Spécifie le type d'échantillonnage à appliquer, soit 'eps' pour l'échantillonnage epsilon, soit 'v_prediction' pour la prédiction de vélocité, influençant le comportement du modèle pendant le processus d'échantillonnage. | COMBO[STRING] | `str` |
| `sigma_max` | La valeur sigma maximale pour le niveau de bruit, permettant un contrôle de la limite supérieure dans le processus d'injection de bruit pendant l'échantillonnage. | `FLOAT` | `float` |
| `sigma_min` | La valeur sigma minimale pour le niveau de bruit, définissant la limite inférieure pour l'injection de bruit, affectant ainsi la précision d'échantillonnage du modèle. | `FLOAT` | `float` |

## Sorties

| Paramètre | Description | Type de données | Type Python |
| --- | --- | --- | --- |
| `modèle` | Le modèle amélioré avec des capacités d'échantillonnage EDM continu intégrées, prêt à être utilisé dans des tâches de génération. | MODEL | `torch.nn.Module` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousEDM/fr.md)
