# USOStyleReference

Le nœud USOStyleReference applique les informations de style d'une image de référence à un modèle Flux. Il construit un embedding de style à partir de la sortie vision CLIP, puis patche un clone du modèle afin que, pendant la génération, l'embedding de style soit inséré devant le conditionnement du prompt texte.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de base auquel appliquer le patch de référence de style | MODEL | Oui | - |
| `model_patch` | Le patch de modèle contenant les informations de référence de style | MODEL_PATCH | Oui | - |
| `clip_vision_output` | Les caractéristiques visuelles encodées extraites du traitement vision CLIP. Le nœud combine les états cachés des couches -20 et -11 avec les avant-derniers états cachés pour construire l'embedding de style | CLIP_VISION_OUTPUT | Oui | - |

Remarque : Les trois entrées sont requises. Ce nœud est marqué comme expérimental.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec le patch de référence de style appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/fr.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
