> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAttentionMultiply/fr.md)

Le nœud CLIPAttentionMultiply vous permet d'ajuster le mécanisme d'attention dans les modèles CLIP en appliquant des facteurs de multiplication aux différentes composantes des couches d'auto-attention. Il fonctionne en modifiant les poids et biais de projection des requêtes, clés, valeurs et de sortie dans le mécanisme d'attention du modèle CLIP. Ce nœud expérimental crée une copie modifiée du modèle CLIP d'entrée avec les facteurs d'échelle spécifiés appliqués.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | requis | - | - | Le modèle CLIP à modifier |
| `q` | FLOAT | requis | 1.0 | 0.0 - 10.0 | Facteur de multiplication pour les poids et biais de projection des requêtes |
| `k` | FLOAT | requis | 1.0 | 0.0 - 10.0 | Facteur de multiplication pour les poids et biais de projection des clés |
| `v` | FLOAT | requis | 1.0 | 0.0 - 10.0 | Facteur de multiplication pour les poids et biais de projection des valeurs |
| `out` | FLOAT | requis | 1.0 | 0.0 - 10.0 | Facteur de multiplication pour les poids et biais de projection de sortie |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Retourne un modèle CLIP modifié avec les facteurs d'échelle d'attention spécifiés appliqués |