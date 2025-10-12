> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/fr.md)

Génère des modèles 3D de manière synchrone à partir d'une seule image en utilisant l'API de Tripo. Ce nœud prend une image en entrée et la convertit en un modèle 3D avec diverses options de personnalisation pour la texture, la qualité et les propriétés du modèle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | Image d'entrée utilisée pour générer le modèle 3D |
| `model_version` | COMBO | Non | Plusieurs options disponibles | La version du modèle Tripo à utiliser pour la génération |
| `style` | COMBO | Non | Plusieurs options disponibles | Paramètre de style pour le modèle généré (par défaut : "Aucun") |
| `texture` | BOOLEAN | Non | - | Indique s'il faut générer des textures pour le modèle (par défaut : True) |
| `pbr` | BOOLEAN | Non | - | Indique s'il faut utiliser le rendu physiquement réaliste (PBR) (par défaut : True) |
| `model_seed` | INT | Non | - | Graine aléatoire pour la génération du modèle (par défaut : 42) |
| `orientation` | COMBO | Non | Plusieurs options disponibles | Paramètre d'orientation pour le modèle généré |
| `texture_seed` | INT | Non | - | Graine aléatoire pour la génération de texture (par défaut : 42) |
| `texture_quality` | COMBO | Non | "standard"<br>"detailed" | Niveau de qualité pour la génération de texture (par défaut : "standard") |
| `texture_alignment` | COMBO | Non | "original_image"<br>"geometry" | Méthode d'alignement pour le mappage de texture (par défaut : "original_image") |
| `face_limit` | INT | Non | -1 à 500000 | Nombre maximum de faces dans le modèle généré, -1 pour aucune limite (par défaut : -1) |
| `quad` | BOOLEAN | Non | - | Indique s'il faut utiliser des faces quadrilatérales au lieu de triangles (par défaut : False) |

**Note :** Le paramètre `image` est requis et doit être fourni pour que le nœud fonctionne. Si aucune image n'est fournie, le nœud générera une RuntimeError.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model_file` | STRING | Le fichier du modèle 3D généré |
| `model task_id` | MODEL_TASK_ID | L'identifiant de tâche pour suivre le processus de génération du modèle |