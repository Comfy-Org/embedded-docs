# TripoRetopologyNode

Tripo: Retopology prend un modèle 3D haute polygones généré par un nœud Tripo précédent et le reconstruit en une version basse polygones avec une topologie propre. Il soumet le modèle au service de retopologie Tripo, attend la fin de la tâche, puis télécharge le modèle terminé et expose son ID de tâche pour que d’autres nœuds Tripo puissent l’utiliser.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_task_id` | ID de tâche du modèle source haute polygones. Accepte un ID de tâche de modèle provenant d’un nœud de génération Tripo ou un ID de tâche de segment provenant de Tripo: Segment Model. | STRING | Oui | ID de tâche Tripo |
| `face_limit` | Nombre de faces cible : 500 à 20 000 triangles ou 500 à 10 000 quads. -1 laisse Tripo choisir. (par défaut : -1) | INT | Oui | -1 (automatique)<br>500 à 20 000 (triangles)<br>500 à 10 000 (quads) |
| `quad` | Sortie en maillage quadrangulaire. Tripo fournit les maillages quadrangulaires au format FBX ; le résultat arrive donc sur la sortie FBX et la sortie GLB reste vide. (par défaut : False) | BOOLEAN | Oui | True<br>False (par défaut) |
| `bake` | Cuit les textures de la source sur le maillage basse polygones. (par défaut : True) | BOOLEAN | Non | True (par défaut)<br>False |
| `part_names` | Noms de pièces séparés par des virgules provenant de Tripo: Segment Model. Une valeur vide traite la totalité du modèle. (par défaut : "") | STRING | Non | Noms de pièces du modèle ou vide |

Remarque : Lorsque `face_limit` est défini sur -1, Tripo choisit automatiquement le nombre de faces. Lorsque `quad` est activé, la limite maximale de faces est de 10 000 quads au lieu de 20 000 triangles, et le résultat est fourni au format FBX (la sortie GLB reste vide). Lorsque `part_names` est vide, la totalité du modèle est traitée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Sortie rétrocompatible qui identifie le fichier de modèle terminé. Les nouveaux flux de travail devraient plutôt utiliser les sorties GLB ou FBX. | STRING |
| `ID de tâche du modèle` | ID de tâche du résultat de retopologie terminé. Peut être passé à d’autres nœuds Tripo pour référencer ce modèle. | STRING |
| `GLB` | Le modèle basse polygones retopologisé au format GLB. Vide lorsque `quad` est activé. | GLB FILE |
| `FBX` | Le modèle basse polygones retopologisé au format FBX. Rempli uniquement lorsque `quad` est activé. | FBX FILE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetopologyNode/fr.md)

---
**Source fingerprint (SHA-256):** `dc15f469b160a1d738e8089cf18de4a8262721bc77ebafa45bf194f04c7726b6`
