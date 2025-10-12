> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/fr.md)

Le nœud FreeU applique des modifications dans le domaine fréquentiel aux blocs de sortie d'un modèle pour améliorer la qualité de génération d'images. Il fonctionne en mettant à l'échelle différents groupes de canaux et en appliquant un filtrage de Fourier à des cartes de caractéristiques spécifiques, permettant un contrôle précis du comportement du modèle pendant le processus de génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle auquel appliquer les modifications FreeU |
| `b1` | FLOAT | Oui | 0.0 - 10.0 | Facteur d'échelle pour les caractéristiques model_channels × 4 (par défaut : 1.1) |
| `b2` | FLOAT | Oui | 0.0 - 10.0 | Facteur d'échelle pour les caractéristiques model_channels × 2 (par défaut : 1.2) |
| `s1` | FLOAT | Oui | 0.0 - 10.0 | Facteur d'échelle des connexions résiduelles pour les caractéristiques model_channels × 4 (par défaut : 0.9) |
| `s2` | FLOAT | Oui | 0.0 - 10.0 | Facteur d'échelle des connexions résiduelles pour les caractéristiques model_channels × 2 (par défaut : 0.2) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `modèle` | MODEL | Le modèle modifié avec les correctifs FreeU appliqués |