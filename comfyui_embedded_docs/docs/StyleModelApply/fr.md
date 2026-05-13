> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelApply/fr.md)

Ce nœud applique un modèle de style à un conditionnement donné, en enrichissant ou en modifiant son style en fonction de la sortie d’un modèle CLIP vision. Il intègre le conditionnement du modèle de style dans le conditionnement existant, permettant ainsi un mélange harmonieux des styles dans le processus de génération.

## Entrées

### Requises

| Paramètre              | Type Comfy            | Description |
|------------------------|-----------------------|-------------|
| `conditioning`         | `CONDITIONING`        | Les données de conditionnement d’origine auxquelles le conditionnement du modèle de style sera appliqué. Essentielles pour définir le contexte ou le style de base qui sera enrichi ou modifié. |
| `style_model`          | `STYLE_MODEL`         | Le modèle de style utilisé pour générer un nouveau conditionnement à partir de la sortie du modèle CLIP vision. Il joue un rôle clé dans la définition du nouveau style à appliquer. |
| `clip_vision_output`   | `CLIP_VISION_OUTPUT`  | La sortie d’un modèle CLIP vision, utilisée par le modèle de style pour générer un nouveau conditionnement. Elle fournit le contexte visuel nécessaire à l’application du style. |

## Sorties

| Paramètre             | Type Comfy            | Description |
|-----------------------|-----------------------|-------------|
| `conditioning`        | `CONDITIONING`        | Le conditionnement enrichi ou modifié, intégrant la sortie du modèle de style. Il représente le conditionnement final stylisé, prêt pour un traitement ou une génération ultérieure. |