# USOStyleReference

Le nœud USOStyleReference applique des correctifs de référence de style aux modèles en utilisant les caractéristiques d'image encodées issues de la sortie CLIP vision. Il crée une version modifiée du modèle d'entrée en intégrant les informations de style extraites des entrées visuelles, permettant ainsi le transfert de style ou des capacités de génération basées sur une référence.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de base auquel appliquer le correctif de référence de style | MODEL | Oui | - |
| `correctif_modèle` | Le correctif de modèle contenant les informations de référence de style | MODEL_PATCH | Oui | - |
| `sortie_vision_clip` | Les caractéristiques visuelles encodées extraites du traitement CLIP vision | CLIP_VISION_OUTPUT | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle modifié avec les correctifs de référence de style appliqués | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/fr.md)

---
**Source fingerprint (SHA-256):** `fd800fb927677da29e148bfa1b287efed82895860ce4b0241d662579d2c07ff4`
