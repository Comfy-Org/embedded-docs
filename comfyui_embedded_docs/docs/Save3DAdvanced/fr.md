# Save3DAdvanced

Ce nœud enregistre un modèle 3D dans votre répertoire de sortie ComfyUI et offre des capacités d’aperçu avancées. Il vous permet de spécifier le nom du fichier de sortie, les dimensions de l’aperçu, et éventuellement de transmettre des informations sur la caméra et le modèle pour une expérience de visualisation 3D améliorée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Fichier de modèle 3D provenant d’un nœud 3D en amont. | FILE3D | Oui | GLB, GLTF, FBX, OBJ, STL, USDZ ou tout format 3D |
| `filename_prefix` | Préfixe pour le nom du fichier enregistré. Un compteur et une extension de fichier seront ajoutés automatiquement. (par défaut : "3d/ComfyUI") | STRING | Oui | Toute chaîne de nom de fichier valide |
| `viewport_state` | État actuel de la fenêtre d’affichage, généralement issu d’un nœud de visualisation 3D. | LOAD3D | Oui | - |
| `model_3d_info` | Informations facultatives sur le modèle 3D pour l’aperçu. | LOAD3DMODELINFO | Non | - |
| `camera_info` | Informations facultatives sur la caméra pour l’aperçu. | LOAD3DCAMERA | Non | - |
| `width` | Largeur de l’aperçu en pixels. (par défaut : 1024) | INT | Oui | 1 à 4096 |
| `height` | Hauteur de l’aperçu en pixels. (par défaut : 1024) | INT | Oui | 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Le fichier de modèle 3D enregistré. | FILE3D |
| `model_3d_info` | Informations sur le modèle 3D transmises aux nœuds en aval. | LOAD3DMODELINFO |
| `camera_info` | Informations sur la caméra transmises aux nœuds en aval. | LOAD3DCAMERA |
| `width` | Valeur de largeur transmise aux nœuds en aval. | INT |
| `height` | Valeur de hauteur transmise aux nœuds en aval. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `2c7d42b1875bb292e675526a2b38fcc8856c8ac45de25ac7b69d92323f0b7ae0`
