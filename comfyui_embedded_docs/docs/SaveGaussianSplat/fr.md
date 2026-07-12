# SaveGaussianSplat

Ce nœud enregistre un fichier 3D de type Gaussian splat dans le répertoire de sortie. Il gère le processus de sauvegarde du fichier et fournit des données d'aperçu pour la fenêtre 3D.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Un fichier 3D de type Gaussian splat. | FILE3D | Oui | SplatAny<br>PLY<br>SPLAT<br>SPZ<br>KSPLAT |
| `filename_prefix` | Le préfixe pour le nom du fichier enregistré (par défaut : "3d/ComfyUI"). | STRING | Oui | Tout préfixe de nom de fichier valide |
| `viewport_state` | L'état actuel de la fenêtre contenant les informations de caméra et de modèle. | LOAD3D | Oui | - |
| `model_3d_info` | Informations supplémentaires sur le modèle 3D pour la fenêtre. | LOAD3DMODELINFO | Non | - |
| `camera_info` | Informations sur la caméra pour l'aperçu dans la fenêtre. | LOAD3DCAMERA | Non | - |
| `width` | La largeur de l'aperçu (par défaut : 1024). | INT | Oui | 1 à 4096 |
| `height` | La hauteur de l'aperçu (par défaut : 1024). | INT | Oui | 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Le fichier 3D Gaussian splat enregistré. | FILE3D |
| `model_3d_info` | Informations sur le modèle 3D pour la fenêtre. | LOAD3DMODELINFO |
| `camera_info` | Informations sur la caméra pour l'aperçu dans la fenêtre. | LOAD3DCAMERA |
| `width` | La largeur de l'aperçu. | INT |
| `height` | La hauteur de l'aperçu. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGaussianSplat/fr.md)

---
**Source fingerprint (SHA-256):** `f2d6b98d2ce1fe11df8ba440b7f46a21e2308966c15daa5ca0bdca7dab1726cc`
