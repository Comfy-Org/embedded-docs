# Aperçu 3D (Avancé)

Ce nœud fournit un aperçu avancé de modèles 3D avec sortie des informations de caméra et de modèle. Il enregistre le modèle 3D dans un fichier temporaire et l'affiche dans l'interface utilisateur, tout en transmettant les données du modèle, les informations de la caméra et les dimensions de la fenêtre d'affichage pour un traitement ultérieur en aval.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Fichier de modèle 3D provenant d'un nœud 3D en amont. | FILE3D | Oui | GLB, GLTF, FBX, OBJ, STL, USDZ ou tout format 3D pris en charge |
| `infos_modèle_3d` | Métadonnées facultatives d'informations sur le modèle. | LOAD3DMODELINFO | Non | - |
| `viewport_state` | État actuel de la fenêtre d'affichage contenant les informations de caméra et de modèle. | LOAD3D | Oui | - |
| `infos_caméra` | Configuration facultative de la caméra pour la vue 3D. | LOAD3DCAMERA | Non | - |
| `largeur` | Largeur de l'aperçu en pixels. | INT | Oui | 1 à 4096 (par défaut : 1024) |
| `hauteur` | Hauteur de l'aperçu en pixels. | INT | Oui | 1 à 4096 (par défaut : 1024) |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `infos_caméra` | Fichier de modèle 3D transmis depuis l'entrée. | FILE3D |
| `infos_modèle_3d` | Métadonnées d'informations sur le modèle, provenant soit de l'entrée, soit de l'état de la fenêtre d'affichage. | LOAD3DMODELINFO |
| `largeur` | Configuration de la caméra, provenant soit de l'entrée, soit de l'état de la fenêtre d'affichage. | LOAD3DCAMERA |
| `hauteur` | Largeur de l'aperçu en pixels. | INT |
| `hauteur` | Hauteur de l'aperçu en pixels. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `7efe8720f88f7d6234387cd633ea629cbf43a0abea1a9aca6c5dcd43bf7f2145`
