> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/fr.md)

Le nœud Hunyuan3Dv2Conditioning traite la sortie vision de CLIP pour générer des données de conditionnement destinées aux modèles vidéo. Il extrait les embeddings de l'état caché final de la sortie vision et crée des paires de conditionnement positives et négatives. Le conditionnement positif utilise les embeddings réels tandis que le conditionnement négatif utilise des embeddings de valeur zéro de même forme.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `sortie_vision_clip` | CLIP_VISION_OUTPUT | Oui | - | La sortie d'un modèle vision CLIP contenant les embeddings visuels |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `négatif` | CONDITIONING | Données de conditionnement positives contenant les embeddings vision CLIP |
| `negative` | CONDITIONING | Données de conditionnement négatives contenant des embeddings de valeur zéro correspondant à la forme des embeddings positifs |
