# SaveGaussianSplat

Ce nœud enregistre un fichier 3D de type Gaussian splat dans le répertoire de sortie de ComfyUI et fournit des données d'aperçu pour le visualiseur 3D.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Un fichier 3D de type Gaussian splat. | FILE3D | Oui | - |
| `filename_prefix` | Préfixe pour le nom du fichier enregistré (par défaut : "3d/ComfyUI") | STRING | Oui | - |
| `viewport_state` | L'état actuel de la fenêtre d'affichage provenant d'un nœud de chargement 3D. | LOAD3D | Oui | - |
| `model_3d_info` | Informations supplémentaires sur le modèle 3D pour l'aperçu. | LOAD3DMODELINFO | Non | - |
| `camera_info` | Informations sur la caméra pour l'aperçu. | LOAD3DCAMERA | Non | - |
| `width` | Largeur de l'aperçu en pixels (par défaut : 1024) | INT | Oui | min : 1, max : 4096, pas : 1 |
| `height` | Hauteur de l'aperçu en pixels (par défaut : 1024) | INT | Oui | min : 1, max : 4096, pas : 1 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Le fichier 3D Gaussian splat enregistré. | FILE3D |
| `model_3d_info` | Informations sur le modèle 3D pour l'aperçu. | LOAD3DMODELINFO |
| `camera_info` | Informations sur la caméra pour l'aperçu. | LOAD3DCAMERA |
| `width` | Largeur de l'aperçu. | INT |
| `height` | Hauteur de l'aperçu. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGaussianSplat/fr.md)

---
**Source fingerprint (SHA-256):** `f2d6b98d2ce1fe11df8ba440b7f46a21e2308966c15daa5ca0bdca7dab1726cc`
