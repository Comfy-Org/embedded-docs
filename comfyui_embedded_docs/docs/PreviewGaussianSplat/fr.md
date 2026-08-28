# Aperçu Splat

Le nœud PreviewGaussianSplat affiche un fichier gaussian splat 3D dans une fenêtre d’aperçu sans l’enregistrer dans le répertoire de sortie de ComfyUI. Il accepte un fichier de modèle 3D dans divers formats gaussian splat, enregistre une copie temporaire pour l’aperçu et transmet les données du modèle pour un traitement ultérieur dans le workflow.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle_3d` | Un fichier 3D gaussian splat. | FILE3D | Oui | splat<br>ply<br>spz<br>ksplat |
| `info_modèle_3d` | Informations de métadonnées facultatives sur le modèle 3D. Lorsque ce paramètre n’est pas connecté, le nœud utilise les informations du modèle provenant de `viewport_state`. | LOAD3DMODELINFO | Non | - |
| `état_vue` | L’état actuel de la fenêtre d’affichage 3D, y compris les informations de caméra et de modèle. | LOAD3D | Oui | - |
| `info_caméra` | Informations de caméra facultatives pour l’aperçu. Lorsque ce paramètre n’est pas connecté, le nœud utilise les informations de caméra provenant de `viewport_state`. | LOAD3DCAMERA | Non | - |
| `largeur` | La largeur du rendu d’aperçu en pixels (par défaut : 1024). | INT | Oui | 1 à 4096 |
| `hauteur` | La hauteur du rendu d’aperçu en pixels (par défaut : 1024). | INT | Oui | 1 à 4096 |

Remarque : lorsque `camera_info` ou `model_3d_info` ne sont pas fournis, le nœud utilise par défaut les informations de caméra et de modèle stockées dans `viewport_state`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `modèle_3d` | Le fichier 3D gaussian splat d’entrée, transmis tel quel. | FILE3D |
| `info_modèle_3d` | Informations de métadonnées sur le modèle 3D, provenant de l’entrée ou dérivées de l’état de la fenêtre d’affichage. | LOAD3DMODELINFO |
| `info_caméra` | Informations de caméra pour l’aperçu, provenant de l’entrée ou dérivées de l’état de la fenêtre d’affichage. | LOAD3DCAMERA |
| `largeur` | La largeur du rendu d’aperçu. | INT |
| `hauteur` | La hauteur du rendu d’aperçu. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/fr.md)

---
**Source fingerprint (SHA-256):** `7157a0b34d7bda3e7ec86cb2ac09e0e10ff96ea7037bb6c9d6ad2c879fdedbb2`
