# Batch Cameras

Associe les caméras et les orbites de caméra en une seule liste de caméras, dans l'ordre d'entrée. Render Mesh et Render Splat rendent une image par caméra de la liste, ce qui permet de construire un rendu multivue.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `cameras` | Emplacement extensible de caméras, depuis Create Camera Info, Create Camera Orbit ou une visionneuse. Une liste de caméras équivaut à toutes les caméras qu'elle contient. | AUTOGROW | Oui | 1 à 50 caméras |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `camera_info` | Une liste de caméras contenant toutes les caméras d'entrée, dans l'ordre d'entrée. | LOAD3D_CAMERA |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchCameras/fr.md)

---
**Source fingerprint (SHA-256):** `a5ddae7f539a2d70efc1b156f7b4ec4b219d7cf78544b882f7b8f9538ae9a88d`
