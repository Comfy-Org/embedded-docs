# Appliquer le modèle de style

Ce nœud applique un modèle de style à un conditionnement donné, en enrichissant ou en modifiant son style en fonction de la sortie d’un modèle CLIP vision. Il intègre le conditionnement du modèle de style dans le conditionnement existant, permettant ainsi un mélange harmonieux des styles dans le processus de génération.

## Entrées

### Requises

| Paramètre | Description | Type Comfy |
| --- | --- | --- |
| `conditionnement` | Les données de conditionnement d’origine auxquelles le conditionnement du modèle de style sera appliqué. Essentielles pour définir le contexte ou le style de base qui sera enrichi ou modifié. | `CONDITIONING` |
| `modèle_de_style` | Le modèle de style utilisé pour générer un nouveau conditionnement à partir de la sortie du modèle CLIP vision. Il joue un rôle clé dans la définition du nouveau style à appliquer. | `STYLE_MODEL` |
| `sortie_clip_vision` | La sortie d’un modèle CLIP vision, utilisée par le modèle de style pour générer un nouveau conditionnement. Elle fournit le contexte visuel nécessaire à l’application du style. | `CLIP_VISION_OUTPUT` |

## Sorties

| Paramètre | Description | Type Comfy |
| --- | --- | --- |
| `conditionnement` | Le conditionnement enrichi ou modifié, intégrant la sortie du modèle de style. Il représente le conditionnement final stylisé, prêt pour un traitement ou une génération ultérieure. | `CONDITIONING` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelApply/fr.md)
