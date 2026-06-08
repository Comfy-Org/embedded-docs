# Aperçu du Nuage de Points

Le nœud Aperçu du Nuage de Points vous permet de visualiser un fichier de nuage de points 3D dans l'interface ComfyUI. Il enregistre le nuage de points dans un fichier temporaire et l'affiche dans une fenêtre d'aperçu 3D, tout en transmettant les données du modèle et les paramètres de la vue pour un traitement ultérieur.

## Entrées

| Paramètre | Description | Type de Données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Fichier de nuage de points (.ply) | FILE3D | Oui | - |
| `model_3d_info` | Informations sur le modèle 3D | LOAD3DMODELINFO | Non | - |
| `viewport_state` | État actuel de la vue | LOAD3D | Oui | - |
| `camera_info` | Informations de la caméra pour la vue 3D | LOAD3DCAMERA | Non | - |
| `width` | Largeur de la fenêtre d'aperçu (par défaut : 1024) | INT | Oui | 1 à 4096 |
| `height` | Hauteur de la fenêtre d'aperçu (par défaut : 1024) | INT | Oui | 1 à 4096 |

## Sorties

| Nom de Sortie | Description | Type de Données |
|---------------|-------------|-----------------|
| `model_3d` | Données du modèle de nuage de points | FILE3D |
| `model_3d_info` | Informations sur le modèle 3D | LOAD3DMODELINFO |
| `camera_info` | Informations de la caméra pour la vue 3D | LOAD3DCAMERA |
| `width` | Largeur de la fenêtre d'aperçu | INT |
| `height` | Hauteur de la fenêtre d'aperçu | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/fr.md)

---
**Source fingerprint (SHA-256):** `f3121511841d1962aad881c0ac5b93f24842bf4810e84fe241330e9eab90334a`
