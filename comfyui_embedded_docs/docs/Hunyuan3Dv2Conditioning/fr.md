# Hunyuan3Dv2Conditioning

Le nœud Hunyuan3Dv2Conditioning traite la sortie de la vision CLIP pour générer des données de conditionnement pour les modèles 3D. Il extrait les plongements (embeddings) du dernier état caché de la sortie de vision et crée des paires de conditionnement positive et négative. Le conditionnement positif utilise les plongements réels tandis que le conditionnement négatif utilise des plongements de valeur nulle de même forme.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip_vision_output` | La sortie d'un modèle de vision CLIP contenant des plongements visuels | CLIP_VISION_OUTPUT | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Données de conditionnement positives contenant les plongements de la vision CLIP | CONDITIONING |
| `negative` | Données de conditionnement négatives contenant des plongements de valeur nulle correspondant à la forme des plongements positifs | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/fr.md)

---
**Source fingerprint (SHA-256):** `114d23574a93bd31013fc909568023c143bba2e4ea75b35a0ebb808c19e83867`
