# ModelMergeSubtract

Ce nœud est conçu pour des opérations avancées de fusion de modèles, permettant spécifiquement de soustraire les paramètres d'un modèle d'un autre en fonction d'un multiplicateur défini. Il permet de personnaliser les comportements des modèles en ajustant l'influence des paramètres d'un modèle sur un autre, facilitant ainsi la création de nouveaux modèles hybrides.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `modèle1` | Le modèle de base duquel les paramètres seront soustraits. | `MODEL` |
| `modèle2` | Le modèle dont les paramètres seront soustraits du modèle de base. | `MODEL` |
| `multiplicateur` | Une valeur à virgule flottante qui ajuste l'effet de la soustraction sur les paramètres du modèle de base. | `FLOAT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle résultant après avoir soustrait les paramètres d'un modèle d'un autre, ajusté par le multiplicateur. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSubtract/fr.md)
