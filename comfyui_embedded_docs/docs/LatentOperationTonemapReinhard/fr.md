> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/fr.md)

Le nœud LatentOperationTonemapReinhard applique un mappage de ton Reinhard aux vecteurs latents. Cette technique normalise les vecteurs latents et ajuste leur magnitude en utilisant une approche statistique basée sur la moyenne et l'écart-type, avec l'intensité contrôlée par un paramètre multiplicateur.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `multiplicateur` | FLOAT | Non | 0.0 à 100.0 | Contrôle l'intensité de l'effet de mappage de ton (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `operation` | LATENT_OPERATION | Retourne une opération de mappage de ton qui peut être appliquée aux vecteurs latents |
