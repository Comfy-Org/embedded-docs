
Ce nœud est conçu pour améliorer les capacités d'échantillonnage d'un modèle en intégrant des techniques d'échantillonnage EDM (Energy-based Diffusion Models) continues. Il permet l'ajustement dynamique des niveaux de bruit dans le processus d'échantillonnage du modèle, offrant un contrôle plus raffiné sur la qualité et la diversité de la génération.

## Entrées

| Paramètre   | Data Type | Python dtype        | Description |
|-------------|--------------|----------------------|-------------|
| `model`     | `MODEL`     | `torch.nn.Module`   | Le modèle à améliorer avec des capacités d'échantillonnage EDM continues. Il sert de base pour appliquer les techniques d'échantillonnage avancées. |
| `sampling`  | COMBO[STRING] | `str`             | Spécifie le type d'échantillonnage à appliquer, soit 'eps' pour l'échantillonnage epsilon, soit 'v_prediction' pour la prédiction de vitesse, influençant le comportement du modèle pendant le processus d'échantillonnage. |
| `sigma_max` | `FLOAT`     | `float`             | La valeur sigma maximale pour le niveau de bruit, permettant un contrôle de la limite supérieure dans le processus d'injection de bruit pendant l'échantillonnage. |
| `sigma_min` | `FLOAT`     | `float`             | La valeur sigma minimale pour le niveau de bruit, fixant la limite inférieure pour l'injection de bruit, affectant ainsi la précision de l'échantillonnage du modèle. |

## Sorties

| Paramètre | Data Type | Python dtype        | Description |
|-----------|-------------|----------------------|-------------|
| `model`   | MODEL     | `torch.nn.Module`   | Le modèle amélioré avec des capacités d'échantillonnage EDM continues intégrées, prêt pour une utilisation ultérieure dans des tâches de génération. |
