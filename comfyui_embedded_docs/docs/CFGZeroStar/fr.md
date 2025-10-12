> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGZeroStar/fr.md)

Le nœud CFGZeroStar applique une technique spécialisée de mise à l'échelle du guidage aux modèles de diffusion. Il modifie le processus de guidage sans classifieur en calculant un facteur d'échelle optimisé basé sur la différence entre les prédictions conditionnelles et non conditionnelles. Cette approche ajuste la sortie finale pour offrir un contrôle amélioré du processus de génération tout en maintenant la stabilité du modèle.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `modèle` | MODEL | requis | - | - | Le modèle de diffusion à modifier avec la technique de mise à l'échelle du guidage CFGZeroStar |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `patched_model` | MODEL | Le modèle modifié avec la mise à l'échelle du guidage CFGZeroStar appliquée |