# Aperçu Nuage de Points

Le nœud Preview Point Cloud vous permet de visualiser un fichier de nuage de points 3D (tel qu'un fichier .ply) directement dans l'interface ComfyUI, sans avoir à l'enregistrer dans le répertoire de sortie. Le nœud écrit le nuage de points dans un fichier temporaire, l'affiche dans une fenêtre d'aperçu 3D, puis transmet les données du modèle, les informations du modèle, les informations de caméra, la largeur et la hauteur pour un traitement ultérieur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Fichier de nuage de points (.ply) | FILE3D | Oui | - |
| `model_3d_info` | Informations sur le modèle 3D. Entrée avancée. Lorsqu'elle n'est pas connectée, la valeur stockée dans `viewport_state` est utilisée. | LOAD3DMODELINFO | Non | - |
| `viewport_state` | État actuel de la fenêtre d'affichage, qui peut contenir les informations de caméra et les informations du modèle utilisées pour l'aperçu. | LOAD3D | Oui | - |
| `camera_info` | Informations de caméra pour la vue 3D. Entrée avancée. Lorsqu'elle n'est pas connectée, la valeur stockée dans `viewport_state` est utilisée. | LOAD3DCAMERA | Non | - |
| `width` | Largeur de la fenêtre d'aperçu en pixels (défaut : 1024). | INT | Oui | 1 to 4096 |
| `height` | Hauteur de la fenêtre d'aperçu en pixels (défaut : 1024). | INT | Oui | 1 to 4096 |

Remarque : lorsque `camera_info` ou `model_3d_info` ne sont pas connectés, le nœud utilise les valeurs stockées dans `viewport_state`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Les données du modèle de nuage de points, transmises telles quelles. | FILE3D |
| `model_3d_info` | Informations sur le modèle 3D utilisé pour l'aperçu. | LOAD3DMODELINFO |
| `camera_info` | Informations de caméra utilisées pour la vue 3D. | LOAD3DCAMERA |
| `width` | Largeur de la fenêtre d'aperçu. | INT |
| `height` | Hauteur de la fenêtre d'aperçu. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/fr.md)

---
**Source fingerprint (SHA-256):** `a192096df29c4d7029f6e7f4f32e0a2f48de5b3d0cd437bd5b03d79e15eb0987`
