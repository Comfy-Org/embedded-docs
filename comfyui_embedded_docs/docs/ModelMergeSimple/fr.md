Le nœud ModelMergeSimple est conçu pour fusionner deux modèles en combinant leurs paramètres selon un ratio spécifié. Ce nœud facilite la création de modèles hybrides qui allient les forces ou caractéristiques des deux modèles d'entrée.

Le paramètre `ratio` détermine le rapport de mélange entre les deux modèles. Lorsque cette valeur est à 1, le modèle de sortie est composé à 100 % de `model1`, et lorsqu'elle est à 0, le modèle de sortie est composé à 100 % de `model2`.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `modèle1` | Le premier modèle à fusionner. Il sert de modèle de base sur lequel les correctifs du second modèle sont appliqués. | `MODEL` |
| `modèle2` | Le second modèle dont les correctifs sont appliqués au premier modèle, influencés par le ratio spécifié. | `MODEL` |
| `ratio` | Lorsque cette valeur est à 1, le modèle de sortie est composé à 100 % de `modèle1`, et lorsqu'elle est à 0, le modèle de sortie est composé à 100 % de `modèle2`. | `FLOAT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné résultant, incorporant des éléments des deux modèles d'entrée selon le ratio spécifié. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSimple/fr.md)
