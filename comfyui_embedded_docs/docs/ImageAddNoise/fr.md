> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageAddNoise/fr.md)

Le nœud ImageAddNoise ajoute du bruit aléatoire à une image d'entrée. Il utilise une graine aléatoire spécifiée pour générer des motifs de bruit cohérents et permet de contrôler l'intensité de l'effet de bruit. L'image résultante conserve les mêmes dimensions que l'entrée mais avec une texture visuelle ajoutée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à laquelle le bruit sera ajouté |
| `seed` | INT | Oui | 0 à 18446744073709551615 | La graine aléatoire utilisée pour créer le bruit (défaut : 0) |
| `strength` | FLOAT | Oui | 0.0 à 1.0 | Contrôle l'intensité de l'effet de bruit (défaut : 0.5) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image de sortie avec le bruit ajouté appliqué |