# Create Camera Orbit

Construit un rig de caméras autour de la cible de la première caméra : un plateau tournant par défaut, un balayage incliné lorsque `pitch` est défini, et éventuellement des vues directement vers le bas et vers le haut. Render Mesh rend une image par caméra et Bake Texture From Views les projette en retour sur le maillage.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `camera_info` | Première caméra de l'orbite. Une liste de caméras orbite autour de chaque caméra qu'elle contient. | LOAD3D_CAMERA | Oui | - |
| `count` | Caméras régulièrement espacées le long du balayage. Par défaut : 4. | INT | Oui | 1 à 64 |
| `yaw` | Rotation totale autour de la cible, dans la direction yaw de Create Camera Info. Les tours complets s'arrêtent un pas avant la première caméra ; les autres balayages se terminent sur la dernière caméra. Par défaut : 360.0. | FLOAT | Oui | -720.0 à 720.0 (pas : 1.0) |
| `pitch` | Inclinaison totale au-dessus de la cible, positive en montant comme le pitch de Create Camera Info ; au-delà de 90, les caméras passent par-dessus le sommet. Les tours complets bouclent comme `yaw`. Par défaut : 0.0. | FLOAT | Oui | -720.0 à 720.0 (pas : 1.0) |
| `poles` | Vues directement vers le bas et/ou vers le haut sur la cible, ajoutées après l'orbite. Le haut de leur image pointe à l'opposé de la première caméra. Par défaut : `"none"`. | COMBO | Oui | `"none"`<br>`"top"`<br>`"bottom"`<br>`"top and bottom"` |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `camera_info` | La liste de caméras du rig, dans l'ordre de l'orbite suivi des vues aux pôles. | LOAD3D_CAMERA |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateCameraOrbit/fr.md)

---
**Source fingerprint (SHA-256):** `b251efc969f8db7cf03527594be3bbd2af037f1ebb56bdf508bf264ddd9f8c08`
