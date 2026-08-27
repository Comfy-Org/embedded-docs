# LotusConditioning

Le nœud LotusConditioning fournit des embeddings de conditionnement précalculés pour le modèle Lotus. Il utilise un encodeur figé avec un conditionnement nul et renvoie des embeddings de prompt codés en dur pour atteindre la parité avec l'implémentation de référence sans nécessiter d'inférence ni de chargement de fichiers tensoriels volumineux. Ce nœud produit un tenseur de conditionnement fixe qui peut être utilisé directement dans le pipeline de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| *Aucune entrée* | Ce nœud n'accepte aucun paramètre d'entrée. | - | - | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `conditionnement` | Les embeddings de conditionnement précalculés pour le modèle Lotus, contenant des embeddings de prompt fixes et un dictionnaire vide. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `1fcb6530850341253c8acb47b2f26ee79d93f51eca84bef03a1fa5de33d6bc8d`
