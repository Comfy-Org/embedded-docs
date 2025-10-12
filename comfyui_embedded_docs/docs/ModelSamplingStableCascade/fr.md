> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/fr.md)

Le nœud ModelSamplingStableCascade applique un échantillonnage en cascade stable à un modèle en ajustant les paramètres d'échantillonnage avec une valeur de décalage. Il crée une version modifiée du modèle d'entrée avec une configuration d'échantillonnage personnalisée pour la génération en cascade stable.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle d'entrée auquel appliquer l'échantillonnage en cascade stable |
| `shift` | FLOAT | Oui | 0.0 - 100.0 | La valeur de décalage à appliquer aux paramètres d'échantillonnage (par défaut : 2.0) |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle modifié avec l'échantillonnage en cascade stable appliqué |