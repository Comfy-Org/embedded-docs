# ModelMergeAdd

Voici la traduction en français de la documentation du nœud **ModelMergeAdd** :

Le nœud **ModelMergeAdd** est conçu pour fusionner deux modèles en ajoutant des correctifs clés d'un modèle à un autre. Ce processus consiste à cloner le premier modèle, puis à appliquer les correctifs du second modèle, permettant ainsi de combiner les caractéristiques ou comportements des deux modèles.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `modèle1` | Le premier modèle à cloner et auquel les correctifs du second modèle seront ajoutés. Il sert de modèle de base pour le processus de fusion. | `MODEL` |
| `modèle2` | Le second modèle dont les correctifs clés sont extraits et ajoutés au premier modèle. Il apporte des caractéristiques ou comportements supplémentaires au modèle fusionné. | `MODEL` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `model` | Le résultat de la fusion de deux modèles par ajout des correctifs clés du second modèle au premier. Ce modèle fusionné combine les caractéristiques ou comportements des deux modèles. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAdd/fr.md)
