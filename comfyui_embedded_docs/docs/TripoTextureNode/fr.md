> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/fr.md)

Le TripoTextureNode génère des modèles 3D texturés en utilisant l'API Tripo. Il prend un identifiant de tâche de modèle et applique une génération de texture avec diverses options incluant les matériaux PBR, les paramètres de qualité de texture et les méthodes d'alignement. Le nœud communique avec l'API Tripo pour traiter la requête de génération de texture et retourne le fichier de modèle résultant ainsi que l'identifiant de tâche.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | Oui | - | L'identifiant de tâche du modèle auquel appliquer les textures |
| `texture` | BOOLEAN | Non | - | Indique si les textures doivent être générées (par défaut : True) |
| `pbr` | BOOLEAN | Non | - | Indique si les matériaux PBR (Rendu Physiquement Réaliste) doivent être générés (par défaut : True) |
| `texture_seed` | INT | Non | - | Graine aléatoire pour la génération de texture (par défaut : 42) |
| `texture_quality` | COMBO | Non | "standard"<br>"detailed" | Niveau de qualité pour la génération de texture (par défaut : "standard") |
| `texture_alignment` | COMBO | Non | "original_image"<br>"geometry" | Méthode d'alignement des textures (par défaut : "original_image") |

*Note : Ce nœud nécessite des jetons d'authentification et des clés API qui sont gérés automatiquement par le système.*

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model_file` | STRING | Le fichier de modèle généré avec les textures appliquées |
| `model task_id` | MODEL_TASK_ID | L'identifiant de tâche pour suivre le processus de génération de texture |