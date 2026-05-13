> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/fr.md)

Le nœud Hunyuan3Dv2ConditioningMultiView traite les embeddings visuels CLIP multi-vues pour la génération vidéo 3D. Il prend en entrée des embeddings optionnels pour les vues avant, gauche, arrière et droite, et les combine avec un encodage positionnel pour créer des données de conditionnement destinées aux modèles vidéo. Le nœud produit à la fois un conditionnement positif à partir des embeddings combinés et un conditionnement négatif avec des valeurs nulles.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `avant` | CLIP_VISION_OUTPUT | Non | - | Sortie visuelle CLIP pour la vue avant |
| `gauche` | CLIP_VISION_OUTPUT | Non | - | Sortie visuelle CLIP pour la vue gauche |
| `arrière` | CLIP_VISION_OUTPUT | Non | - | Sortie visuelle CLIP pour la vue arrière |
| `droite` | CLIP_VISION_OUTPUT | Non | - | Sortie visuelle CLIP pour la vue droite |

**Remarque :** Au moins une entrée de vue doit être fournie pour que le nœud fonctionne. Le nœud ne traitera que les vues contenant des données de sortie CLIP valides.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `negative` | CONDITIONING | Conditionnement positif contenant les embeddings multi-vues combinés avec l'encodage positionnel |
| `negative` | CONDITIONING | Conditionnement négatif avec des valeurs nulles pour l'apprentissage contrastif |

---
**Source fingerprint (SHA-256):** `01998ae9ba7d2ae9a2f6a0b5aee4c03168f935fb9769317cd80d93a7a4b96f13`
