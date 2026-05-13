> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/fr.md)

Voici la traduction en français de la documentation du nœud TripoImageToModelNode :

Génère des modèles 3D de manière synchrone à partir d'une seule image en utilisant l'API Tripo. Ce nœud prend une image en entrée et la convertit en modèle 3D avec diverses options de personnalisation pour la texture, la qualité et les propriétés du modèle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | - | Image d'entrée utilisée pour générer le modèle 3D |
| `version_modèle` | COMBO | Non | Plusieurs options disponibles | Version du modèle Tripo à utiliser pour la génération |
| `style` | COMBO | Non | Plusieurs options disponibles | Réglage de style pour le modèle généré (par défaut : "None") |
| `texture` | BOOLEAN | Non | - | Indique s'il faut générer des textures pour le modèle (par défaut : True) |
| `pbr` | BOOLEAN | Non | - | Indique s'il faut utiliser le rendu basé sur la physique (PBR) (par défaut : True) |
| `graine_modèle` | INT | Non | - | Graine aléatoire pour la génération du modèle (par défaut : 42) |
| `orientation` | COMBO | Non | Plusieurs options disponibles | Réglage d'orientation pour le modèle généré |
| `graine_texture` | INT | Non | - | Graine aléatoire pour la génération de la texture (par défaut : 42) |
| `qualité_texture` | COMBO | Non | "standard"<br>"detailed" | Niveau de qualité pour la génération de texture (par défaut : "standard") |
| `alignement_texture` | COMBO | Non | "original_image"<br>"geometry" | Méthode d'alignement pour le mappage de texture (par défaut : "original_image") |
| `limite_faces` | INT | Non | -1 à 500000 | Nombre maximum de faces dans le modèle généré, -1 pour aucune limite (par défaut : -1) |
| `quad` | BOOLEAN | Non | - | Indique s'il faut utiliser des faces quadrilatérales au lieu de triangles (par défaut : False) |
| `geometry_quality` | COMBO | Non | "standard"<br>"detailed" | Niveau de qualité pour la génération de géométrie (par défaut : "standard") |

**Remarque :** Le paramètre `image` est requis et doit être fourni pour que le nœud fonctionne. Si aucune image n'est fournie, le nœud générera une erreur RuntimeError.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `modèle task_id` | STRING | Fichier du modèle 3D généré (uniquement pour la rétrocompatibilité) |
| `GLB` | MODEL_TASK_ID | Identifiant de tâche pour suivre le processus de génération du modèle |
| `GLB` | FILE3DGLB | Modèle 3D généré au format GLB |

---
**Source fingerprint (SHA-256):** `1342de2f9788fac504fa0cfa248d011c04a8874307bb26dac86a7ced43a2809e`
