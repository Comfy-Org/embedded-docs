# Hunyuan3Dv2ConditioningMultiView

Le nœud Hunyuan3Dv2ConditioningMultiView traite les embeddings de vision CLIP multi-vues pour la génération de vidéos 3D. Il prend en entrée des embeddings optionnels pour les vues avant, gauche, arrière et droite, et ajoute un encodage positionnel à chaque vue fournie avant de les combiner en une seule séquence de conditionnement. Le nœud produit à la fois un conditionnement positif à partir des embeddings combinés et un conditionnement négatif avec des valeurs nulles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `front` | Sortie de vision CLIP pour la vue avant | CLIP_VISION_OUTPUT | Non | - |
| `left` | Sortie de vision CLIP pour la vue gauche | CLIP_VISION_OUTPUT | Non | - |
| `back` | Sortie de vision CLIP pour la vue arrière | CLIP_VISION_OUTPUT | Non | - |
| `right` | Sortie de vision CLIP pour la vue droite | CLIP_VISION_OUTPUT | Non | - |

**Remarque :** Au moins une vue d’entrée doit être fournie pour que le nœud fonctionne. Le nœud ne traite que les vues qui contiennent des données de sortie de vision CLIP valides. Chaque vue fournie reçoit un encodage positionnel basé sur sa position de vue (avant, gauche, arrière, droite), et les vues encodées sont concaténées dans cet ordre.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif contenant les embeddings multi-vues combinés avec encodage positionnel | CONDITIONING |
| `negative` | Conditionnement négatif contenant des valeurs nulles avec la même forme que le conditionnement positif | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/fr.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
