# Hunyuan3Dv2Conditioning

Le nœud Hunyuan3Dv2Conditioning traite la sortie de vision CLIP pour générer des données de conditionnement pour les modèles 3D. Il extrait les plongements du dernier état caché de la sortie visuelle et crée des paires de conditionnement positives et négatives. Le conditionnement positif utilise les plongements réels tandis que le conditionnement négatif utilise des plongements nuls de même forme.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `sortie_vision_clip` | La sortie d'un modèle de vision CLIP contenant des plongements visuels | CLIP_VISION_OUTPUT | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Données de conditionnement positives contenant les plongements de vision CLIP | CONDITIONING |
| `negative` | Données de conditionnement négatives contenant des plongements nuls correspondant à la forme des plongements positifs | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/fr.md)

---
**Source fingerprint (SHA-256):** `114d23574a93bd31013fc909568023c143bba2e4ea75b35a0ebb808c19e83867`
