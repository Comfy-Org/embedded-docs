> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/fr.md)

Le nœud PerturbedAttentionGuidance applique un guidage par attention perturbée à un modèle de diffusion pour améliorer la qualité de la génération. Il modifie le mécanisme d'auto-attention du modèle pendant l'échantillonnage en le remplaçant par une version simplifiée qui se concentre sur les projections de valeur. Cette technique aide à améliorer la cohérence et la qualité des images générées en ajustant le processus de débruitage conditionnel.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle de diffusion auquel appliquer le guidage par attention perturbée |
| `échelle` | FLOAT | Non | 0.0 - 100.0 | L'intensité de l'effet de guidage par attention perturbée (par défaut : 3.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `modèle` | MODEL | Le modèle modifié avec le guidage par attention perturbée appliqué |