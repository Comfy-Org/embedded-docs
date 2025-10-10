> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/fr.md)

Le nœud Hunyuan3Dv2ConditioningMultiView traite les embeddings visuels CLIP multi-vues pour la génération de vidéos 3D. Il prend en entrée des embeddings optionnels pour les vues avant, gauche, arrière et droite, et les combine avec un encodage positionnel pour créer des données de conditionnement destinées aux modèles vidéo. Le nœud produit à la fois un conditionnement positif à partir des embeddings combinés et un conditionnement négatif avec des valeurs nulles.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `front` | CLIP_VISION_OUTPUT | Non | - | Sortie CLIP vision pour la vue avant |
| `left` | CLIP_VISION_OUTPUT | Non | - | Sortie CLIP vision pour la vue gauche |
| `back` | CLIP_VISION_OUTPUT | Non | - | Sortie CLIP vision pour la vue arrière |
| `right` | CLIP_VISION_OUTPUT | Non | - | Sortie CLIP vision pour la vue droite |

**Remarque :** Au moins une entrée de vue doit être fournie pour que le nœud fonctionne. Le nœud ne traitera que les vues contenant des données valides de sortie CLIP vision.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Conditionnement positif contenant les embeddings multi-vues combinés avec l'encodage positionnel |
| `negative` | CONDITIONING | Conditionnement négatif avec des valeurs nulles pour l'apprentissage contrastif |