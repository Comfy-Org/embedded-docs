# ByteDance Seedance 2.5 Draft to Final Video

Ce nœud effectue le rendu de la vidéo finale 1080p d'un Seedance 2.5 Draft. Un draft est un aperçu rapide en 480p : dans un nœud vidéo Seedance 2.5 (texte vers vidéo, première-dernière image vers vidéo, ou référence vers vidéo), définissez `model` sur `Seedance 2.5 Draft`, exécutez-le, puis connectez ici sa sortie `draft_task_id`. La vidéo finale conserve la scène et le mouvement du draft, et réutilise le prompt, les références, la durée, le rapport d'aspect et le réglage audio qui ont produit le draft.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `draft_task_id` | La sortie `draft_task_id` d'un nœud Seedance 2.5 exécuté avec le modèle Seedance 2.5 Draft, ou un ID de tâche de draft collé. Lorsque vous réexécutez le nœud producteur, réglez son contrôle de seed sur fixe, sinon l'exécution suivante génère un nouveau draft au lieu de réutiliser celui que vous avez examiné. | STRING | Oui | - |
| `watermark` | Indique s'il faut ajouter un filigrane à la vidéo. La valeur par défaut est False. Il s'agit d'un réglage avancé. | BOOLEAN | Non | True / False |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo finale 1080p rendue, téléchargée depuis le fournisseur une fois la tâche de rendu terminée. | VIDEO |

**Remarque :** Un draft peut être rendu pendant 7 jours après sa création. L'ID de tâche du draft identifie le draft à lui seul, donc le prompt, les références, la durée, le rapport d'aspect et le réglage audio n'ont pas besoin d'être transmis à nouveau.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2DraftToFinalVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `c9a607826915f09ec199748964010a00a239b5efab3647a3b97fdceee6b04cde`
