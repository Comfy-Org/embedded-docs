> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/fr.md)

Génère des modèles 3D de manière synchrone à partir d’une description textuelle via l’API Tripo. Ce nœud prend une description textuelle et crée un modèle 3D avec des propriétés optionnelles de texture et de matériau.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `invite` | STRING | Oui | - | Description textuelle pour générer le modèle 3D (saisie multiligne) |
| `invite_négative` | STRING | Non | - | Description textuelle de ce qu’il faut éviter dans le modèle généré (saisie multiligne) |
| `version_modèle` | COMBO | Non | Plusieurs options disponibles | Version du modèle Tripo à utiliser pour la génération (par défaut : v2.5-20250123) |
| `style` | COMBO | Non | Plusieurs options disponibles | Réglage de style pour le modèle généré (par défaut : "Aucun") |
| `texture` | BOOLEAN | Non | - | Indique s’il faut générer des textures pour le modèle (par défaut : Vrai) |
| `pbr` | BOOLEAN | Non | - | Indique s’il faut générer des matériaux PBR (Rendu Physiquement Réaliste) (par défaut : Vrai) |
| `graine_image` | INT | Non | - | Graine aléatoire pour la génération d’image (par défaut : 42) |
| `modèle_graine` | INT | Non | - | Graine aléatoire pour la génération du modèle (par défaut : 42) |
| `texture_graine` | INT | Non | - | Graine aléatoire pour la génération de texture (par défaut : 42) |
| `qualité_texture` | COMBO | Non | "standard"<br>"détaillée" | Niveau de qualité pour la génération de texture (par défaut : "standard") |
| `limite_visage` | INT | Non | -1 à 2 000 000 | Nombre maximum de faces dans le modèle généré, -1 pour aucune limite (par défaut : -1) |
| `quad` | BOOLEAN | Non | - | Indique s’il faut générer une géométrie à base de quadrangles au lieu de triangles (par défaut : Faux) |
| `geometry_quality` | COMBO | Non | "standard"<br>"détaillée" | Niveau de qualité pour la génération de géométrie (par défaut : "standard") |

**Remarque :** Le paramètre `prompt` est requis et ne peut pas être vide. Si aucune invite n’est fournie, le nœud générera une erreur.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `modèle task_id` | STRING | Fichier du modèle 3D généré (uniquement pour la rétrocompatibilité) |
| `GLB` | MODEL_TASK_ID | Identifiant unique de la tâche pour le processus de génération du modèle |
| `GLB` | FILE3DGLB | Modèle 3D généré au format GLB |

---
**Source fingerprint (SHA-256):** `f73316e0a50adfb6fe22ca6a20a2a5b36a6597abf0f4ddae9183d9e4a45cb46d`
