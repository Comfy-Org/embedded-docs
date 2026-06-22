# Tripo : Texte vers Modèle

Génère des modèles 3D de manière synchrone à partir d’une description textuelle via l’API Tripo. Ce nœud prend une description textuelle et crée un modèle 3D avec des propriétés optionnelles de texture et de matériau.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `invite` | Description textuelle pour générer le modèle 3D (saisie multiligne) | STRING | Oui | - |
| `invite_négative` | Description textuelle de ce qu’il faut éviter dans le modèle généré (saisie multiligne) | STRING | Non | - |
| `version_modèle` | Version du modèle Tripo à utiliser pour la génération (par défaut : v2.5-20250123) | COMBO | Non | Plusieurs options disponibles |
| `style` | Réglage de style pour le modèle généré (par défaut : "Aucun") | COMBO | Non | Plusieurs options disponibles |
| `texture` | Indique s’il faut générer des textures pour le modèle (par défaut : Vrai) | BOOLEAN | Non | - |
| `pbr` | Indique s’il faut générer des matériaux PBR (Rendu Physiquement Réaliste) (par défaut : Vrai) | BOOLEAN | Non | - |
| `graine_image` | Graine aléatoire pour la génération d’image (par défaut : 42) | INT | Non | - |
| `modèle_graine` | Graine aléatoire pour la génération du modèle (par défaut : 42) | INT | Non | - |
| `texture_graine` | Graine aléatoire pour la génération de texture (par défaut : 42) | INT | Non | - |
| `qualité_texture` | Niveau de qualité pour la génération de texture (par défaut : "standard") | COMBO | Non | "standard"<br>"détaillée" |
| `limite_visage` | Nombre maximum de faces dans le modèle généré, -1 pour aucune limite (par défaut : -1) | INT | Non | -1 à 2 000 000 |
| `quad` | Indique s’il faut générer une géométrie à base de quadrangles au lieu de triangles (par défaut : Faux) | BOOLEAN | Non | - |
| `geometry_quality` | Niveau de qualité pour la génération de géométrie (par défaut : "standard") | COMBO | Non | "standard"<br>"détaillée" |

**Remarque :** Le paramètre `prompt` est requis et ne peut pas être vide. Si aucune invite n’est fournie, le nœud générera une erreur.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `modèle task_id` | Fichier du modèle 3D généré (uniquement pour la rétrocompatibilité) | STRING |
| `GLB` | Identifiant unique de la tâche pour le processus de génération du modèle | MODEL_TASK_ID |
| `GLB` | Modèle 3D généré au format GLB | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `f73316e0a50adfb6fe22ca6a20a2a5b36a6597abf0f4ddae9183d9e4a45cb46d`
