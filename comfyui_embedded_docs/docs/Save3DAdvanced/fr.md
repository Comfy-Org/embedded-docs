# Save3DAdvanced

Ce nœud enregistre un modèle 3D dans un fichier situé dans le répertoire de sortie de ComfyUI, avec un contrôle avancé sur les dimensions de sortie et les paramètres de la caméra/du viewport. Il transmet également le modèle 3D, les informations du modèle, les informations de la caméra et les dimensions aux nœuds en aval.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Fichier de modèle 3D provenant d'un nœud 3D en amont. | FILE3D | Oui | GLB, GLTF, FBX, OBJ, STL, USDZ, Any |
| `filename_prefix` | Préfixe pour le nom du fichier enregistré (par défaut : "3d/ComfyUI"). | STRING | Oui | Texte libre |
| `viewport_state` | État du viewport provenant d'un nœud Load 3D, contenant les informations de la caméra et du modèle. | LOAD3D | Oui | - |
| `model_3d_info` | Informations facultatives sur le modèle 3D pour remplacer l'état du viewport. | LOAD3DMODELINFO | Non | - |
| `camera_info` | Informations facultatives sur la caméra pour remplacer l'état du viewport. | LOAD3DCAMERA | Non | - |
| `width` | Largeur de l'aperçu de sortie en pixels (par défaut : 1024). | INT | Oui | 1 à 4096 |
| `height` | Hauteur de l'aperçu de sortie en pixels (par défaut : 1024). | INT | Oui | 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Le fichier de modèle 3D transmis depuis l'entrée. | FILE3D |
| `model_3d_info` | Informations sur le modèle, provenant soit de l'état du viewport, soit de l'entrée facultative. | LOAD3DMODELINFO |
| `camera_info` | Informations sur la caméra, provenant soit de l'état du viewport, soit de l'entrée facultative. | LOAD3DCAMERA |
| `width` | La valeur de largeur transmise depuis l'entrée. | INT |
| `height` | La valeur de hauteur transmise depuis l'entrée. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `2c7d42b1875bb292e675526a2b38fcc8856c8ac45de25ac7b69d92323f0b7ae0`
