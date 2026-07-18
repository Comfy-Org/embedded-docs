Voici la traduction en français de la documentation du nœud TripoImageToModelNode :

Génère des modèles 3D de manière synchrone à partir d'une seule image en utilisant l'API Tripo. Ce nœud prend une image en entrée et la convertit en modèle 3D avec diverses options de personnalisation pour la texture, la qualité et les propriétés du modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Image d'entrée utilisée pour générer le modèle 3D | IMAGE | Oui | - |
| `version_modèle` | Version du modèle Tripo à utiliser pour la génération | COMBO | Non | Plusieurs options disponibles |
| `style` | Réglage de style pour le modèle généré (par défaut : "None") | COMBO | Non | Plusieurs options disponibles |
| `texture` | Indique s'il faut générer des textures pour le modèle (par défaut : True) | BOOLEAN | Non | - |
| `pbr` | Indique s'il faut utiliser le rendu basé sur la physique (PBR) (par défaut : True) | BOOLEAN | Non | - |
| `graine_modèle` | Graine aléatoire pour la génération du modèle (par défaut : 42) | INT | Non | - |
| `orientation` | Réglage d'orientation pour le modèle généré | COMBO | Non | Plusieurs options disponibles |
| `graine_texture` | Graine aléatoire pour la génération de la texture (par défaut : 42) | INT | Non | - |
| `qualité_texture` | Niveau de qualité pour la génération de texture (par défaut : "standard") | COMBO | Non | "standard"<br>"detailed" |
| `alignement_texture` | Méthode d'alignement pour le mappage de texture (par défaut : "original_image") | COMBO | Non | "original_image"<br>"geometry" |
| `limite_faces` | Nombre maximum de faces dans le modèle généré, -1 pour aucune limite (par défaut : -1) | INT | Non | -1 à 500000 |
| `quad` | Indique s'il faut utiliser des faces quadrilatérales au lieu de triangles (par défaut : False) | BOOLEAN | Non | - |
| `geometry_quality` | Niveau de qualité pour la génération de géométrie (par défaut : "standard") | COMBO | Non | "standard"<br>"detailed" |

**Remarque :** Le paramètre `image` est requis et doit être fourni pour que le nœud fonctionne. Si aucune image n'est fournie, le nœud générera une erreur RuntimeError.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `fichier_modèle` | Fichier du modèle 3D généré (uniquement pour la rétrocompatibilité) | STRING |
| `modèle task_id` | Identifiant de tâche pour suivre le processus de génération du modèle | MODEL_TASK_ID |
| `GLB` | Modèle 3D généré au format GLB | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `1342de2f9788fac504fa0cfa248d011c04a8874307bb26dac86a7ced43a2809e`
