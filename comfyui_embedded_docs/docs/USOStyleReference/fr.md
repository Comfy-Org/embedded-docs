# USOStyleReference

Le nœud USOStyleReference applique une référence de style à un modèle en combinant les caractéristiques de vision CLIP avec un patch de modèle, et renvoie une copie patchée du modèle d'entrée. Il est destiné aux modèles Flux et est marqué comme expérimental. Les informations de style visuel sont combinées avec le conditionnement textuel du modèle afin d'influencer la génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de base auquel le patch de référence de style est appliqué. | MODEL | Oui | - |
| `correctif_modèle` | Le patch de modèle contenant le modèle de projection utilisé pour encoder les caractéristiques de l'image de référence. | MODEL_PATCH | Oui | - |
| `sortie_vision_clip` | Les caractéristiques visuelles encodées extraites du traitement de vision CLIP de l'image de référence. | CLIP_VISION_OUTPUT | Oui | - |

Remarque : Le `clip_vision_output` doit provenir d'un modèle de vision CLIP qui fournit les états cachés complets et l'avant-dernier état caché. Le nœud combine les 20e à partir de la fin, 11e à partir de la fin et avant-dernier états cachés pour former l'incorporation de style. Le `model_patch` doit exposer un modèle de projection via son attribut `model` qui convertit ces caractéristiques d'image en incorporation de style. Pendant l'échantillonnage, l'incorporation de style est ajoutée au début du conditionnement textuel afin d'influencer la génération.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec le patch de référence de style appliqué. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/fr.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
