> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/fr.md)

Le nœud CFGNorm applique une technique de normalisation au processus de guidance sans classifieur (CFG) dans les modèles de diffusion. Il ajuste l'échelle de la prédiction débruitée en comparant les normes des sorties conditionnelles et non conditionnelles, puis applique un multiplicateur de force pour contrôler l'effet. Cela contribue à stabiliser le processus de génération en évitant les valeurs extrêmes dans la mise à l'échelle de la guidance.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | requis | - | - | Le modèle de diffusion auquel appliquer la normalisation CFG |
| `strength` | FLOAT | requis | 1.0 | 0.0 - 100.0 | Contrôle l'intensité de l'effet de normalisation appliqué à la mise à l'échelle CFG |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `patched_model` | MODEL | Retourne le modèle modifié avec la normalisation CFG appliquée à son processus d'échantillonnage |