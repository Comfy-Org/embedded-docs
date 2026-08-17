# Aperçu de la Fusion de Modèles Mochi

Ce nœud fusionne deux modèles d'IA selon une approche par blocs offrant un contrôle fin sur les différents composants du modèle. Il permet de mélanger les modèles en ajustant les poids d'interpolation pour des sections spécifiques, notamment les fréquences positionnelles, les couches d'incorporation (embeddings) et les blocs individuels du transformeur. Le processus de fusion combine les architectures et les paramètres des deux modèles d'entrée selon les valeurs de poids spécifiées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Le premier modèle à fusionner | MODEL | Oui | - |
| `model2` | Le deuxième modèle à fusionner | MODEL | Oui | - |
| `pos_frequencies.` | Poids pour l'interpolation des fréquences positionnelles (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `t_embedder.` | Poids pour l'interpolation de l'embedder temporel (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `t5_y_embedder.` | Poids pour l'interpolation de l'embedder T5-Y (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `t5_yproj.` | Poids pour l'interpolation de la projection T5-Y (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.0.` | Poids pour l'interpolation du bloc 0 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.1.` | Poids pour l'interpolation du bloc 1 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.2.` | Poids pour l'interpolation du bloc 2 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.3.` | Poids pour l'interpolation du bloc 3 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.4.` | Poids pour l'interpolation du bloc 4 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.5.` | Poids pour l'interpolation du bloc 5 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.6.` | Poids pour l'interpolation du bloc 6 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.7.` | Poids pour l'interpolation du bloc 7 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.8.` | Poids pour l'interpolation du bloc 8 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.9.` | Poids pour l'interpolation du bloc 9 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.10.` | Poids pour l'interpolation du bloc 10 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.11.` | Poids pour l'interpolation du bloc 11 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.12.` | Poids pour l'interpolation du bloc 12 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.13.` | Poids pour l'interpolation du bloc 13 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.14.` | Poids pour l'interpolation du bloc 14 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.15.` | Poids pour l'interpolation du bloc 15 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.16.` | Poids pour l'interpolation du bloc 16 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.17.` | Poids pour l'interpolation du bloc 17 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.18.` | Poids pour l'interpolation du bloc 18 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.19.` | Poids pour l'interpolation du bloc 19 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.20.` | Poids pour l'interpolation du bloc 20 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.21.` | Poids pour l'interpolation du bloc 21 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.22.` | Poids pour l'interpolation du bloc 22 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.23.` | Poids pour l'interpolation du bloc 23 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.24.` | Poids pour l'interpolation du bloc 24 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.25.` | Poids pour l'interpolation du bloc 25 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.26.` | Poids pour l'interpolation du bloc 26 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.27.` | Poids pour l'interpolation du bloc 27 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.28.` | Poids pour l'interpolation du bloc 28 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.29.` | Poids pour l'interpolation du bloc 29 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.30.` | Poids pour l'interpolation du bloc 30 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.31.` | Poids pour l'interpolation du bloc 31 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.32.` | Poids pour l'interpolation du bloc 32 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.33.` | Poids pour l'interpolation du bloc 33 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.34.` | Poids pour l'interpolation du bloc 34 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.35.` | Poids pour l'interpolation du bloc 35 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.36.` | Poids pour l'interpolation du bloc 36 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.37.` | Poids pour l'interpolation du bloc 37 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.38.` | Poids pour l'interpolation du bloc 38 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.39.` | Poids pour l'interpolation du bloc 39 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.40.` | Poids pour l'interpolation du bloc 40 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.41.` | Poids pour l'interpolation du bloc 41 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.42.` | Poids pour l'interpolation du bloc 42 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.43.` | Poids pour l'interpolation du bloc 43 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.44.` | Poids pour l'interpolation du bloc 44 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.45.` | Poids pour l'interpolation du bloc 45 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.46.` | Poids pour l'interpolation du bloc 46 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.47.` | Poids pour l'interpolation du bloc 47 (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `final_layer.` | Poids pour l'interpolation de la couche finale (défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée selon les poids spécifiés | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMochiPreview/fr.md)

---
**Source fingerprint (SHA-256):** `8fdf5d023d97ef04bf2b40577be5dbc4c16f8f4437586a98adbdbf7f9fa8a359`
