# Tripo : Retopologie

Tripo: Retopology prend un modèle 3D haute densité généré par un nœud Tripo précédent et le reconstruit sous forme de version basse densité avec une topologie propre. Il soumet le modèle au service de retopologie Tripo, attend la fin de la tâche, puis télécharge le modèle terminé et expose son ID de tâche pour utilisation par d'autres nœuds Tripo.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model_task_id` | ID de tâche du modèle haute densité source. Accepte un ID de tâche de modèle provenant d'un nœud de génération Tripo ou un ID de tâche de segment provenant de Tripo: Segment Model. | STRING | Oui | ID de tâche Tripo |
| `face_limit` | Nombre cible de faces : 500 à 20 000 triangles ou 500 à 10 000 quads. -1 laisse Tripo choisir. (par défaut : -1) | INT | Oui | -1 (automatique)<br>500 à 20 000 (triangles)<br>500 à 10 000 (quads) |
| `quad` | Sortie de maillage à quads. Tripo livre les maillages à quads au format FBX, donc le résultat arrive sur la sortie FBX et la sortie GLB reste vide. (par défaut : False) | BOOLEAN | Oui | True<br>False (par défaut) |
| `bake` | Applique (bake) les textures sources sur le maillage basse densité. (par défaut : True) | BOOLEAN | Non | True (par défaut)<br>False |
| `part_names` | Noms de parties séparés par des virgules issus de Tripo: Segment Model. Une valeur vide traite le modèle entier. (par défaut : "") | STRING | Non | Noms de parties du modèle ou vide |

Remarque : lorsque `face_limit` est défini sur -1, Tripo décide automatiquement du nombre de faces. Lorsque `quad` est activé, la limite maximale de faces est de 10 000 quads au lieu de 20 000 triangles, et le résultat est fourni au format FBX (la sortie GLB reste vide). Lorsque `part_names` est vide, le modèle entier est traité. Si `face_limit` a une valeur autre que -1 et se situe en dehors de la plage autorisée, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Sortie rétrocompatible qui identifie le fichier de modèle terminé. Les workflows plus récents doivent plutôt utiliser les sorties GLB ou FBX. | STRING |
| `model task_id` | ID de tâche du résultat de retopologie terminé. Peut être transmis à d'autres nœuds Tripo pour référencer ce modèle. | STRING |
| `GLB` | Le modèle basse densité retopologisé au format GLB. Vide lorsque `quad` est activé. | GLB FILE |
| `FBX` | Le modèle basse densité retopologisé au format FBX. Rempli uniquement lorsque `quad` est activé. | FBX FILE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetopologyNode/fr.md)

---
**Source fingerprint (SHA-256):** `b0e967eb4987a70242b6cfce93f09e0caffb7f4bdd3e4f1439e68f33f9138bb5`
