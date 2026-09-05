# TripoImageToMultiviewNode

Génère les vues de face, de gauche, de dos et de droite du sujet à partir d’une image d’entrée unique, via l’API Tripo. Cette opération est payante et facturée environ 0,10 USD. Le nœud téléverse l’image, attend la fin de la tâche de génération Tripo, puis renvoie les quatre vues ainsi que l’identifiant de la tâche multivue.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L’image source du sujet à partir de laquelle Tripo génère les vues de face, de gauche, de dos et de droite. Une seule image est utilisée pour la requête. | IMAGE | Oui | Image unique |

Remarque : Le nœud appelle l’API cloud de Tripo et attend la fin de la tâche de génération. Une tâche typique prend environ 25 secondes. L’authentification est gérée automatiquement via les entrées cachées du nœud, aucune clé API Tripo n’est donc requise dans le workflow.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `task_id multivue` | L’identifiant de la tâche renvoyé par Tripo pour la requête de génération d’images multivues. Il s’agit d’un identifiant de type chaîne pouvant être utilisé pour référencer la tâche terminée. | MULTIVIEW_TASK_ID |
| `avant` | La vue de face générée du sujet. | IMAGE |
| `gauche` | La vue du côté gauche générée du sujet. | IMAGE |
| `arrière` | La vue de dos générée du sujet. | IMAGE |
| `droite` | La vue du côté droit générée du sujet. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToMultiviewNode/fr.md)

---
**Source fingerprint (SHA-256):** `3beca1feeb88aa080330e6867ffd7076bd45b2c52471d1bfacc71f66452211a5`
