# ByteDance Seedance 2.5 Draft vers vidéo finale

Ce nœud effectue le rendu de la vidéo finale d'un Seedance 2.5 Draft en 1080p, ou en 4k pour les comptes d'entreprise. Un brouillon est un aperçu rapide en 480p : dans un nœud vidéo Seedance 2.5 (texte vers vidéo, première et dernière image vers vidéo, ou référence vers vidéo), définissez `model` sur `Seedance 2.5 Draft`, exécutez-le, puis connectez sa sortie `draft_task_id` ici. Le rendu final conserve la scène et le mouvement du brouillon, et réutilise le prompt, les références, la durée, le rapport d'aspect et le réglage audio qui ont produit le brouillon.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `draft_task_id` | La sortie `draft_task_id` d'un nœud Seedance 2.5 exécuté avec le modèle Seedance 2.5 Draft, ou un ID de tâche de brouillon collé. Lorsque vous réexécutez le nœud producteur, définissez son contrôle de graine sur fixed ; sinon, l'exécution suivante génère un nouveau brouillon au lieu de réutiliser celui que vous avez examiné. | STRING | Oui | - |
| `watermark` | Indique s'il faut ajouter un filigrane à la vidéo. La valeur par défaut est False. Il s'agit d'un paramètre avancé. | BOOLEAN | Non | True / False |
| `resolution` | Résolution de la vidéo finale. `"4k"` est disponible uniquement pour les comptes d'entreprise. Valeur par défaut : `"1080p"`. | COMBO | Non | `"1080p"`<br>`"4k"` |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo finale rendue, téléchargée depuis le fournisseur une fois la tâche de rendu terminée. | VIDEO |

**Remarque :** Un brouillon peut être rendu pendant 7 jours après sa création. L'ID de tâche du brouillon identifie le brouillon à lui seul, il n'est donc pas nécessaire de transmettre à nouveau le prompt, les références, la durée, le rapport d'aspect et le réglage audio.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2DraftToFinalVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `bf96a485d5febde26e22433d190cfe42bd21dc6316d66141ad23d4b95a845dc5`
