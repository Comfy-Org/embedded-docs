# Hunyuan3Dv2ConditioningMultiView

Le nœud Hunyuan3Dv2ConditioningMultiView combine les sorties de vision CLIP de jusqu'à quatre vues (avant, gauche, arrière et droite) en un unique conditionnement multi-vues. Chaque vue fournie reçoit un encodage positionnel ajouté à son plongement de vision CLIP, puis les plongements résultants sont concaténés. Le nœud produit un conditionnement positif basé sur les plongements combinés et un conditionnement négatif rempli de zéros de la même forme.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `avant` | Sortie de vision CLIP pour la vue avant. Entrée de vue facultative. | CLIP_VISION_OUTPUT | Non | - |
| `gauche` | Sortie de vision CLIP pour la vue gauche. Entrée de vue facultative. | CLIP_VISION_OUTPUT | Non | - |
| `arrière` | Sortie de vision CLIP pour la vue arrière. Entrée de vue facultative. | CLIP_VISION_OUTPUT | Non | - |
| `droite` | Sortie de vision CLIP pour la vue droite. Entrée de vue facultative. | CLIP_VISION_OUTPUT | Non | - |

**Remarque :** Au moins une entrée de vue doit être fournie pour que le nœud fonctionne. Le nœud ne traite que les vues contenant des données de sortie de vision CLIP valides et ignore les vues non connectées.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif contenant les plongements multi-vues combinés avec l'encodage positionnel. | CONDITIONING |
| `negative` | Conditionnement négatif avec des valeurs nulles correspondant à la forme du conditionnement positif. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/fr.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
