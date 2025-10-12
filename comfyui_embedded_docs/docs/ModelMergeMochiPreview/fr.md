> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMochiPreview/fr.md)

Ce nœud fusionne deux modèles d'IA en utilisant une approche basée sur des blocs avec un contrôle précis des différentes composantes du modèle. Il permet de mélanger des modèles en ajustant les poids d'interpolation pour des sections spécifiques incluant les fréquences positionnelles, les couches d'embedding et les blocs de transformateurs individuels. Le processus de fusion combine les architectures et paramètres des deux modèles d'entrée selon les valeurs de poids spécifiées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle1` | MODEL | Oui | - | Premier modèle à fusionner |
| `modèle2` | MODEL | Oui | - | Second modèle à fusionner |
| `pos_frequencies.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation des fréquences positionnelles (par défaut : 1.0) |
| `t_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation de l'embedding temporel (par défaut : 1.0) |
| `t5_y_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation de l'embedding T5-Y (par défaut : 1.0) |
| `t5_yproj.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation de la projection T5-Y (par défaut : 1.0) |
| `blocks.0.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 0 (par défaut : 1.0) |
| `blocks.1.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 1 (par défaut : 1.0) |
| `blocks.2.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 2 (par défaut : 1.0) |
| `blocks.3.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 3 (par défaut : 1.0) |
| `blocks.4.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 4 (par défaut : 1.0) |
| `blocks.5.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 5 (par défaut : 1.0) |
| `blocks.6.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 6 (par défaut : 1.0) |
| `blocks.7.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 7 (par défaut : 1.0) |
| `blocks.8.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 8 (par défaut : 1.0) |
| `blocks.9.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 9 (par défaut : 1.0) |
| `blocks.10.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 10 (par défaut : 1.0) |
| `blocks.11.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 11 (par défaut : 1.0) |
| `blocks.12.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 12 (par défaut : 1.0) |
| `blocks.13.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 13 (par défaut : 1.0) |
| `blocks.14.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 14 (par défaut : 1.0) |
| `blocks.15.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 15 (par défaut : 1.0) |
| `blocks.16.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 16 (par défaut : 1.0) |
| `blocks.17.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 17 (par défaut : 1.0) |
| `blocks.18.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 18 (par défaut : 1.0) |
| `blocks.19.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 19 (par défaut : 1.0) |
| `blocks.20.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 20 (par défaut : 1.0) |
| `blocks.21.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 21 (par défaut : 1.0) |
| `blocks.22.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 22 (par défaut : 1.0) |
| `blocks.23.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 23 (par défaut : 1.0) |
| `blocks.24.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 24 (par défaut : 1.0) |
| `blocks.25.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 25 (par défaut : 1.0) |
| `blocks.26.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 26 (par défaut : 1.0) |
| `blocks.27.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 27 (par défaut : 1.0) |
| `blocks.28.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 28 (par défaut : 1.0) |
| `blocks.29.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 29 (par défaut : 1.0) |
| `blocks.30.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 30 (par défaut : 1.0) |
| `blocks.31.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 31 (par défaut : 1.0) |
| `blocks.32.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 32 (par défaut : 1.0) |
| `blocks.33.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 33 (par défaut : 1.0) |
| `blocks.34.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 34 (par défaut : 1.0) |
| `blocks.35.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 35 (par défaut : 1.0) |
| `blocks.36.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 36 (par défaut : 1.0) |
| `blocks.37.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 37 (par défaut : 1.0) |
| `blocks.38.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 38 (par défaut : 1.0) |
| `blocks.39.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 39 (par défaut : 1.0) |
| `blocks.40.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 40 (par défaut : 1.0) |
| `blocks.41.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 41 (par défaut : 1.0) |
| `blocks.42.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 42 (par défaut : 1.0) |
| `blocks.43.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 43 (par défaut : 1.0) |
| `blocks.44.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 44 (par défaut : 1.0) |
| `blocks.45.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 45 (par défaut : 1.0) |
| `blocks.46.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 46 (par défaut : 1.0) |
| `blocks.47.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation du bloc 47 (par défaut : 1.0) |
| `final_layer.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour l'interpolation de la couche finale (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée selon les poids spécifiés |
