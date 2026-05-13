> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/fr.md)

Le nœud USOStyleReference applique des correctifs de référence de style aux modèles en utilisant les caractéristiques d'image encodées issues de la sortie CLIP vision. Il crée une version modifiée du modèle d'entrée en intégrant les informations de style extraites des entrées visuelles, permettant ainsi le transfert de style ou des capacités de génération basées sur une référence.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle de base auquel appliquer le correctif de référence de style |
| `correctif_modèle` | MODEL_PATCH | Oui | - | Le correctif de modèle contenant les informations de référence de style |
| `sortie_vision_clip` | CLIP_VISION_OUTPUT | Oui | - | Les caractéristiques visuelles encodées extraites du traitement CLIP vision |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `modèle` | MODEL | Le modèle modifié avec les correctifs de référence de style appliqués |

---
**Source fingerprint (SHA-256):** `fd800fb927677da29e148bfa1b287efed82895860ce4b0241d662579d2c07ff4`
