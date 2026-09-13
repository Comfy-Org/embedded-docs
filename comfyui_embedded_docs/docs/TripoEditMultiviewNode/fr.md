# Tripo : Modifier les vues multiples

Modifie les vues d'un résultat Tripo: Image to Multiview à l'aide d'une instruction textuelle distincte pour chaque vue. Les vues sans instruction restent inchangées. Les images modifiées sont destinées à être connectées à Tripo: Multiview to Model pour créer un modèle 3D ; un ensemble multivue modifié ne peut pas être modifié une seconde fois.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `multiview_task_id` | ID de tâche du résultat Tripo: Image to Multiview dont les vues seront modifiées. Doit provenir du nœud Tripo: Image to Multiview. | MULTIVIEW_TASK_ID | Oui | ID de tâche |
| `front_prompt` | Instruction textuelle décrivant la modification à appliquer à la vue de face. Lorsqu'elle est vide, la vue de face reste inchangée. Par défaut : chaîne vide. | STRING | Non | Texte multiligne |
| `left_prompt` | Instruction textuelle décrivant la modification à appliquer à la vue de gauche. Lorsqu'elle est vide, la vue de gauche reste inchangée. Par défaut : chaîne vide. | STRING | Non | Texte multiligne |
| `back_prompt` | Instruction textuelle décrivant la modification à appliquer à la vue arrière. Lorsqu'elle est vide, la vue arrière reste inchangée. Par défaut : chaîne vide. | STRING | Non | Texte multiligne |
| `right_prompt` | Instruction textuelle décrivant la modification à appliquer à la vue de droite. Lorsqu'elle est vide, la vue de droite reste inchangée. Par défaut : chaîne vide. | STRING | Non | Texte multiligne |

Remarque : au moins l'une des quatre instructions (`front_prompt`, `left_prompt`, `back_prompt`, `right_prompt`) doit contenir du texte non vide ; un texte composé uniquement d'espaces est considéré comme vide, et si toutes les instructions sont vides, le nœud déclenche une erreur.

Remarque : le coût est d'environ 0,05 USD par vue ayant une instruction de modification.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `front` | Image de la vue de face modifiée. | IMAGE |
| `left` | Image de la vue de gauche modifiée. | IMAGE |
| `back` | Image de la vue arrière modifiée. | IMAGE |
| `right` | Image de la vue de droite modifiée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoEditMultiviewNode/fr.md)

---
**Source fingerprint (SHA-256):** `db8b0a3ffe4332fcbcaac4da0d7b07217d01d2f05526750540f6036293e013ab`
