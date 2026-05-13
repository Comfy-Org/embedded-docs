> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSimple/fr.md)

Le nœud ModelMergeSimple est conçu pour fusionner deux modèles en combinant leurs paramètres selon un ratio spécifié. Ce nœud facilite la création de modèles hybrides qui allient les forces ou caractéristiques des deux modèles d'entrée.

Le paramètre `ratio` détermine le rapport de mélange entre les deux modèles. Lorsque cette valeur est à 1, le modèle de sortie est composé à 100 % de `model1`, et lorsqu'elle est à 0, le modèle de sortie est composé à 100 % de `model2`.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `model1`  | `MODEL`         | Le premier modèle à fusionner. Il sert de modèle de base sur lequel les correctifs du second modèle sont appliqués. |
| `model2`  | `MODEL`         | Le second modèle dont les correctifs sont appliqués au premier modèle, influencés par le ratio spécifié. |
| `ratio`   | `FLOAT`         | Lorsque cette valeur est à 1, le modèle de sortie est composé à 100 % de `model1`, et lorsqu'elle est à 0, le modèle de sortie est composé à 100 % de `model2`. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `model`   | MODEL           | Le modèle fusionné résultant, incorporant des éléments des deux modèles d'entrée selon le ratio spécifié. |