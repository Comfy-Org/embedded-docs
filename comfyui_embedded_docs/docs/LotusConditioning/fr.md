> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/fr.md)

Le nœud LotusConditioning fournit des embeddings de conditionnement pré-calculés pour le modèle Lotus. Il utilise un encodeur figé avec un conditionnement nul et renvoie des embeddings de prompt codés en dur pour atteindre la parité avec l'implémentation de référence, sans nécessiter d'inférence ni de chargement de fichiers tensoriels volumineux. Ce nœud produit un tenseur de conditionnement fixe pouvant être utilisé directement dans le pipeline de génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| *Aucune entrée* | - | - | - | Ce nœud n'accepte aucun paramètre d'entrée. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `conditioning` | CONDITIONING | Les embeddings de conditionnement pré-calculés pour le modèle Lotus, contenant des embeddings de prompt fixes et un dictionnaire vide. |

---
**Source fingerprint (SHA-256):** `aa428f8c355e2840dadbf634fe27d20c7c323dbe8c21255b40f4dafa12e4a0d0`
