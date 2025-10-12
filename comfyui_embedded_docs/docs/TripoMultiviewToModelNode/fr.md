> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/fr.md)

Ce nœud génère des modèles 3D de manière synchrone en utilisant l'API de Tripo en traitant jusqu'à quatre images montrant différentes vues d'un objet. Il nécessite une image de face et au moins une vue supplémentaire (gauche, arrière ou droite) pour créer un modèle 3D complet avec des options de texture et de matériaux.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | Image de vue de face de l'objet (requise) |
| `image_left` | IMAGE | Non | - | Image de vue de gauche de l'objet |
| `image_back` | IMAGE | Non | - | Image de vue arrière de l'objet |
| `image_right` | IMAGE | Non | - | Image de vue de droite de l'objet |
| `model_version` | COMBO | Non | Plusieurs options disponibles | Version du modèle Tripo à utiliser pour la génération |
| `orientation` | COMBO | Non | Plusieurs options disponibles | Paramètre d'orientation pour le modèle 3D |
| `texture` | BOOLEAN | Non | - | Indique si les textures doivent être générées pour le modèle (par défaut : True) |
| `pbr` | BOOLEAN | Non | - | Indique si les matériaux PBR (Physically Based Rendering) doivent être générés (par défaut : True) |
| `model_seed` | INT | Non | - | Graine aléatoire pour la génération du modèle (par défaut : 42) |
| `texture_seed` | INT | Non | - | Graine aléatoire pour la génération des textures (par défaut : 42) |
| `texture_quality` | COMBO | Non | "standard"<br>"detailed" | Niveau de qualité pour la génération des textures (par défaut : "standard") |
| `texture_alignment` | COMBO | Non | "original_image"<br>"geometry" | Méthode d'alignement des textures sur le modèle (par défaut : "original_image") |
| `face_limit` | INT | Non | -1 à 500000 | Nombre maximum de faces dans le modèle généré, -1 pour aucune limite (par défaut : -1) |
| `quad` | BOOLEAN | Non | - | Indique si la géométrie doit être générée en quadrilatères au lieu de triangles (par défaut : False) |

**Note :** L'image de face (`image`) est toujours requise. Au moins une image de vue supplémentaire (`image_left`, `image_back` ou `image_right`) doit être fournie pour le traitement multivue.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model_file` | STRING | Chemin du fichier ou identifiant pour le modèle 3D généré |
| `model task_id` | MODEL_TASK_ID | Identifiant de tâche pour suivre le processus de génération du modèle |
