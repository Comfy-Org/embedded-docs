
Ce nœud applique un modèle de style à un conditionnement donné, en améliorant ou en modifiant son style basé sur la sortie d'un modèle de vision CLIP. Il intègre le conditionnement du modèle de style dans le conditionnement existant, permettant une fusion harmonieuse des styles dans le processus de génération.

## Entrées

### Requis

| Paramètre             | Comfy dtype          | Description |
|-----------------------|-----------------------|-------------|
| `conditioning`        | `CONDITIONING`       | Les données de conditionnement originales auxquelles le conditionnement du modèle de style sera appliqué. C'est crucial pour définir le contexte ou le style de base qui sera amélioré ou modifié. |
| `style_model`         | `STYLE_MODEL`        | Le modèle de style utilisé pour générer un nouveau conditionnement basé sur la sortie du modèle de vision CLIP. Il joue un rôle clé dans la définition du nouveau style à appliquer. |
| `clip_vision_output`  | `CLIP_VISION_OUTPUT` | La sortie d'un modèle de vision CLIP, utilisée par le modèle de style pour générer un nouveau conditionnement. Elle fournit le contexte visuel nécessaire pour l'application du style. |

## Sorties

| Paramètre            | Comfy dtype           | Description |
|----------------------|-----------------------|-------------|
| `conditioning`       | `CONDITIONING`        | Le conditionnement amélioré ou modifié, incorporant la sortie du modèle de style. Il représente le conditionnement final, stylisé, prêt pour un traitement ou une génération ultérieure. |
