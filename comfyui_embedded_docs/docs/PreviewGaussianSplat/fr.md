# Aperçu Splat

Le nœud `PreviewGaussianSplat` vous permet de prévisualiser un fichier gaussian splat 3D directement dans l’interface ComfyUI sans l’enregistrer dans le répertoire de sortie. Il stocke temporairement le fichier dans un dossier temporaire, l’affiche dans une fenêtre d’aperçu 3D, puis transmet les données du modèle, les informations de caméra et la taille de l’aperçu aux autres nœuds.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Un fichier gaussian splat 3D. | FILE3D | Oui | splat, ply, spz, ksplat |
| `model_3d_info` | Informations de métadonnées facultatives sur le modèle 3D. | LOAD3DMODELINFO | Non | - |
| `viewport_state` | L’état actuel de la fenêtre 3D, y compris les informations de caméra et de modèle. | LOAD3D | Oui | - |
| `camera_info` | Informations de caméra facultatives pour l’aperçu. | LOAD3DCAMERA | Non | - |
| `width` | La largeur du rendu d’aperçu en pixels (défaut : 1024). | INT | Oui | 1 to 4096 |
| `height` | La hauteur du rendu d’aperçu en pixels (défaut : 1024). | INT | Oui | 1 to 4096 |

Remarque : lorsque `camera_info` ou `model_3d_info` ne sont pas fournis, le nœud utilise les valeurs correspondantes de `viewport_state` à la place.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Le fichier gaussian splat 3D d’entrée, transmis sans modification. | FILE3D |
| `model_3d_info` | Informations de métadonnées sur le modèle 3D, provenant soit de l’entrée, soit de l’état de la fenêtre. | LOAD3DMODELINFO |
| `camera_info` | Informations de caméra pour l’aperçu, provenant soit de l’entrée, soit de l’état de la fenêtre. | LOAD3DCAMERA |
| `width` | La largeur du rendu d’aperçu. | INT |
| `height` | La hauteur du rendu d’aperçu. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/fr.md)

---
**Source fingerprint (SHA-256):** `7157a0b34d7bda3e7ec86cb2ac09e0e10ff96ea7037bb6c9d6ad2c879fdedbb2`
