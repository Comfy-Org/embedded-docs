# TripoEditMultiviewNode

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `multiview_task_id` | ID de tâche du résultat Tripo : Image to Multiview dont les vues seront modifiées. | MULTIVIEW_TASK_ID | Oui | ID de tâche |
| `front_prompt` | Instruction textuelle décrivant la modification à appliquer à la vue avant. Si elle est vide, la vue avant reste inchangée. Par défaut : vide. | STRING | Non | Texte multiligne |
| `left_prompt` | Instruction textuelle décrivant la modification à appliquer à la vue gauche. Si elle est vide, la vue gauche reste inchangée. Par défaut : vide. | STRING | Non | Texte multiligne |
| `back_prompt` | Instruction textuelle décrivant la modification à appliquer à la vue arrière. Si elle est vide, la vue arrière reste inchangée. Par défaut : vide. | STRING | Non | Texte multiligne |
| `right_prompt` | Instruction textuelle décrivant la modification à appliquer à la vue droite. Si elle est vide, la vue droite reste inchangée. Par défaut : vide. | STRING | Non | Texte multiligne |

Remarque : Au moins une des quatre instructions (`front_prompt`, `left_prompt`, `back_prompt`, `right_prompt`) doit contenir du texte non vide ; sinon, le nœud génère une erreur. Le `multiview_task_id` doit provenir du nœud Tripo : Image to Multiview. Un ensemble de vues modifié ne peut pas être modifié de nouveau.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `front` | Image de la vue avant modifiée. | IMAGE |
| `gauche` | Image de la vue gauche modifiée. | IMAGE |
| `arrière` | Image de la vue arrière modifiée. | IMAGE |
| `droite` | Image de la vue droite modifiée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoEditMultiviewNode/fr.md)

---
**Source fingerprint (SHA-256):** `7a25f3867776c01ab606d43a988b5491e543b72d3eedac1779fa170453c1ca21`
