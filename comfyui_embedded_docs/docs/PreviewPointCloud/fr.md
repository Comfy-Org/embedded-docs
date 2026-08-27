# Aperçu Nuage de Points

Le nœud Preview Point Cloud vous permet de visualiser un fichier de nuage de points 3D directement dans l'interface ComfyUI sans l'enregistrer dans le répertoire de sortie de ComfyUI. Il enregistre le nuage de points dans un emplacement temporaire et l'affiche dans une fenêtre d'aperçu 3D, tout en transmettant les données du modèle, les informations de caméra et l'état de la fenêtre d'affichage pour un traitement ultérieur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle_3d` | Fichier de nuage de points (.ply) | FILE3D | Oui | - |
| `info_modèle_3d` | Informations sur le modèle 3D | LOAD3DMODELINFO | Non | - |
| `état_vue` | L'état actuel de la fenêtre d'affichage | LOAD3D | Oui | - |
| `info_caméra` | Informations de caméra pour la vue 3D | LOAD3DCAMERA | Non | - |
| `largeur` | Largeur de la fenêtre d'aperçu (par défaut : 1024) | INT | Oui | 1 à 4096 |
| `hauteur` | Hauteur de la fenêtre d'aperçu (par défaut : 1024) | INT | Oui | 1 à 4096 |

Note : Lorsque `camera_info` ou `model_3d_info` ne sont pas connectés, le nœud utilise les valeurs correspondantes stockées dans `viewport_state`. Le fichier de nuage de points est enregistré dans le répertoire temporaire de ComfyUI et n'est pas écrit dans le répertoire de sortie. Il s'agit d'un nœud de sortie, il est donc principalement utilisé pour afficher le résultat d'aperçu dans l'interface.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `modèle_3d` | Les données du modèle de nuage de points | FILE3D |
| `info_modèle_3d` | Informations sur le modèle 3D | LOAD3DMODELINFO |
| `info_caméra` | Informations de caméra pour la vue 3D | LOAD3DCAMERA |
| `largeur` | Largeur de la fenêtre d'aperçu | INT |
| `hauteur` | Hauteur de la fenêtre d'aperçu | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/fr.md)

---
**Source fingerprint (SHA-256):** `a192096df29c4d7029f6e7f4f32e0a2f48de5b3d0cd437bd5b03d79e15eb0987`
