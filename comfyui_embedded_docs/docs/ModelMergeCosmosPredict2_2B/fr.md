Le nœud `ModelMergeCosmosPredict2_2B` fusionne deux modèles de diffusion en utilisant une approche par blocs avec un contrôle fin sur les différents composants du modèle. Il permet de mélanger des parties spécifiques de deux modèles en ajustant les poids d'interpolation pour les intégrateurs de position, les intégrateurs temporels, les blocs de transformeurs et les couches finales. Cela offre un contrôle précis sur la manière dont les différents composants architecturaux de chaque modèle contribuent au résultat fusionné final.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle1` | Le premier modèle à fusionner | MODEL | Oui | - |
| `modèle2` | Le second modèle à fusionner | MODEL | Oui | - |
| `pos_embedder.` | Poids d'interpolation de l'intégrateur de position (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `x_embedder.` | Poids d'interpolation de l'intégrateur d'entrée (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedder.` | Poids d'interpolation de l'intégrateur temporel (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedding_norm.` | Poids d'interpolation de la normalisation de l'intégration temporelle (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.0.` | Poids d'interpolation du bloc de transformeur 0 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.1.` | Poids d'interpolation du bloc de transformeur 1 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.2.` | Poids d'interpolation du bloc de transformeur 2 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.3.` | Poids d'interpolation du bloc de transformeur 3 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.4.` | Poids d'interpolation du bloc de transformeur 4 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.5.` | Poids d'interpolation du bloc de transformeur 5 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.6.` | Poids d'interpolation du bloc de transformeur 6 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.7.` | Poids d'interpolation du bloc de transformeur 7 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.8.` | Poids d'interpolation du bloc de transformeur 8 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.9.` | Poids d'interpolation du bloc de transformeur 9 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.10.` | Poids d'interpolation du bloc de transformeur 10 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.11.` | Poids d'interpolation du bloc de transformeur 11 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.12.` | Poids d'interpolation du bloc de transformeur 12 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.13.` | Poids d'interpolation du bloc de transformeur 13 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.14.` | Poids d'interpolation du bloc de transformeur 14 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.15.` | Poids d'interpolation du bloc de transformeur 15 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.16.` | Poids d'interpolation du bloc de transformeur 16 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.17.` | Poids d'interpolation du bloc de transformeur 17 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.18.` | Poids d'interpolation du bloc de transformeur 18 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.19.` | Poids d'interpolation du bloc de transformeur 19 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.20.` | Poids d'interpolation du bloc de transformeur 20 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.21.` | Poids d'interpolation du bloc de transformeur 21 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.22.` | Poids d'interpolation du bloc de transformeur 22 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.23.` | Poids d'interpolation du bloc de transformeur 23 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.24.` | Poids d'interpolation du bloc de transformeur 24 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.25.` | Poids d'interpolation du bloc de transformeur 25 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.26.` | Poids d'interpolation du bloc de transformeur 26 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.27.` | Poids d'interpolation du bloc de transformeur 27 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `final_layer.` | Poids d'interpolation de la couche finale (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_2B/fr.md)

---
**Source fingerprint (SHA-256):** `53a8de66d6b731f5b29af326832f66cc973284bc8fdf09d779575f2346cc75a7`
