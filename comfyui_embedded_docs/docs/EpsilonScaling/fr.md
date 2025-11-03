> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EpsilonScaling/fr.md)

Implémente la méthode Epsilon Scaling issue du document de recherche "Elucidating the Exposure Bias in Diffusion Models". Cette méthode améliore la qualité des échantillons en mettant à l'échelle le bruit prédit pendant le processus d'échantillonnage. Elle utilise un calendrier uniforme pour atténuer le biais d'exposition dans les modèles de diffusion.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle auquel appliquer l'epsilon scaling |
| `scaling_factor` | FLOAT | Non | 0.5 - 1.5 | Le facteur utilisé pour mettre à l'échelle le bruit prédit (par défaut : 1.005) |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle avec l'epsilon scaling appliqué |
