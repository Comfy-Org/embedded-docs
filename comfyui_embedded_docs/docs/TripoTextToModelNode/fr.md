> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/fr.md)

Génère des modèles 3D de manière synchrone à partir d'une invite textuelle en utilisant l'API de Tripo. Ce nœud prend une description textuelle et crée un modèle 3D avec des propriétés optionnelles de texture et de matériaux.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Description textuelle pour générer le modèle 3D (saisie multiligne) |
| `negative_prompt` | STRING | Non | - | Description textuelle de ce qu'il faut éviter dans le modèle généré (saisie multiligne) |
| `model_version` | COMBO | Non | Plusieurs options disponibles | La version du modèle Tripo à utiliser pour la génération |
| `style` | COMBO | Non | Plusieurs options disponibles | Paramètre de style pour le modèle généré (par défaut : "Aucun") |
| `texture` | BOOLEAN | Non | - | Indique s'il faut générer des textures pour le modèle (par défaut : True) |
| `pbr` | BOOLEAN | Non | - | Indique s'il faut générer des matériaux PBR (Rendu Physiquement Réaliste) (par défaut : True) |
| `image_seed` | INT | Non | - | Graine aléatoire pour la génération d'image (par défaut : 42) |
| `model_seed` | INT | Non | - | Graine aléatoire pour la génération du modèle (par défaut : 42) |
| `texture_seed` | INT | Non | - | Graine aléatoire pour la génération de texture (par défaut : 42) |
| `texture_quality` | COMBO | Non | "standard"<br>"detailed" | Niveau de qualité pour la génération de texture (par défaut : "standard") |
| `face_limit` | INT | Non | -1 à 500000 | Nombre maximum de faces dans le modèle généré, -1 pour aucune limite (par défaut : -1) |
| `quad` | BOOLEAN | Non | - | Indique s'il faut générer une géométrie basée sur des quadrilatères au lieu de triangles (par défaut : False) |

**Note :** Le paramètre `prompt` est requis et ne peut pas être vide. Si aucune invite n'est fournie, le nœud générera une erreur.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model_file` | STRING | Le fichier du modèle 3D généré |
| `model task_id` | MODEL_TASK_ID | L'identifiant unique de tâche pour le processus de génération du modèle |
