> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/fr.md)

Ce nœud génère des modèles 3D de manière synchrone en utilisant l'API de Tripo, en traitant jusqu'à quatre images montrant différentes vues d'un objet. Une image de face et au moins une vue supplémentaire (gauche, arrière ou droite) sont nécessaires pour créer un modèle 3D complet avec des options de texture et de matériau.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | - | Image de face de l'objet (requise) |
| `image_gauche` | IMAGE | Non | - | Image de la vue gauche de l'objet |
| `image_arrière` | IMAGE | Non | - | Image de la vue arrière de l'objet |
| `image_droite` | IMAGE | Non | - | Image de la vue droite de l'objet |
| `version_modèle` | COMBO | Non | Plusieurs options disponibles | Version du modèle à utiliser pour la génération |
| `orientation` | COMBO | Non | Plusieurs options disponibles | Réglage d'orientation pour le modèle 3D (par défaut : "default") |
| `texture` | BOOLEAN | Non | - | Indique s'il faut générer des textures pour le modèle (par défaut : True) |
| `pbr` | BOOLEAN | Non | - | Indique s'il faut générer des matériaux PBR (Rendu Basé Physiquement) (par défaut : True) |
| `graine_modèle` | INT | Non | - | Graine aléatoire pour la génération du modèle (par défaut : 42) |
| `graine_texture` | INT | Non | - | Graine aléatoire pour la génération de la texture (par défaut : 42) |
| `qualité_texture` | COMBO | Non | `"standard"`<br>`"detailed"` | Niveau de qualité pour la génération de texture (par défaut : "standard") |
| `alignement_texture` | COMBO | Non | `"original_image"`<br>`"geometry"` | Méthode d'alignement des textures sur le modèle (par défaut : "original_image") |
| `limite_visage` | INT | Non | -1 à 500000 | Nombre maximum de faces dans le modèle généré. Définir sur -1 pour aucune limite (par défaut : -1) |
| `quad` | BOOLEAN | Non | - | Ce paramètre est obsolète et n'a aucun effet (par défaut : False) |
| `geometry_quality` | COMBO | Non | `"standard"`<br>`"detailed"` | Niveau de qualité pour la génération de la géométrie (par défaut : "standard") |

**Remarque :** L'image de face (`image`) est toujours requise. Au moins une image de vue supplémentaire (`image_left`, `image_back` ou `image_right`) doit être fournie pour le traitement multivue.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `modèle task_id` | STRING | Chemin du fichier ou identifiant du modèle 3D généré (uniquement pour la rétrocompatibilité) |
| `GLB` | MODEL_TASK_ID | Identifiant de tâche pour suivre le processus de génération du modèle |
| `GLB` | FILE3DGLB | Fichier du modèle 3D généré au format GLB |

---
**Source fingerprint (SHA-256):** `4ad433f4a0060d0ac2ce14463497db3168a1bf3348f17b98e958409e9a63baaf`
