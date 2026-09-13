# USOStyleReference

Le nœud USOStyleReference applique une référence de style à un modèle en combinant des caractéristiques de vision CLIP avec un patch de modèle, et renvoie une copie du modèle d'entrée avec le patch appliqué. Les informations de style visuel sont combinées au conditionnement textuel du modèle afin qu'elles puissent influencer la génération. Ce nœud est destiné aux modèles Flux et est marqué comme expérimental.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de base auquel le patch de référence de style est appliqué. | MODEL | Oui | - |
| `correctif_modèle` | Le patch de modèle contenant le modèle de projection utilisé pour encoder les caractéristiques de l'image de référence. | MODEL_PATCH | Oui | - |
| `sortie_vision_clip` | Les caractéristiques visuelles encodées extraites du traitement de vision CLIP de l'image de référence. | CLIP_VISION_OUTPUT | Oui | - |

Remarque : le `clip_vision_output` doit provenir d'un modèle de vision CLIP qui fournit les états cachés complets et l'avant-dernier état caché. Le nœud combine le 20e en partant de la fin, le 11e en partant de la fin et l'avant-dernier état caché pour former l'embedding de style. Le `model_patch` doit exposer un modèle de projection via son attribut `model`, qui convertit ces caractéristiques d'image en embedding de style. Pendant l'échantillonnage, l'embedding de style est ajouté au début du conditionnement textuel afin qu'il puisse influencer la génération, et les ID de texte à position zéro correspondants sont ajoutés au début des ID de texte afin que la séquence d'identifiants reste alignée avec le conditionnement étendu.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec le patch de référence de style appliqué. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/fr.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
