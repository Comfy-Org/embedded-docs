Le nœud **ConditioningSetAreaPercentageVideo** modifie les données de conditionnement en définissant une zone spécifique et une région temporelle pour la génération vidéo. Il permet de définir la position, la taille et la durée de la zone où le conditionnement sera appliqué, en utilisant des valeurs en pourcentage relatives aux dimensions globales. Cela est utile pour concentrer la génération sur des parties spécifiques d'une séquence vidéo.

## Entrées

| Paramètre | Description | Type de données | Type d'entrée | Valeur par défaut | Plage |
| --- | --- | --- | --- | --- | --- |
| `conditionnement` | Les données de conditionnement à modifier | CONDITIONING | Requis | - | - |
| `largeur` | La largeur de la zone en pourcentage de la largeur totale | FLOAT | Requis | 1.0 | 0.0 - 1.0 |
| `hauteur` | La hauteur de la zone en pourcentage de la hauteur totale | FLOAT | Requis | 1.0 | 0.0 - 1.0 |
| `temporel` | La durée temporelle de la zone en pourcentage de la longueur totale de la vidéo | FLOAT | Requis | 1.0 | 0.0 - 1.0 |
| `x` | La position horizontale de départ de la zone en pourcentage | FLOAT | Requis | 0.0 | 0.0 - 1.0 |
| `y` | La position verticale de départ de la zone en pourcentage | FLOAT | Requis | 0.0 | 0.0 - 1.0 |
| `z` | La position temporelle de départ de la zone en pourcentage de la timeline vidéo | FLOAT | Requis | 0.0 | 0.0 - 1.0 |
| `force` | Le multiplicateur de force appliqué au conditionnement dans la zone définie | FLOAT | Requis | 1.0 | 0.0 - 10.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `conditionnement` | Les données de conditionnement modifiées avec les paramètres de zone et de force spécifiés appliqués | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/fr.md)

---
**Source fingerprint (SHA-256):** `72d4bef4f8ddc4765cf69863f7ad03d34992f0ff30a963dbe2dc1b7d69815410`
