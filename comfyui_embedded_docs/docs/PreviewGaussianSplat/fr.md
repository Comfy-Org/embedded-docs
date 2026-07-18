# PreviewGaussianSplat

Le nœud PreviewGaussianSplat permet de prévisualiser un fichier de splats gaussiens 3D dans l'interface ComfyUI. Il accepte un fichier de modèle 3D dans divers formats de splats gaussiens et le rend dans une fenêtre de prévisualisation 3D, tout en transmettant les données du modèle pour un traitement ultérieur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle_3d` | Un fichier 3D de splats gaussiens. | FILE3D | Oui | Formats pris en charge : splat, ply, spz, ksplat |
| `info_modèle_3d` | Informations facultatives de métadonnées sur le modèle 3D. | LOAD3DMODELINFO | Non | - |
| `état_vue` | L'état actuel de la fenêtre d'affichage 3D, incluant les informations de caméra et de modèle. | LOAD3D | Oui | - |
| `info_caméra` | Informations facultatives de caméra pour la prévisualisation. | LOAD3DCAMERA | Non | - |
| `largeur` | La largeur du rendu de prévisualisation en pixels (par défaut : 1024). | INT | Oui | 1 à 4096 |
| `hauteur` | La hauteur du rendu de prévisualisation en pixels (par défaut : 1024). | INT | Oui | 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `modèle_3d` | Le fichier de splats gaussiens 3D d'entrée, transmis sans modification. | FILE3D |
| `info_modèle_3d` | Informations de métadonnées sur le modèle 3D, provenant soit de l'entrée, soit dérivées de l'état de la fenêtre d'affichage. | LOAD3DMODELINFO |
| `info_caméra` | Informations de caméra pour la prévisualisation, provenant soit de l'entrée, soit dérivées de l'état de la fenêtre d'affichage. | LOAD3DCAMERA |
| `largeur` | La largeur du rendu de prévisualisation. | INT |
| `hauteur` | La hauteur du rendu de prévisualisation. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/fr.md)

---
**Source fingerprint (SHA-256):** `7b79e9ab25858e7db6e999313cc11226895aeb4d7fee414f56f0d5fd2363b485`
