> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/fr.md)

Le nœud RenormCFG modifie le processus de classifier-free guidance (CFG) dans les modèles de diffusion en appliquant une mise à l'échelle conditionnelle et une normalisation. Il ajuste le processus de débruitage en fonction de seuils d'étape de temps spécifiés et de facteurs de renormalisation pour contrôler l'influence des prédictions conditionnelles par rapport aux prédictions non conditionnelles pendant la génération d'image.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle de diffusion auquel appliquer le CFG renormalisé |
| `cfg_trunc` | FLOAT | Non | 0.0 - 100.0 | Seuil d'étape de temps pour appliquer la mise à l'échelle CFG (par défaut : 100.0) |
| `renorm_cfg` | FLOAT | Non | 0.0 - 100.0 | Facteur de renormalisation pour contrôler la force du guidage conditionnel (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `modèle` | MODEL | Le modèle modifié avec la fonction CFG renormalisée appliquée |