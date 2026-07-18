# SavePointCloud

Le nœud Save Point Cloud enregistre un fichier de nuage de points 3D dans votre répertoire de sortie ComfyUI. Il transmet également les données du nuage de points ainsi que les informations facultatives sur la caméra et le modèle pour une utilisation par d'autres nœuds de votre flux de travail.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Fichier de nuage de points (.ply) | FILE3D | Oui | - |
| `filename_prefix` | Préfixe pour le nom du fichier enregistré (par défaut : "3d/ComfyUI") | STRING | Oui | - |
| `viewport_state` | État provenant d'un nœud de vue 3D | LOAD3D | Oui | - |
| `model_3d_info` | Informations facultatives sur le modèle 3D pour une utilisation avancée | LOAD3DMODELINFO | Non | - |
| `camera_info` | Informations facultatives sur la caméra pour une utilisation avancée | LOAD3DCAMERA | Non | - |
| `width` | Largeur de l'image d'aperçu en pixels (par défaut : 1024) | INT | Oui | min : 1, max : 4096, pas : 1 |
| `height` | Hauteur de l'image d'aperçu en pixels (par défaut : 1024) | INT | Oui | min : 1, max : 4096, pas : 1 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Le fichier de nuage de points enregistré | FILE3D |
| `model_3d_info` | Informations sur le modèle 3D | LOAD3DMODELINFO |
| `camera_info` | Informations sur la caméra pour la vue | LOAD3DCAMERA |
| `width` | Largeur de l'image d'aperçu | INT |
| `height` | Hauteur de l'image d'aperçu | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SavePointCloud/fr.md)

---
**Source fingerprint (SHA-256):** `ce8f005c431843a57d87a4aff2eed7a1604ebdf360f83b3aaaadc3ed364d218a`
