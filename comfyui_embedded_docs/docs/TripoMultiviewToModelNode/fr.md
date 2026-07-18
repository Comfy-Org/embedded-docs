Ce nœud génère des modèles 3D de manière synchrone en utilisant l'API de Tripo, en traitant jusqu'à quatre images montrant différentes vues d'un objet. Une image de face et au moins une vue supplémentaire (gauche, arrière ou droite) sont nécessaires pour créer un modèle 3D complet avec des options de texture et de matériau.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Image de face de l'objet (requise) | IMAGE | Oui | - |
| `image_gauche` | Image de la vue gauche de l'objet | IMAGE | Non | - |
| `image_arrière` | Image de la vue arrière de l'objet | IMAGE | Non | - |
| `image_droite` | Image de la vue droite de l'objet | IMAGE | Non | - |
| `version_modèle` | Version du modèle à utiliser pour la génération | COMBO | Non | Plusieurs options disponibles |
| `orientation` | Réglage d'orientation pour le modèle 3D (par défaut : "default") | COMBO | Non | Plusieurs options disponibles |
| `texture` | Indique s'il faut générer des textures pour le modèle (par défaut : True) | BOOLEAN | Non | - |
| `pbr` | Indique s'il faut générer des matériaux PBR (Rendu Basé Physiquement) (par défaut : True) | BOOLEAN | Non | - |
| `graine_modèle` | Graine aléatoire pour la génération du modèle (par défaut : 42) | INT | Non | - |
| `graine_texture` | Graine aléatoire pour la génération de la texture (par défaut : 42) | INT | Non | - |
| `qualité_texture` | Niveau de qualité pour la génération de texture (par défaut : "standard") | COMBO | Non | `"standard"`<br>`"detailed"` |
| `alignement_texture` | Méthode d'alignement des textures sur le modèle (par défaut : "original_image") | COMBO | Non | `"original_image"`<br>`"geometry"` |
| `limite_visage` | Nombre maximum de faces dans le modèle généré. Définir sur -1 pour aucune limite (par défaut : -1) | INT | Non | -1 à 500000 |
| `quad` | Ce paramètre est obsolète et n'a aucun effet (par défaut : False) | BOOLEAN | Non | - |
| `geometry_quality` | Niveau de qualité pour la génération de la géométrie (par défaut : "standard") | COMBO | Non | `"standard"`<br>`"detailed"` |

**Remarque :** L'image de face (`image`) est toujours requise. Au moins une image de vue supplémentaire (`image_left`, `image_back` ou `image_right`) doit être fournie pour le traitement multivue.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `fichier_modèle` | Chemin du fichier ou identifiant du modèle 3D généré (uniquement pour la rétrocompatibilité) | STRING |
| `modèle task_id` | Identifiant de tâche pour suivre le processus de génération du modèle | MODEL_TASK_ID |
| `GLB` | Fichier du modèle 3D généré au format GLB | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `4ad433f4a0060d0ac2ce14463497db3168a1bf3348f17b98e958409e9a63baaf`
