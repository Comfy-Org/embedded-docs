# Aperçu Splat

Le nœud PreviewGaussianSplat affiche un fichier gaussian splat 3D dans une fenêtre d’aperçu sans l’enregistrer dans le répertoire de sortie de ComfyUI. Il accepte un fichier de modèle 3D dans divers formats gaussian splat, enregistre une copie temporaire pour l’aperçu et transmet les données du modèle pour un traitement ultérieur dans le flux de travail. Ce nœud est marqué comme expérimental et agit comme un nœud de sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Un fichier 3D gaussian splat. | FILE3D | Oui | splat<br>ply<br>spz<br>ksplat |
| `model_3d_info` | Informations de métadonnées facultatives sur le modèle 3D. Lorsque cette entrée n’est pas connectée, le nœud utilise les informations du modèle provenant de `viewport_state`. | LOAD3DMODELINFO | Non | - |
| `viewport_state` | L’état actuel du viewport 3D, y compris les informations sur la caméra et le modèle. | LOAD3D | Oui | - |
| `camera_info` | Informations de caméra facultatives pour l’aperçu. Lorsque cette entrée n’est pas connectée, le nœud utilise les informations de caméra provenant de `viewport_state`. | LOAD3DCAMERA | Non | - |
| `width` | La largeur du rendu d’aperçu en pixels (par défaut : 1024). | INT | Oui | 1 à 4096 |
| `height` | La hauteur du rendu d’aperçu en pixels (par défaut : 1024). | INT | Oui | 1 à 4096 |

Remarque : Lorsque `camera_info` ou `model_3d_info` n’est pas fourni, le nœud utilise par défaut les informations de caméra et de modèle stockées dans `viewport_state`. Si `viewport_state` n’est pas un objet d’état de viewport valide, il est traité comme vide.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Le fichier 3D gaussian splat d’entrée, transmis sans modification. | FILE3D |
| `model_3d_info` | Informations de métadonnées sur le modèle 3D, provenant soit de l’entrée, soit dérivées de l’état du viewport. | LOAD3DMODELINFO |
| `camera_info` | Informations de caméra pour l’aperçu, provenant soit de l’entrée, soit dérivées de l’état du viewport. | LOAD3DCAMERA |
| `width` | La largeur du rendu d’aperçu. | INT |
| `height` | La hauteur du rendu d’aperçu. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/fr.md)

---
**Source fingerprint (SHA-256):** `4fc86c692724ce406f9bba9aa9ebe22a92e72a25d11abf8f55d1b99044bb1acd`
