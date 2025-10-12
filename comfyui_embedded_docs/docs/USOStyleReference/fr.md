> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/fr.md)

Le nœud USOStyleReference applique des correctifs de référence de style aux modèles en utilisant les caractéristiques d'image encodées provenant de la sortie vision de CLIP. Il crée une version modifiée du modèle d'entrée en incorporant des informations de style extraites d'entrées visuelles, permettant des capacités de transfert de style ou de génération par référence.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle de base auquel appliquer le correctif de référence de style |
| `model_patch` | MODEL_PATCH | Oui | - | Le correctif de modèle contenant les informations de référence de style |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Oui | - | Les caractéristiques visuelles encodées extraites du traitement vision de CLIP |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle modifié avec les correctifs de référence de style appliqués |