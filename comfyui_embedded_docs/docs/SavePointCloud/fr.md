# SavePointCloud

Le nœud Save Point Cloud enregistre un fichier de nuage de points 3D dans le répertoire de sortie et fournit éventuellement des données d'aperçu pour la visionneuse 3D. Il gère la dénomination et l'enregistrement des fichiers, tout en transmettant les informations de caméra et de modèle à des fins d'affichage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Fichier de nuage de points (.ply) | FILE3D_POINT_CLOUD_ANY ou FILE3D_PLY | Oui | - |
| `filename_prefix` | Préfixe pour le nom du fichier enregistré (par défaut : "3d/ComfyUI") | STRING | Oui | - |
| `viewport_state` | État actuel de la fenêtre d'affichage contenant les informations de caméra et de modèle | LOAD3D | Oui | - |
| `model_3d_info` | Informations supplémentaires sur le modèle pour la visionneuse 3D | LOAD3D_MODEL_INFO | Non | - |
| `camera_info` | Informations de caméra pour la visionneuse 3D | LOAD3D_CAMERA | Non | - |
| `width` | Largeur de l'affichage d'aperçu en pixels (par défaut : 1024) | INT | Oui | 1 à 4096 |
| `height` | Hauteur de l'affichage d'aperçu en pixels (par défaut : 1024) | INT | Oui | 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Le fichier de nuage de points enregistré | FILE3D_POINT_CLOUD_ANY |
| `model_3d_info` | Informations sur le modèle pour la visionneuse 3D | LOAD3D_MODEL_INFO |
| `camera_info` | Informations de caméra pour la visionneuse 3D | LOAD3D_CAMERA |
| `width` | Largeur de l'affichage d'aperçu | INT |
| `height` | Hauteur de l'affichage d'aperçu | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SavePointCloud/fr.md)

---
**Source fingerprint (SHA-256):** `ce8f005c431843a57d87a4aff2eed7a1604ebdf360f83b3aaaadc3ed364d218a`
