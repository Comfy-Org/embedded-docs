# Aperçu 3D (Avancé)

Ce nœud fournit un aperçu avancé de modèle 3D avec sortie d’informations de caméra et de modèle. Il prévisualise un fichier de modèle 3D sans l’enregistrer dans le répertoire de sortie de ComfyUI, en écrivant le modèle dans un fichier temporaire pour l’affichage dans l’interface. Les données du modèle, les informations du modèle, les informations de caméra et les dimensions de la fenêtre d’affichage sont également transmises pour un traitement ultérieur en aval.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Fichier de modèle 3D provenant d’un nœud 3D en amont. | FILE3D | Oui | GLB, GLTF, FBX, OBJ, STL, USDZ, ou tout format 3D pris en charge |
| `model_3d_info` | Métadonnées d’informations sur le modèle (optionnel). | LOAD3DMODELINFO | Non | - |
| `viewport_state` | L’état actuel de la fenêtre d’affichage contenant les informations de caméra et de modèle. | LOAD3D | Oui | - |
| `camera_info` | Configuration de caméra optionnelle pour la vue 3D. | LOAD3DCAMERA | Non | - |
| `width` | La largeur de l’aperçu en pixels. | INT | Oui | 1 à 4096 (par défaut : 1024) |
| `height` | La hauteur de l’aperçu en pixels. | INT | Oui | 1 à 4096 (par défaut : 1024) |

Remarque : Lorsque `camera_info` n’est pas connecté, le nœud utilise la valeur `camera_info` de `viewport_state`. Lorsque `model_3d_info` n’est pas connecté, le nœud utilise la valeur `model_3d_info` de `viewport_state`, ou une liste vide si l’état de la fenêtre d’affichage ne la contient pas.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Le fichier de modèle 3D transmis depuis l’entrée. | FILE3D |
| `model_3d_info` | Métadonnées d’informations sur le modèle, provenant de l’entrée ou de l’état de la fenêtre d’affichage. | LOAD3DMODELINFO |
| `camera_info` | Configuration de caméra, provenant de l’entrée ou de l’état de la fenêtre d’affichage. | LOAD3DCAMERA |
| `width` | La largeur de l’aperçu en pixels. | INT |
| `height` | La hauteur de l’aperçu en pixels. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `eda8c8fdd6ce7c39caf00c3054fc58e6dcab124fc3774d17af2deae651fbbf2e`
