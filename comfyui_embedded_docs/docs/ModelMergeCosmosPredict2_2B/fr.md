> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_2B/fr.md)

Le nœud ModelMergeCosmosPredict2_2B fusionne deux modèles de diffusion en utilisant une approche basée sur des blocs avec un contrôle précis des différentes composantes du modèle. Il vous permet de mélanger des parties spécifiques de deux modèles en ajustant les poids d'interpolation pour les encodeurs de position, les encodeurs de temps, les blocs transformeurs et les couches finales. Cela offre un contrôle précis sur la manière dont les différentes composantes architecturales de chaque modèle contribuent au résultat fusionné final.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Oui | - | Le premier modèle à fusionner |
| `model2` | MODEL | Oui | - | Le deuxième modèle à fusionner |
| `pos_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation de l'encodeur de position (par défaut : 1.0) |
| `x_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation de l'encodeur d'entrée (par défaut : 1.0) |
| `t_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation de l'encodeur de temps (par défaut : 1.0) |
| `t_embedding_norm.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation de la normalisation de l'embedding de temps (par défaut : 1.0) |
| `blocks.0.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 0 (par défaut : 1.0) |
| `blocks.1.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 1 (par défaut : 1.0) |
| `blocks.2.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 2 (par défaut : 1.0) |
| `blocks.3.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 3 (par défaut : 1.0) |
| `blocks.4.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 4 (par défaut : 1.0) |
| `blocks.5.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 5 (par défaut : 1.0) |
| `blocks.6.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 6 (par défaut : 1.0) |
| `blocks.7.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 7 (par défaut : 1.0) |
| `blocks.8.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 8 (par défaut : 1.0) |
| `blocks.9.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 9 (par défaut : 1.0) |
| `blocks.10.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 10 (par défaut : 1.0) |
| `blocks.11.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 11 (par défaut : 1.0) |
| `blocks.12.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 12 (par défaut : 1.0) |
| `blocks.13.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 13 (par défaut : 1.0) |
| `blocks.14.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 14 (par défaut : 1.0) |
| `blocks.15.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 15 (par défaut : 1.0) |
| `blocks.16.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 16 (par défaut : 1.0) |
| `blocks.17.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 17 (par défaut : 1.0) |
| `blocks.18.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 18 (par défaut : 1.0) |
| `blocks.19.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 19 (par défaut : 1.0) |
| `blocks.20.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 20 (par défaut : 1.0) |
| `blocks.21.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 21 (par défaut : 1.0) |
| `blocks.22.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 22 (par défaut : 1.0) |
| `blocks.23.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 23 (par défaut : 1.0) |
| `blocks.24.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 24 (par défaut : 1.0) |
| `blocks.25.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 25 (par défaut : 1.0) |
| `blocks.26.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 26 (par défaut : 1.0) |
| `blocks.27.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation du bloc transformeur 27 (par défaut : 1.0) |
| `final_layer.` | FLOAT | Oui | 0.0 - 1.0 | Poids d'interpolation de la couche finale (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée |