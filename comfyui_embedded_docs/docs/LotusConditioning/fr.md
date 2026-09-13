# LotusConditioning

Le nœud LotusConditioning fournit des embeddings de conditionnement fixes et pré-calculés pour le modèle Lotus. Comme Lotus utilise un encodeur figé avec un conditionnement nul, le nœud intègre directement les embeddings de prompt résultants au lieu d'exécuter une inférence ou de charger des fichiers de tenseurs volumineux ; sa sortie ne change donc jamais. Le conditionnement renvoyé peut être branché directement dans un pipeline de génération qui attend un conditionnement compatible avec Lotus.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| *Aucune entrée* | Ce nœud n'accepte aucun paramètre d'entrée. | - | - | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `conditioning` | Les embeddings de conditionnement pré-calculés pour le modèle Lotus. Renvoyés sous forme de liste de conditionnement contenant les embeddings de prompt fixes ainsi qu'un dictionnaire vide. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `1fcb6530850341253c8acb47b2f26ee79d93f51eca84bef03a1fa5de33d6bc8d`
