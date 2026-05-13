> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/fr.md)

Le nœud Hunyuan3Dv2Conditioning traite la sortie de la vision CLIP pour générer des données de conditionnement destinées aux modèles 3D. Il extrait les embeddings du dernier état caché de la sortie visuelle et crée des paires de conditionnement positives et négatives. Le conditionnement positif utilise les embeddings réels, tandis que le conditionnement négatif utilise des embeddings de valeur nulle de la même forme.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `clip_vision_output` | CLIP_VISION_OUTPUT | Oui | - | La sortie d'un modèle de vision CLIP contenant des embeddings visuels |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `positive` | CONDITIONING | Données de conditionnement positives contenant les embeddings de la vision CLIP |
| `negative` | CONDITIONING | Données de conditionnement négatives contenant des embeddings de valeur nulle correspondant à la forme des embeddings positifs |

---
**Source fingerprint (SHA-256):** `3a32967d62a0645b0c375b17ab96e20805c2e0005e585dddf5a3a77d35994fec`
