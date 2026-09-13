# Hunyuan3Dv2ConditioningMultiView

Le nœud Hunyuan3Dv2ConditioningMultiView combine les sorties CLIP vision de jusqu’à quatre vues (front, left, back et right) en un seul conditionnement multi-vues. Chaque vue fournie reçoit un encodage positionnel ajouté à son embedding CLIP vision, puis les embeddings résultants sont concaténés. Le nœud produit un conditionnement positif basé sur les embeddings combinés et un conditionnement négatif rempli de zéros de même forme.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `front` | Sortie CLIP vision pour la vue de face. Entrée de vue facultative. | CLIP_VISION_OUTPUT | Non | - |
| `left` | Sortie CLIP vision pour la vue de gauche. Entrée de vue facultative. | CLIP_VISION_OUTPUT | Non | - |
| `back` | Sortie CLIP vision pour la vue arrière. Entrée de vue facultative. | CLIP_VISION_OUTPUT | Non | - |
| `right` | Sortie CLIP vision pour la vue de droite. Entrée de vue facultative. | CLIP_VISION_OUTPUT | Non | - |

**Remarque :** Au moins une entrée de vue doit être fournie pour que le nœud fonctionne. Le nœud ne traite que les vues contenant des données de sortie CLIP vision valides et ignore les vues qui ne sont pas connectées. Chaque vue reçoit un encodage positionnel fixe en fonction de son emplacement (`front`, `left`, `back`, `right`), et les embeddings traités de toutes les vues fournies sont assemblés le long de la dimension de séquence.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Conditionnement positif contenant les embeddings multi-vues combinés avec encodage positionnel. | CONDITIONING |
| `negative` | Conditionnement négatif avec des valeurs nulles correspondant à la forme du conditionnement positif. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/fr.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
