# Tripo : Modèle de texture

Voici la traduction en français de la documentation du nœud TripoTextureNode :

Le TripoTextureNode génère des modèles 3D texturés à l'aide de l'API Tripo. Il prend un ID de tâche de modèle et applique une génération de texture avec diverses options, notamment les matériaux PBR, les paramètres de qualité de texture et les méthodes d'alignement. Le nœud communique avec l'API Tripo pour traiter la demande de génération de texture et renvoie le fichier de modèle résultant ainsi que l'ID de tâche.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle_id_tâche` | L'ID de tâche du modèle auquel appliquer les textures | MODEL_TASK_ID | Oui | - |
| `texture` | Indique s'il faut générer des textures (par défaut : True) | BOOLEAN | Non | - |
| `pbr` | Indique s'il faut générer des matériaux PBR (Physically Based Rendering) (par défaut : True) | BOOLEAN | Non | - |
| `texture_graine` | Graine aléatoire pour la génération de texture (par défaut : 42) | INT | Non | - |
| `qualité_texture` | Niveau de qualité pour la génération de texture (par défaut : "standard"). L'option "detailed" coûte 0,20 USD, tandis que "standard" coûte 0,10 USD. | COMBO | Non | "standard"<br>"detailed" |
| `alignement_texture` | Méthode d'alignement des textures (par défaut : "original_image"). "original_image" aligne les textures sur l'image d'entrée d'origine, tandis que "geometry" les aligne sur la géométrie 3D. | COMBO | Non | "original_image"<br>"geometry" |

*Remarque : Ce nœud nécessite des jetons d'authentification et des clés API qui sont automatiquement gérés par le système.*

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `fichier_modèle` | Le fichier de modèle généré avec les textures appliquées (uniquement pour la rétrocompatibilité) | STRING |
| `modèle task_id` | L'ID de tâche pour suivre le processus de génération de texture | MODEL_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB avec les textures appliquées | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/fr.md)

---
**Source fingerprint (SHA-256):** `6d2a6ff7bbbe9fa91f63c6c7d237799044d2f9aa5afe7b90b99cf9e5a21afc32`
