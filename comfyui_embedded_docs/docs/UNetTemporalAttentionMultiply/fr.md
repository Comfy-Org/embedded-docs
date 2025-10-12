> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetTemporalAttentionMultiply/fr.md)

Le nœud UNetTemporalAttentionMultiply applique des facteurs de multiplication à différents types de mécanismes d'attention dans un modèle UNet temporel. Il modifie le modèle en ajustant les pondérations des couches d'auto-attention et d'attention croisée, en distinguant les composantes structurelles et temporelles. Cela permet d'affiner l'influence de chaque type d'attention sur la sortie du modèle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle d'entrée à modifier avec les multiplicateurs d'attention |
| `self_structural` | FLOAT | Non | 0.0 - 10.0 | Multiplicateur pour les composantes structurelles de l'auto-attention (par défaut : 1.0) |
| `self_temporal` | FLOAT | Non | 0.0 - 10.0 | Multiplicateur pour les composantes temporelles de l'auto-attention (par défaut : 1.0) |
| `cross_structural` | FLOAT | Non | 0.0 - 10.0 | Multiplicateur pour les composantes structurelles de l'attention croisée (par défaut : 1.0) |
| `cross_temporal` | FLOAT | Non | 0.0 - 10.0 | Multiplicateur pour les composantes temporelles de l'attention croisée (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle modifié avec les pondérations d'attention ajustées |