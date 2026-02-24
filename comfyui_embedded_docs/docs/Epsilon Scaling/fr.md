> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](<https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon> Scaling/fr.md)

Ce nœud implémente la méthode Epsilon Scaling issue de l'article de recherche "Elucidating the Exposure Bias in Diffusion Models". Il fonctionne en mettant à l'échelle le bruit prédit pendant le processus d'échantillonnage pour aider à réduire le biais d'exposition, ce qui peut conduire à une amélioration de la qualité des images générées. Cette implémentation utilise le "planificateur uniforme" recommandé par l'article.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle auquel le correctif de mise à l'échelle epsilon sera appliqué. |
| `scaling_factor` | FLOAT | Non | 0.5 - 1.5 | Le facteur par lequel le bruit prédit est mis à l'échelle. Une valeur supérieure à 1.0 réduit le bruit, tandis qu'une valeur inférieure à 1.0 l'augmente (par défaut : 1.005). |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Une version corrigée du modèle d'entrée avec la fonction de mise à l'échelle epsilon appliquée à son processus d'échantillonnage. |
