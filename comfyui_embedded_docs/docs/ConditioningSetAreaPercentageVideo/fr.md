# Pourcentage de la zone de conditionnement vidéo

Le nœud `ConditioningSetAreaPercentageVideo` modifie les données de conditionnement en définissant une zone spécifique et une région temporelle pour la génération vidéo. Il permet de définir la position, la taille et la durée de la zone où le conditionnement sera appliqué, en utilisant des valeurs en pourcentage relatives aux dimensions globales. Cela est utile pour concentrer la génération sur des parties spécifiques d'une séquence vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `conditioning` | Les données de conditionnement à modifier | CONDITIONING | Oui | - |
| `width` | La largeur de la zone en pourcentage de la largeur totale (par défaut : 1,0) | FLOAT | Oui | 0.0 - 1.0 |
| `height` | La hauteur de la zone en pourcentage de la hauteur totale (par défaut : 1,0) | FLOAT | Oui | 0.0 - 1.0 |
| `temporal` | La durée temporelle de la zone en pourcentage de la durée totale de la vidéo (par défaut : 1,0) | FLOAT | Oui | 0.0 - 1.0 |
| `x` | La position horizontale de départ de la zone en pourcentage (par défaut : 0,0) | FLOAT | Oui | 0.0 - 1.0 |
| `y` | La position verticale de départ de la zone en pourcentage (par défaut : 0,0) | FLOAT | Oui | 0.0 - 1.0 |
| `z` | La position temporelle de départ de la zone en pourcentage de la chronologie vidéo (par défaut : 0,0) | FLOAT | Oui | 0.0 - 1.0 |
| `strength` | Le multiplicateur de force appliqué au conditionnement dans la zone définie (par défaut : 1,0) | FLOAT | Oui | 0.0 - 10.0 |

Remarque : Toutes les valeurs de taille et de position sont des pourcentages normalisés (0,0 à 1,0) relatifs aux dimensions globales et à la chronologie de la vidéo.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `conditioning` | Les données de conditionnement modifiées avec la zone et les paramètres de force spécifiés appliqués | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/fr.md)

---
**Source fingerprint (SHA-256):** `9c5ddae6a2b1da5907fb52ef625eefb12b0b228fd3bd52c3033b5c4226d76150`
