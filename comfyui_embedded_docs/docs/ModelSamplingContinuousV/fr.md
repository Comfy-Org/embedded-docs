> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/fr.md)

Le nœud ModelSamplingContinuousV modifie le comportement d'échantillonnage d'un modèle en appliquant des paramètres d'échantillonnage par prédiction V continue. Il crée un clone du modèle d'entrée et le configure avec des paramètres personnalisés de plage sigma pour un contrôle avancé de l'échantillonnage. Cela permet aux utilisateurs d'affiner le processus d'échantillonnage avec des valeurs sigma minimum et maximum spécifiques.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle d'entrée à modifier avec l'échantillonnage par prédiction V continue |
| `sampling` | STRING | Oui | "v_prediction" | La méthode d'échantillonnage à appliquer (seule la prédiction V est actuellement supportée) |
| `sigma_max` | FLOAT | Oui | 0.0 - 1000.0 | La valeur sigma maximale pour l'échantillonnage (par défaut : 500.0) |
| `sigma_min` | FLOAT | Oui | 0.0 - 1000.0 | La valeur sigma minimale pour l'échantillonnage (par défaut : 0.03) |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle modifié avec l'échantillonnage par prédiction V continue appliqué |